from db.SentenceDb import SentenceDb
from db.WordDb import WordDb
from db.LetterDb import LetterDb


class DbFactory:

    @staticmethod
    def createDbStrategy(strategyType: str):
        if strategyType == "sentence":
            return SentenceDb();
        elif strategyType == "word":
            return WordDb();
        elif strategyType == "letter":
            return LetterDb();
        else:
            raise ValueError("Unknown automation type.")









