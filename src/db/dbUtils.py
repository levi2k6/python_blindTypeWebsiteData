import json
import mysql.connector

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


def isTableEmpty( type: str):

    table = typeToTable(type);

    conn = getConn()
    cursor = conn.cursor()
    cursor.execute(f"SELECT COUNT(*) FROM {table}")
    count = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return count == 0;

