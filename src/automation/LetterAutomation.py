import initialize
from ChallengeStrategy import ChallengeStrategy
import dataManager
import AudioManager

class LetterAutomation(ChallengeStrategy):

    def addAllChallengeDb(self):
        for datum in initialize.sentenceJson:
            if dataManager.getData(datum, type):
                print("Challenge already existed.")
                return

            dataManager.postData(datum, "sentence");
            print("Sentence table has been successfully added data into it.")
        pass


    def deleteAllChallengeDb(self):
        if not dataManager.isTableEmpty("sentence"):
            dataManager.deleteData("sentence");
        AudioManager.deleteGeneratedAudioFiles("sentence");
        pass



