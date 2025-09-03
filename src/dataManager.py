import initialize
import json
import mysql.connector
import textReader
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
    audioPath = os.path.expanduser(f"{initialize.locations['mp3Location']}{fileName}.mp3")
    textReader.generateAudioFile(text, audioPath);

    sql = "INSERT INTO sentence_challenges( difficulty, text, audio_path) VALUES( %s, %s, %s)";
    values = ("easy", text, audioPath);
    cursor.execute(sql, values)
    conn.commit();


    cursor.close()
    conn.close()


