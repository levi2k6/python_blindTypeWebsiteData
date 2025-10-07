from abc import ABC, abstractmethod

class dbStrategy(ABC): 

    @abstractmethod
    def postData(self, text: str):
        pass


    @abstractmethod
    def getData(self, text):
        pass


    @abstractmethod
    def deleteData(self):
        pass


