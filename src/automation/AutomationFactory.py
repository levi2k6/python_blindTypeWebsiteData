from AutomationStrategy import AutomationStrategy 
from SentenceAutomation import SentenceAutomation
from WordAutomation import WordAutomation
from LetterAutomation import LetterAutomation

class AutomationFactory:

    def createAutomatio(self, automation: str)-> AutomationStrategy: 
        if automation == "sentence":
            return SentenceAutomation()
        elif automation == "word": 
            return WordAutomation() 
        elif automation == "letter":
            return LetterAutomation()
        else:
            raise ValueError("Unknown automation type.")
    




