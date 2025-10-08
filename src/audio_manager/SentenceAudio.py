import initialize
from audio_manager.Audio import Audio
import os
import shutil
from audio_manager.AudioTTS import tts 



class SentenceAudio(Audio):

    def generateAudioFile(self, text):

        fileName = text.replace(" ","_") 
        audioPath = f"{initialize.locations['mp3Location']}/sentence/{fileName}.mp3"
        os.makedirs(f"{initialize.locations['mp3Location']}/sentence", exist_ok=True)

        text += "."
        tts.tts_to_file(text=text, file_path=audioPath, speed=0.2)
        print("Successfully create sentence model.");


    def deleteAudioFile(self):
        try:
            shutil.rmtree(f"{initialize.locations['mp3Location']}/sentence")
            print(f"Sentence folder successfully deleted")
        except FileNotFoundError: 
            print(f"Sentence folder not found")
        except PermissionError:
            print("No permission to delete")
        except OSError as e:
            print(f"Sentence folder OS error: {e}")


    def regenerateAudioFile(self, fileName):
        audioPath = f"{initialize.locations['mp3Location']}/sentence/{fileName}.mp3" 

        if(not audioPath):
            print("audio file not found")
            return;

        os.remove(audioPath)
        text = fileName.replace("_"," ")
        self.generateAudioFile(text);

