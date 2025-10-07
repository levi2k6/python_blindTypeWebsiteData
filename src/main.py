
from automation.AutomationContext import AutomationContext
from automation.AutomationFactory import AutomationFactory
from db.DbManager import DbManager
import initialize
from audio_manager.AudioManager import AudioManager

from input.InputCommand import InputCommand


def main():
    dbManager = DbManager()
    audioManager = AudioManager()
    automationFactory = AutomationFactory(audioManager, dbManager)

    audioManager = AudioManager()
    automationContext =  AutomationContext(automationFactory, audioManager)
    inputCommand = InputCommand(automationContext)

    inputCommand.makeInput();

main()

