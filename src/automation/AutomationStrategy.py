
from abc import ABC, abstractmethod

class AutomationStrategy(ABC): 

    @abstractmethod
    def addAllChallengeDb(self):
        pass

    @abstractmethod
    def deleteAllChallengeDb(self):
        pass




