
import dataManager

import os
import json

with open("data/location.json") as file:
    location = json.load(file)
    if not location:
        print("location is empty");
    else:
        print(location["sentenceLocation"])

path = os.path.expanduser(location["sentenceLocation"]);

with open(path) as file:
    data = json.load(file)
    if not data:
        print("data is empty");
    # else: 
    #     print(data["sentences"]);

def main():
    userInput = input("Enter action: ");

    if userInput == "addData":
        addData();
        main();
    elif userInput == "exist":
        print("Program off")

   
def addData():
    for datum in data["sentences"]:
        print(datum)
        dataManager.postData(datum)

main()

