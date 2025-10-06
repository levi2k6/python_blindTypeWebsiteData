from typing import Dict, List
from automation.AutomationContext import AutomationContext


class Input:

    def __init__(self, automationContext: AutomationContext):
        self.commands: Dict = {
            "addAll": self.addAll,
            "addSentence": self.addSentence,
            "addWord": self.addWord,
            "addLetter": self.addLetter,
            "deleteSentence": self.deleteSentence,
            "deleteWord": self.deleteWord,
            "deleteLetter": self.deleteLetter
        };

        self.automationContext: AutomationContext = automationContext

    def executeInput(self, userInput: str):
        if userInput in self.commands: 
            self.commands[userInput]
        else:
            self.invalidInput();
         
    def addAll(self):
        self.automationContext.setAutomationStrategy("sentence")
        self.automationContext.addAllChallengeDb();
        self.automationContext.setAutomationStrategy("word")
        self.automationContext.addAllChallengeDb();
        self.automationContext.setAutomationStrategy("letter")
        self.automationContext.addAllChallengeDb();

    def addSentence(self):
        self.automationContext.setAutomationStrategy("sentence")
        self.automationContext.addAllChallengeDb();

    def addWord(self):
        self.automationContext.setAutomationStrategy("word")
        self.automationContext.addAllChallengeDb();

    def addLetter(self):
        self.automationContext.setAutomationStrategy("letter")
        self.automationContext.addAllChallengeDb();

    def deleteAll(self):
        self.automationContext.setAutomationStrategy("sentence")
        self.automationContext.deleteAllChallengeDb();

    def deleteSentence(self): 
        self.automationContext.setAutomationStrategy("sentence")
        self.automationContext.deleteAllChallengeDb();

    def deleteWord(self): 
        self.automationContext.setAutomationStrategy("word")
        self.automationContext.deleteAllChallengeDb();

    def deleteLetter(self): 
        self.automationContext.setAutomationStrategy("letter")
        self.automationContext.deleteAllChallengeDb();

    def invalidInput(self):
        print("Invalid Input")


