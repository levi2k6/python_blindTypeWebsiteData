from typing import Dict, List
from automation.AutomationContext import AutomationContext

class InputCommand:

    def __init__(self, automationContext: AutomationContext):
        self.commands: Dict = {
            "addAll": self.addAll,
            "addSentence": self.addSentence,
            "addWord": self.addWord,
            "addLetter": self.addLetter,
            "deleteAll": self.deleteAll,
            "deleteSentence": self.deleteSentence,
            "deleteWord": self.deleteWord,
            "deleteLetter": self.deleteLetter,
            "quit": self.quit,
            "test" : self.test
        };

        self.automationContext: AutomationContext = automationContext

    def makeInput(self):
        userInput = input("Enter action: ");
        if userInput in self.commands: 
            self.commands[userInput]()
        else:
            self.invalidInput();
         
    def addAll(self):
        self.automationContext.setAutomationStrategy("sentence")
        self.automationContext.addAllChallengeDb();
        self.automationContext.setAutomationStrategy("word")
        self.automationContext.addAllChallengeDb();
        self.automationContext.setAutomationStrategy("letter")
        self.automationContext.addAllChallengeDb();
        self.makeInput();

    def addSentence(self):
        self.automationContext.setAutomationStrategy("sentence")
        self.automationContext.addAllChallengeDb()
        self.makeInput();

    def addWord(self):
        self.automationContext.setAutomationStrategy("word")
        self.automationContext.addAllChallengeDb()
        self.makeInput();

    def addLetter(self):
        self.automationContext.setAutomationStrategy("letter")
        self.automationContext.addAllChallengeDb()
        self.makeInput();

    def deleteAll(self):
        self.automationContext.setAutomationStrategy("sentence")
        self.automationContext.deleteAllChallengeDb()
        self.automationContext.setAutomationStrategy("word")
        self.automationContext.deleteAllChallengeDb()
        self.automationContext.setAutomationStrategy("letter")
        self.makeInput();

    def deleteSentence(self): 
        self.automationContext.setAutomationStrategy("sentence")
        self.automationContext.deleteAllChallengeDb();
        self.makeInput();

    def deleteWord(self): 
        self.automationContext.setAutomationStrategy("word")
        self.automationContext.deleteAllChallengeDb();
        self.makeInput();

    def deleteLetter(self): 
        print("deleteLetter()")
        self.automationContext.setAutomationStrategy("letter")
        self.automationContext.deleteAllChallengeDb();
        self.makeInput();

    def quit(self):
        print("System shutdown")

    def test(self):
        self.makeInput();
        pass

    def invalidInput(self):
        print("Invalid Input")
        self.makeInput();


