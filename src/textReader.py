from TTS.api import TTS

import initialize

import os
import shutil
import json

ttsSentence = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=True, gpu=False)
ttsWord = TTS(model_name="tts_models/en/ljspeech/vits--neon", progress_bar=True, gpu=False)

def generateAudioFiles(text, fileName, type):
    audioPath = f"{initialize.locations['mp3Location']}/{type}/{fileName}.mp3"
    os.makedirs(f"{initialize.locations['mp3Location']}/{type}", exist_ok=True)

    if(type == "sentence"):
        ttsSentence.tts_to_file(text=text, file_path=audioPath, speed=0.2)
        print("sentence model used")
    elif(type == "word"):
        ttsWord.tts_to_file(text=text, file_path=audioPath, speed=0.1)
        print("word model used")
    elif(type == "letter"):
        ttsWord.tts_to_file(text=text, file_path=audioPath, speed=0.1)
        print("letter model used")


def deleteGeneratedAudioFiles(type):
    try:
        shutil.rmtree(f"{initialize.locations['mp3Location']}/{type}")
        print(f"{type} folder successfully deleted")
    except FileNotFoundError: 
        print(f"{type} folder not found")
    except PermissionError:
        print("No permission to delete")
    except OSError as e:
        print(f"{type} folder OS error: {e}")


