
import json
import mysql.connector

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

    sql = "INSERT INTO sentence_challenges( difficulty, text) VALUES( %s, %s)";
    values = ("easy", text);
    cursor.execute(sql, values)
    conn.commit();

    cursor.close()
    conn.close()


