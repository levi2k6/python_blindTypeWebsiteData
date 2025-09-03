
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

    if userInput == "addData":
        addData();
        main();
    elif userInput == "test":
        test.test();
    elif userInput == "exit":
        print("Program off")
    else:
        print("Invalid input");

   
def addData():
    for datum in jsonData["sentences"]:
        print(datum)
        dataManager.postData(datum)

initialize.start()
loadJson()
main()

