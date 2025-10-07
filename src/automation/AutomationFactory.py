from automation.AutomationStrategy import AutomationStrategy 
from automation.SentenceAutomation import SentenceAutomation
from automation.WordAutomation import WordAutomation
from automation.LetterAutomation import LetterAutomation
from audio_manager.AudioManager import AudioManager
from db.DbManager import DbManager

class AutomationFactory:

    def __init__(self, audioManager: AudioManager, dbManager: DbManager):
        self.audioManager = audioManager
        self.dbManager = dbManager

    def createAutomation(self, automation: str)-> AutomationStrategy: 
        if automation == "sentence":
            return SentenceAutomation(self.audioManager, self.dbManager)
        elif automation == "word": 
            return WordAutomation(self.audioManager, self.dbManager) 
        elif automation == "letter":
            return LetterAutomation(self.audioManager, self.dbManager)
        else:
            raise ValueError("Unknown automation type.")
    




