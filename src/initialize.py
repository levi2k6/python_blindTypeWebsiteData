import os
import json

locations = {}

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
        print("Initialization success.")

    loadJson()

def loadJson():
    global wordJson;
    global sentenceJson;

    wordPath = os.path.expanduser(locations["wordLocation"])
    print("wordPath: ", wordPath)

    with open(wordPath) as file:
        data = json.load(file)
        if not data:
            print("data is empty");

        wordJson = data;

    sentencePath = os.path.expanduser(locations["sentenceLocation"])
    with open(sentencePath) as file:
        data = json.load(file)
        if not data:
            print("data is empty");

        sentenceJson = data;

