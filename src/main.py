
from automation.AutomationContext import AutomationContext
from automation.AutomationFactory import AutomationFactory
import initialize
import dataManager
import AudioManager
import test
from input.Input import Input

def main():
    userInput = input("Enter action: ");

    automationContext = AutomationFactory()
    automationContext =  AutomationContext(automationContext)
    input = Input(automationContext)



def regenAudio(type, input):
    print("regenAudio()")
    if type == "sentence": 
        for datum in initialize.sentenceJson:
            if datum == input:
                fileName = datum.replace(" ","_") 
                AudioManager.regenerateAudioFile(input, fileName, "sentence");
    elif type == "word": 
        for datum in initialize.wordJson:
            if datum == input:
                fileName = datum.replace(" ","_") 
                AudioManager.regenerateAudioFile(input, fileName, "word");
    elif type == "letter":
        for datum in initialize.letterJson:
            if datum == input:
                fileName = datum.replace(" ","_") 
                AudioManager.regenerateAudioFile(input, fileName, "letter");
    else:
        print("audio file not found in ", type);

   

main()

