# # from TTS.api import TTS
import initialize

print(initialize.locations)
print(initialize.locations["diaLocation"])

import os
import shutil
import sys
sys.path.append(initialize.locations["diaLocation"]);
from dia.model import Dia 
import torch

device = "cuda" if torch.cuda.is_available() else "cpu"
model = Dia.from_pretrained("nari-labs/Dia-1.6B-0626", device="cpu")


def generateAudioFiles(text, fileName, type):
    outputPath = f"{initialize.locations['mp3Location']}/{type}/{fileName}.wav"
    os.makedirs(f"{initialize.locations['mp3Location']}/{type}", exist_ok=True)

    audio = model.generate(text) 
    if len(audio.shape) == 1:
        audio = audio.reshape(-1, 1)

    model.save_audio(audio, outputPath)
    print(fileName, " audio created.");

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


