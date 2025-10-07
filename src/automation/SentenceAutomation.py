from db import dbUtils
import initialize
from automation.AutomationStrategy import AutomationStrategy 

from db.DbManager import DbManager
from db import dbUtils
from audio_manager.AudioManager import AudioManager 

class SentenceAutomation(AutomationStrategy):

    def __init__(self, audioManager: AudioManager, dbManager: DbManager):
        self.audioManager = audioManager 
        self.dbManager = dbManager
        

    def addAllChallengeDb(self):
        for datum in initialize.sentenceJson:
            if not self.dbManager.getData(datum):
                self.dbManager.setCurrentDbStrategy("sentence");
                self.dbManager.postData(datum);

                self.audioManager.setCurrentAudioFile("sentence");
                self.audioManager.generateAudioFile(datum);

                print("Sentence table has been successfully added data into it.")
            else:
                print("sentence_challenges already has data")
                return
            
        pass

    def deleteAllChallengeDb(self):
        if not dbUtils.isTableEmpty("sentence"):
            self.dbManager.setCurrentDbStrategy("sentence")
            self.dbManager.deleteData();
        else:
            print("sentence_challenges table is already empty")

        self.audioManager.setCurrentAudioFile("sentence");
        self.audioManager.deleteAudioFile();
        pass


