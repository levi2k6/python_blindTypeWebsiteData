from TTS.api import TTS

import initialize

import os
import json

tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=True, gpu=False)

def generateAudioFile(text, fileName):

    audioPath = os.path.expanduser(f"{initialize.locations['mp3Location']}/{fileName}.mp3")
    os.makedirs(os.path.dirname(initialize.locations['mp3Location']), exist_ok=True)
    tts.tts_to_file(text=text, file_path=audioPath, speed=0.2)

