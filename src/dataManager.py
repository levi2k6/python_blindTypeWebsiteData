import initialize
import json
import mysql.connector
import textReader

import uuid
import os

with open("data/dbConfig.json") as file:
    config = json.load(file)

def postData(text):
    conn = mysql.connector.connect(
        host = config["host"],
        user = config["user"],
        password = config["password"],
        database = config["database"]
    )

    cursor = conn.cursor()

    fileName = text.replace(" ","_") 
    textReader.generateAudioFile(text, fileName);

    sql = "INSERT INTO sentence_challenges( difficulty, text, audio_name) VALUES( %s, %s, %s)";
    values = ("easy", text, fileName);
    cursor.execute(sql, values)
    conn.commit();


    cursor.close()
    conn.close()


