from abc import ABC, abstractmethod

class Audio(ABC):

    @abstractmethod
    def generateAudioFile(self, text):
        pass
         
    @abstractmethod
    def deleteAudioFile(self): 
        pass

    @abstractmethod
    def regenerateAudioFile(self, fileName):
        pass


