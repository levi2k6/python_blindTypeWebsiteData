from TTS.api import TTS

import initialize


import os
import shutil
import json

tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=True, gpu=False)

def generateAudioFiles(text, fileName, type):

    audioPath = f"{initialize.locations['mp3Location']}/{type}/{fileName}.mp3"
    os.makedirs(f"{initialize.locations['mp3Location']}/{type}", exist_ok=True)
    tts.tts_to_file(text=text, file_path=audioPath, speed=0.2)

def deleteGeneratedAudioFiles(type):
    try:
        shutil.rmtree(f"{initialize.locations['mp3Location']}/{type}")
        print("Folder successfully deleted")
    except FileNotFoundError: 
        print("Folder not found")
    except PermissionError:
        print("No permission to delete")
    except OSError as e:
        print(f"Error: {e}")


