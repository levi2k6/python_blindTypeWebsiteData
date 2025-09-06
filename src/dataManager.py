import initialize
import json
import mysql.connector
import textReader

import uuid
import os

with open("data/dbConfig.json") as file:
    config = json.load(file)

def getConn():
    conn = mysql.connector.connect(
            host = config["host"],
            user = config["user"],
            password = config["password"],
            database = config["database"]
    )
    return conn;

def typeToTable(type):
    if type == "sentence":
        return "sentence_challenges"; 
    elif type == "word":
        return "word_challenges"; 


def isTableEmpty(type: str):

    table = typeToTable(type);

    conn = getConn()
    cursor = conn.cursor()
    cursor.execute(f"SELECT COUNT(*) FROM {table}")
    count = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return count == 0;


def postData(text, type):
    conn = getConn()
    cursor = conn.cursor()

    fileName = text.replace(" ","_") 
    textReader.generateAudioFiles(text, fileName, type);

    table = typeToTable(type); 

    sql = f"INSERT INTO {table}( difficulty, text, audio_name) VALUES( %s, %s, %s)";
    values = ("easy", text, fileName);
    cursor.execute(sql, values)
    conn.commit();

    cursor.close()
    conn.close()

def deleteData(type):
    conn = getConn()
    cursor = conn.cursor()

    table = typeToTable(type);

    sql = f"TRUNCATE TABLE {table}";
    cursor.execute(sql);
    conn.commit();

    textReader.deleteGeneratedAudioFiles(type);




