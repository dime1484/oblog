from colorama import init, Fore, Back, Style
from sys import exit

class Log:
    def __init__(self, **kwargs):
        init()
        self.note_allowed = kwargs.get("NOTIFS")
        self.msg_allowed = kwargs.get("MESSAGE")
        self.warn_allowed = kwargs.get("WARNINGS")
        self.crit_allowed = kwargs.get("CRITICAL")
        self.fat_allowed = kwargs.get("FATAL")
        self.name = kwargs.get("SCRIPT")

    def note(self, content):
        if self.note_allowed:
            print(Fore.CYAN, "Note!", content, Style.RESET_ALL)

    def message(self, content):
        if self.msg_allowed:
            print(Fore.GREEN, "Message!", content, Style.RESET_ALL)
    
    def warning(self, content):
        if self.warn_allowed:
            print(Fore.YELLOW, "Warning!", Style.RESET_ALL, f"In:{self.name}", Fore.YELLOW, content, Style.RESET_ALL)
    
    def critical(self, content):
        if self.crit_allowed:
            print(Fore.RED, "Critical!", Style.RESET_ALL, f"In:{self.name}", Fore.RED, content, Style.RESET_ALL)

    def fatal(self, content):
        if self.fat_allowed:
            print(Back.YELLOW, Fore.BLACK, "Fatal-->", Style.RESET_ALL, f"In:{self.name}", Back.YELLOW, Fore.BLACK, content, Style.RESET_ALL)
            exit()

logger = Log(NOTIFS=True, MESSAGE=True, WARNINGS=True, CRITICAL=True, FATAL=True, SCRIPT="'Test script'")
logger.note("This is a development note")
logger.message("This is a message for the user!")
logger.warning("This is a non-critical warning!")
logger.critical("Something bad happened! This is a critical warning!")
logger.fatal("Something very bad happened, after this fatal note the program will stop!")
