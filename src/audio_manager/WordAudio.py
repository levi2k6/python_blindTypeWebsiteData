from TTS.api import TTS
import initialize
from audio_manager.Audio import Audio
import os
import shutil
from audio_manager.AudioTTS import tts 

class WordAudio(Audio):

    def generateAudioFile(self, text):

        fileName = text.replace(" ","_") 
        audioPath = f"{initialize.locations['mp3Location']}/word/{fileName}.mp3"
        os.makedirs(f"{initialize.locations['mp3Location']}/word", exist_ok=True)

        text += "."
        tts.tts_to_file(text=text, file_path=audioPath, speed=0.1)
        print("Successfully create sentence model.");


    def deleteAudioFile(self):
        try:
            shutil.rmtree(f"{initialize.locations['mp3Location']}/word")
            print(f"Word folder successfully deleted")
        except FileNotFoundError: 
            print(f"Word folder not found")
        except PermissionError:
            print("No permission to delete")
        except OSError as e:
            print(f"Word folder OS error: {e}")


    def regenerateAudioFile(self, fileName):
        audioPath = f"{initialize.locations['mp3Location']}/word/{fileName}.mp3" 

        if(not audioPath):
            print("audio file not found")
            return;

        os.remove(audioPath)
        text = fileName.replace("_"," ")
        self.generateAudioFile(text);

