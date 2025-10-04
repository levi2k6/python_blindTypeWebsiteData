import os
import json

locations = {}

letterJson = [];
wordJson = [];
sentenceJson = [];

def start():
    global locations
    with open("data/location.json") as file:
        data = json.load(file)
        if not data:
            print("Failed to initialize system.");
            return;

        locations = data;
        print("locations: ", locations)
        print("Initialization success.")
    loadJson()

def loadJson():
    global letterJson;
    global wordJson;
    global sentenceJson;

    letterPath = os.path.expanduser(locations["letterLocation"])
    print("letterPath: ", letterPath)

    with open(letterPath) as file:
        data = json.load(file)
        if not data:
            print("data is empty");

        letterJson = data;


    wordPath = os.path.expanduser(locations["wordLocation"])
    print("wordPath: ", wordPath)

    with open(wordPath) as file:
        data = json.load(file)
        if not data:
            print("data is empty");

        wordJson = data;

    sentencePath = os.path.expanduser(locations["sentenceLocation"])
    print("sentencePath: ", sentencePath)

    with open(sentencePath) as file:
        data = json.load(file)
        if not data:
            print("data is empty");

        sentenceJson = data;


start()
