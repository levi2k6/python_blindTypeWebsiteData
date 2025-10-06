from AutomationStrategy import AutomationStrategy 
from typing import Optional

from automation.AutomationFactory import AutomationFactory


class AutomationContext:

    automationFactory: AutomationFactory; 

    currentAutomation: Optional[AutomationStrategy] = None 

    def __init__(self, automationFactory):
        self.automationFactory = automationFactory

    def setAutomationStrategy(self, automationName: str):
        self.automationStrategy = self.automationFactory.createAutomatio(automationName)   

    def addAllChallengeDb(self): 
        if not self.currentAutomation:
            return
        self.currentAutomation.addAllChallengeDb();
            
    def deleteAllChallengeDb(self): 
        if not self.currentAutomation:
            return
        self.currentAutomation.deleteAllChallengeDb();

