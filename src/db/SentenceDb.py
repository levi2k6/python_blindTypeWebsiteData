import json
from db.dbStrategy import dbStrategy
from db import dbUtils

class SentenceDb(dbStrategy):

    def postData(self, text: str):
        conn = dbUtils.getConn()
        cursor = conn.cursor()

        fileName = text.replace(" ","_") 

        sql = ""
        values = ()

        sql = f"INSERT INTO sentence_challenges(difficulty, text, audio_name) VALUES( %s, %s, %s)"
        values = ("easy", text, fileName)
        
        cursor.execute(sql, values)
        conn.commit();

        cursor.close()
        conn.close()

    def getData(self, text):
        conn = dbUtils.getConn()
        cursor = conn.cursor()
        
        sql = f"SELECT * FROM sentence_challenges WHERE text = %s" 
        cursor.execute(sql, (text,))
        challenge = cursor.fetchall()
        return challenge 


    def deleteData(self):
        conn = dbUtils.getConn()
        cursor = conn.cursor()

        sql = "TRUNCATE TABLE sentence_challenges";
        cursor.execute(sql);
        conn.commit();

        cursor.close()
        conn.close()
        print("Sentence table successfully deleted.")

