
import initialize
import dataManager
import textReader
import test

def main():
    userInput = input("Enter action: ");

    if userInput == "addAll":
        addData("sentence")
        addData("word")
        addData("letter")
        main()
    elif userInput == "addSentence":
        addData("sentence")
        main()
    elif userInput == "addWord":
        addData("word")
        main()
    elif userInput == "addLetter":
        addData("letter")
        main()
    elif userInput == "deleteAll":
        deleteData("sentence") 
        deleteData("word")
        deleteData("letter")
        main()
    elif userInput == "deleteSentence":
        deleteData("sentence")
        main()
    elif userInput == "deleteWord":
        deleteData("word")
        main()
    elif userInput == "deleteLetter":
        deleteData("letter")
        main()
    elif userInput == "regenSentence":
        userInput = input("find sentence: ")
        regenAudio("sentence", userInput)
        main()
    elif userInput == "regenWord":
        userInput = input("find word: ")
        regenAudio("word", userInput)
        main()
    elif userInput == "regenLetter":
        userInput = input("find letter: ")
        regenAudio("letter", userInput)
        main()
    elif userInput == "exit":
        print("Program off")
    elif userInput == "test":
        test.test()
        main()
    else:
        print("Invalid input");
        main()

def addData(type):
    if not dataManager.isTableEmpty(type):
       print(f"{type} table already has data in it.")
       return

    if type == "sentence": 
        for datum in initialize.sentenceJson:
            print(datum)
            dataManager.postData(datum, type)
    if type == "word": 
        for datum in initialize.wordJson:
            print(datum)
            dataManager.postData(datum, type)
    if type == "letter":
        for datum in initialize.letterJson:
            print(datum)
            dataManager.postData(datum, type)


def regenAudio(type, input):
    print("regenAudio()")
    if type == "sentence": 
        for datum in initialize.sentenceJson:
            if datum == input:
                fileName = datum.replace(" ","_") 
                textReader.regenerateAudioFile(input, fileName, "sentence");
    elif type == "word": 
        for datum in initialize.wordJson:
            if datum == input:
                fileName = datum.replace(" ","_") 
                textReader.regenerateAudioFile(input, fileName, "word");
    elif type == "letter":
        for datum in initialize.letterJson:
            if datum == input:
                fileName = datum.replace(" ","_") 
                textReader.regenerateAudioFile(input, fileName, "letter");
    else:
        print("audio file not found in ", type);

   
def deleteData(type):
    dataManager.deleteData(type);

main()

