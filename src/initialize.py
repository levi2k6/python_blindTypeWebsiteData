
import json

locations = {}

def start():
    global locations
    with open("data/location.json") as file:
        data = json.load(file)
        if not data:
            print("Failed to initialize system.");
            return;

        locations = data;
        print("Initialization success.")




