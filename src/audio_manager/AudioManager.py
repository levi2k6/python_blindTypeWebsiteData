from TTS.api import TTS

import initialize
from audio_manager.Audio import Audio
from typing import Optional 


class AudioManager:

    currentAudio: Optional[Audio] = None  

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



