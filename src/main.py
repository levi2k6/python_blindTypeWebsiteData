
import initialize
import dataManager
import test

import os
import json

def main():
    userInput = input("Enter action: ");

    if userInput == "addAll":
        addData("sentence");
        addData("word");
        main();
    elif userInput == "addSentence":
        addData("sentence");
        main();
    elif userInput == "addWord":
        addData("word");
        main();
    elif userInput == "deleteAll":
        deleteData("sentence") 
        deleteData("word")
        main();
    elif userInput == "deleteSentence":
        deleteData("sentence");
        main();
    elif userInput == "deleteWord":
        deleteData("word")
        main();
    elif userInput == "exit":
        print("Program off")
        main();
    elif userInput == "test":
        test.test();
        main();
    else:
        print("Invalid input");
        main();

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
   
def deleteData(type):
    dataManager.deleteData(type);

initialize.start()
main()

