
import initialize
import dataManager
import test

import os
import json

jsonData = {};

def loadJson():
    global jsonData

    path = os.path.expanduser(initialize.locations["sentenceLocation"]);

    with open(path) as file:
        data = json.load(file)
        if not data:
            print("data is empty");
        # else: 
        #     print(data["sentences"]);
        jsonData = data

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
    elif userInput == "deleteSentence":
        deleteData("sentence");
    elif userInput == "seleteWord":
        deleteData("word")
    elif userInput == "exit":
        print("Program off")
    elif userInput == "test":
        test.test();
        main();
    else:
        print("Invalid input");
        main();

def addData(type):
    if not dataManager.isTableEmpty(type):
        print(f"{type} all ready has data.")
        return

    for datum in jsonData["sentences"]:
        print(datum)
        dataManager.postData(datum, type)

def deleteData(type):
    if dataManager.isTableEmpty(type):
        print(f"{type} all ready is already empty.")
        return
    dataManager.deleteData(type);
    

initialize.start()
loadJson()
main()

