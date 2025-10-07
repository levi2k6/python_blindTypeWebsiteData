from automation.AutomationStrategy import AutomationStrategy  
from typing import Optional

from audio_manager.AudioManager import AudioManager
from automation.AutomationFactory import AutomationFactory

class AutomationContext:
   
    def __init__(self, automationFactory, audioManager: AudioManager):
        self.automationFactory = automationFactory
        self.audioManager = audioManager

        self.automationFactory: AutomationFactory; 
        self.currentAutomation: AutomationStrategy | None = None 


    def setAutomationStrategy(self, strategyType: str):
        print("AutomationContext: ", "setAutomationStrategy()")
        self.currentAutomation = self.automationFactory.createAutomation(strategyType)   
        print("currentAutomation: ", self.currentAutomation)


    def addAllChallengeDb(self): 
        if not self.currentAutomation:
            return
        self.currentAutomation.addAllChallengeDb();
            
    def deleteAllChallengeDb(self): 
        if not self.currentAutomation:
            return
        self.currentAutomation.deleteAllChallengeDb();

    def regenerateAudioFile(self, fileName):
        self.audioManager.regenerateAudioFile(fileName);



