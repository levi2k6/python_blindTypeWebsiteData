from TTS.api import TTS

import initialize

import os
import json

tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=True, gpu=False)

def generateAudioFile(text, path):

    os.makedirs(os.path.dirname(path), exist_ok=True)
    tts.tts_to_file(text=text, file_path=path, speed=0.2)

