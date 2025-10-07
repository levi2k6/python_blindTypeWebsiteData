from db import dbUtils
import initialize
from automation.AutomationStrategy import AutomationStrategy 

from db.DbManager import DbManager
from db import dbUtils
from audio_manager.AudioManager import AudioManager 

class LetterAutomation(AutomationStrategy):

    def __init__(self, audioManager: AudioManager, dbManager: DbManager):
        self.audioManager = audioManager 
        self.dbManager = dbManager
        

    def addAllChallengeDb(self):
        for datum in initialize.letterJson:
            if not self.dbManager.getData(datum):
                self.dbManager.setCurrentDbStrategy("letter");
                self.dbManager.postData(datum);

                self.audioManager.setCurrentAudioFile("letter");
                self.audioManager.generateAudioFile(datum);

                print("Sentence table has been successfully added data into it.")
            else:
                print("letter_challenges already has data")
                return
            
        pass

    def deleteAllChallengeDb(self):
        if not dbUtils.isTableEmpty("letter"):
            self.dbManager.setCurrentDbStrategy("letter")
            self.dbManager.deleteData();
        else:
            print("letter_challenges table is already empty")

        self.audioManager.setCurrentAudioFile("letter");
        self.audioManager.deleteAudioFile();
        pass

