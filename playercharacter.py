# Player Character class

from enums import *
from custom_types import *

class PlayerCharacter:
    def __init__(self, playerName):
        self.playerName = playerName
        self.characterName = "[undefined name]"
        self.race = Race.HUMAN
        self.cclass = Class.FIGHTER
        self.level = 1
        self.alignment = Alignment.TRUE_NEUTRAL
        self.experience = 0
        self.origin = "[undefined origin]"
        self.socialClass = "[undefined social class]"
        self.patron = "[undefined patron]"
        self.affiliation = "[undefined affiliation]"
        self.diety = "[undefined diety]"
        self.height = 0
        self.weight = 0
        self.age = 0
        self.sex = Sex.MALE
        self.hair = Hair.BLONDE
        self.eyes = Eyes.BLACK
        self.languages = [Languages.COMMON]
        self.abilties = Abilities()
        self.spells = None

    def __str__(self):
        return f"""
Player Owner:       {self.playerName}
    Name:           {self.characterName}
    Race:           {self.race.value}
    Class:          {self.cclass}
    Level:          {self.level}
    Alignment:      {self.alignment.value}
    Experience:     {self.experience}
    Origin:         {self.origin}
    Social Class:   {self.socialClass}
    Patron:         {self.patron}
    Affiliation:    {self.affiliation}
    Diety:          {self.diety}
    Height:         {self.height//12}'{self.height%12}"
    Weight:         {self.weight}lbs
    Age:            {self.age}
    Sex:            {self.sex.value}
    Hair:           {self.hair.value}
    Eyes:           {self.eyes.value}
    Languages:      {PlayerCharacter.langToString(self)}
    Abilities:{self.abilties}   
        """

    # returns a string of the self.languages member    
    def langToString(self):
        languages = ""
        for i in range(len(self.languages)):
            languages += self.languages[i].value + ", "
        # remove last comma
        return languages[:len(languages)-2] 