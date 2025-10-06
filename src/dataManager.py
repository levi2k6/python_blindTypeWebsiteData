import initialize
import json
import mysql.connector
import AudioManager

import uuid
import os

import dataManager

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
        return "sentence_challenges"
    elif type == "word":
        return "word_challenges"
    elif type == "letter":
        return "letter_challenges"


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

    AudioManager.generateAudioFiles(text, fileName, type);

    table = typeToTable(type); 

    sql = ""
    values = ()

    if type == "sentence":
        sql = f"INSERT INTO {table}( difficulty, text, audio_name) VALUES( %s, %s, %s)"
        values = ("easy", text, fileName)
    elif type == "word":
        sql = f"INSERT INTO {table}( difficulty, text) VALUES( %s, %s)"
        values = ("easy", text)
    elif type == "letter":
        sql = f"INSERT INTO {table}(text) VALUES( %s )"
        values = (text,)

    cursor.execute(sql, values)
    conn.commit();

    cursor.close()
    conn.close()

def getData(text, type):
    conn = getConn()
    cursor = conn.cursor()
    
    table = typeToTable(type)
    sql = f"SELECT * FROM {table} WHERE text = %s" 
    cursor.execute(sql, (text,))
    challenge = cursor.fetchall()
    return challenge 


def deleteData(type):
    conn = getConn()
    cursor = conn.cursor()

    table = typeToTable(type);

    sql = f"TRUNCATE TABLE {table}";
    cursor.execute(sql);
    conn.commit();

    cursor.close()
    conn.close()
    print(f"{type} table successfully deleted.")


def test(text, type):
    if getData(text, type):
        print("Challenge already existed.")
        return
    print("Challenge not found")


