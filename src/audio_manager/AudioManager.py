from TTS.api import TTS

from audio_manager.AudioFactory import AudioFactory
from audio_manager.Audio import Audio
from typing import Optional 


class AudioManager:

    def __init__(self):
        self.currentAudio: Optional[Audio] = None  

    def setCurrentAudioFile(self, strategyName: str):
        self.currentAudio = AudioFactory.createAudioStrategy(strategyName)

    def generateAudioFile(self, text: str):
        if(not self.currentAudio):
            return;
        self.currentAudio.generateAudioFile(text);

    def deleteAudioFile(self):
        if(not self.currentAudio):
            return;
        self.currentAudio.deleteAudioFile();

    def regenerateAudioFile(self, fileName: str): 
        if(not self.currentAudio):
            return;
        self.currentAudio.regenerateAudioFile(fileName);

