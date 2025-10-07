from audio_manager.SentenceAudio import SentenceAudio
from audio_manager.WordAudio import WordAudio 
from audio_manager.LetterAudio import LetterAudio 


class AudioFactory:

    @staticmethod
    def createAudioStrategy(strategyName: str):
        if strategyName == "sentence":
            return SentenceAudio();
        if strategyName == "word":
            return WordAudio();
        if strategyName == "letter":
            return LetterAudio();


     



