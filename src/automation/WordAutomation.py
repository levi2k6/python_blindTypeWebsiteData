from db import dbUtils
import initialize
from automation.AutomationStrategy import AutomationStrategy 

from db.DbManager import DbManager
from db import dbUtils
from audio_manager.AudioManager import AudioManager 

class WordAutomation(AutomationStrategy):

    def __init__(self, audioManager: AudioManager, dbManager: DbManager):
        self.audioManager = audioManager 
        self.dbManager = dbManager
        

    def addAllChallengeDb(self):
        for datum in initialize.wordJson:
            if not self.dbManager.getData(datum):
                self.dbManager.setCurrentDbStrategy("word");
                self.dbManager.postData(datum);

                self.audioManager.setCurrentAudioFile("word");
                self.audioManager.generateAudioFile(datum);

                print("Sentence table has been successfully added data into it.")
            else:
                print("word_challenges already has data")
                return
            
        pass

    def deleteAllChallengeDb(self):
        if not dbUtils.isTableEmpty("word"):
            self.dbManager.setCurrentDbStrategy("word")
            self.dbManager.deleteData();
        else:
            print("word_challenges table is already empty")

        self.audioManager.setCurrentAudioFile("word");
        self.audioManager.deleteAudioFile();
        pass



