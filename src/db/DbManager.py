import json
from db.dbStrategy import dbStrategy
from typing import Optional  
from db.DbFactory import DbFactory 

class DbManager:

    def __init__(self):
        self.currentDbStrategy: dbStrategy | None = None

    def setCurrentDbStrategy(self, type: str): 
        print("DbManager ", "setCurrentDbStrategy")
        self.currentDbStrategy = DbFactory.createDbStrategy(type) 
        print("currentDbStrategy: ", self.currentDbStrategy)


    def postData(self, text: str):
        if not self.currentDbStrategy:
            return

        self.currentDbStrategy.postData(text);
        

    def getData(self, text):
        if not self.currentDbStrategy:
            return

        self.currentDbStrategy.getData(text);


    def deleteData(self):
        if not self.currentDbStrategy:
            return

        self.currentDbStrategy.deleteData();


