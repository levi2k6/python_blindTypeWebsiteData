import json
from db.dbStrategy import dbStrategy
from db import dbUtils

class LetterDb(dbStrategy):

    def postData(self, text: str):
        conn = dbUtils.getConn()
        cursor = conn.cursor()

        fileName = text.replace(" ","_") 

        sql = ""
        values = ()

        sql = f"INSERT INTO letter_challenges(text) VALUES(%s)"
        values = (text,)
       
        cursor.execute(sql, values)
        conn.commit();

        cursor.close()
        conn.close()

    def getData(self, text):
        conn = dbUtils.getConn()
        cursor = conn.cursor()
        
        sql = f"SELECT * FROM letter_challenges WHERE text = %s" 
        cursor.execute(sql, (text,))
        challenge = cursor.fetchall()
        return challenge 


    def deleteData(self):
        conn = dbUtils.getConn()
        cursor = conn.cursor()

        sql = "TRUNCATE TABLE letter_challenges";
        cursor.execute(sql);
        conn.commit();

        cursor.close()
        conn.close()
        print("Letter table successfully deleted.")

