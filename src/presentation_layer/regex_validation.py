import re
from enum import Enum
import sys


class RegexValidation(Enum):
    EMAIL = "([\w.-]+)@([\w.-]+\.[a-zA-Z]{2,})"
    NAME = ".{2,}"
    YEAR = "freshman|sophomore|junior|senior"
    
    def validate_input(input: str, regex:str) -> bool:
        if re.fullmatch(regex, input):
            return True
        return False
        #Temporary solution that physically prevents invalid data from being interacting with the database by forcing termination.
        #Permanent solution would be implementing a while-not loop on every string input