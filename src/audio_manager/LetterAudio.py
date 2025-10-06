from TTS.api import TTS
from audio_manager.AudioManager import generateAudioFiles
import initialize
from audio_manager.Audio import Audio
import os
import shutil


class LetterAudio(Audio):
    tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC_ph", progress_bar=True, gpu=False)

    def generateAudioFile(self, text):

        fileName = text.replace(" ","_") 
        audioPath = f"{initialize.locations['mp3Location']}/{"letter"}/{fileName}.mp3"
        os.makedirs(f"{initialize.locations['mp3Location']}/{"letter"}", exist_ok=True)

        self.tts.tts_to_file(text=text, file_path=audioPath, speed=0.2)
        print("Successfully create sentence model.");


    def deleteAudioFiles(self):
        try:
            shutil.rmtree(f"{initialize.locations['mp3Location']}/letter")
            print(f"Letter folder successfully deleted")
        except FileNotFoundError: 
            print(f"Letter folder not found")
        except PermissionError:
            print("No permission to delete")
        except OSError as e:
            print(f"Letter folder OS error: {e}")


    def regenerateAudioFile(self, fileName):
        audioPath = f"{initialize.locations['mp3Location']}/{"letter"}/{fileName}.mp3" 

        if(not audioPath):
            print("audio file not found")
            return;

        os.remove(audioPath)
        text = fileName.replace("_"," ")
        self.generateAudioFile(text);

