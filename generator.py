# Responsible for generating realistic player characters

from random import *
from playercharacter import PlayerCharacter
from enums import *
from custom_types import *
from dice import rollxdy
from copy import deepcopy

# character class responsible for generating a random character


class CharacterRandom(PlayerCharacter):
    def __init__(self, playerName):
    # 'main' function, generates a random character using helper functions below
    # returns PlayerCharacter
        # class -> race -> sex -> origin -> social class -> name -> diety -> languages -> height -> weight -> hair -> eyes
        # get non-random attributes: level, experience

        # user must input their name to create a PlayerCharacter
        # TODO input from user on player owner
        super().__init__(playerName)

        # assign a random race, remove drow and orc as playable races
        allowableRaces = list(Race)
        allowableRaces.remove(Race.DROW)
        allowableRaces.remove(Race.ORC)
        self.race = choice(allowableRaces)

        # assign a random class
        self.cclassPref = choice(list(ClassPreferences))
        self.cclass = self.cclassPref.name
        
        self.age = CharacterRandom.randomAge(self.race, self.cclassPref)
        self.sex = choice(list(Sex))
        
        heightWeight = CharacterRandom.randomHeightWeight(self.race, self.sex)
        self.height = heightWeight[0]
        self.weight = heightWeight[1]
        
        self.hair = choice(list(Hair))
        self.eyes = choice(list(Eyes))
        self.alignment = choice(list(SpecialAlignments.NON_EVIL.value))
        # assign a random diety
        #self.diety = CharacterRandom.randomDiety(self.cclass, self.race)

        # assign random abilties based off class
        self.abilties = AbilitiesRandom(self.cclassPref)

        

    # TODO
    def randomDiety(cclass, race):
        dietychoice = choice(list(Deities)).value
    
        return dietychoice

    #TODO
    def randomOrigin():
        # return random country from the flanaess
        # interesting implementation: for instance, an orc is MUCH more
        # likely to have been born in the pomarj (percentages do exist for each country....)

        return choice(list(Country)).value

    # determine the age 
    def randomAge(race, cclassPref):
        ageTable = [
            # race, cleric, fighter, magic user, thief
            [Race.DWARF, 250 + rollxdy(20, 2), 40 + rollxdy(4, 5), rollxdy(100, 1) + 35, 75 + rollxdy(6, 3)],
            [Race.ELF, 500 + rollxdy(10, 10), 130 + rollxdy(6, 5), 150 + rollxdy(6, 5), 100 + rollxdy(6, 5)],
            [Race.GNOME, 300 + rollxdy(12, 3), 60 + rollxdy(4, 5), 100 + rollxdy(12, 2), 80 + rollxdy(4, 5)],
            [Race.HALF_ELF, 40 + rollxdy(4, 2), 22 + rollxdy(4, 3), 30 + rollxdy(8, 2), 22 + rollxdy(8, 3)],
            [Race.HALFLING, rollxdy(100, 1) + 35, 20 + rollxdy(4, 3), rollxdy(100, 1) + 35, 40 + rollxdy(4, 2)],
            [Race.HALF_ORC, 20 + rollxdy(4, 1), 13 + rollxdy(4, 1), 15 + rollxdy(4, 1), 20 + rollxdy(4, 2)],
            [Race.ORC, 20 + rollxdy(4, 1), 13 + rollxdy(4, 1), 15 + rollxdy(4, 1), 20 + rollxdy(4, 2)],
            [Race.HUMAN, 18 + rollxdy(4, 1), 15 + rollxdy(4, 1), 24 + rollxdy(8, 2), 18 + rollxdy(4, 1)]
        ]
        age = 0
        for i in range(len(ageTable)):
            if(race == ageTable[i][0]):
                if(cclassPref == ClassPreferences.CLERIC or cclassPref == ClassPreferences.DRUID):
                    age = ageTable[i][1]
                    break
                elif(cclassPref == ClassPreferences.FIGHTER or cclassPref == ClassPreferences.PALADIN or cclassPref == ClassPreferences.RANGER or cclassPref == ClassPreferences.MONK):
                    age = ageTable[i][2]
                    break
                elif(cclassPref == ClassPreferences.MAGIC_USER or cclassPref == ClassPreferences.ILLUSIONIST):
                    age = ageTable[i][3]
                    break
                elif(cclassPref== ClassPreferences.THIEF):
                    age = ageTable[i][4]
                    break
                else:
                    age = -1
                    break

        return age
   
    # returns a tuple of (height, weight)
    def randomHeightWeight(race, sex):
        # not TRULY accurate to Table #3 Height and Weight Determination
        HWTableMales = [
            #race, avgHeight +, avgHeight-, avgWeight+, avgWeight-
            [Race.DWARF, 48 + rollxdy(4, 1), 48 - rollxdy(4, 1), 150 + rollxdy(12, 2), 150 - rollxdy(8, 2)],
            [Race.ELF, 60 + rollxdy(4, 1), 60 - rollxdy(6, 1), 100 + rollxdy(20, 1), 100 - rollxdy(10, 1)],
            [Race.GNOME, 42 + rollxdy(3, 1), 42 - rollxdy(3, 1), 80 + rollxdy(6, 2), 80 - rollxdy(4, 2)],
            [Race.HALF_ELF, 66 + rollxdy(6, 1), 66 - rollxdy(6, 1), 130 + rollxdy(20, 1), 130 - rollxdy(20, 1)],
            [Race.HALFLING, 36 + rollxdy(6, 1), 36 - rollxdy(3, 1), 60 + rollxdy(6, 2), 60 - rollxdy(4, 2)],
            [Race.HALF_ORC, 66 + rollxdy(4, 1), 66 - rollxdy(4, 1), 150 + rollxdy(10, 4), 150 - rollxdy(8, 2)],
            [Race.HUMAN, 72 + rollxdy(12, 1), 72 - rollxdy(12, 1), 175 + rollxdy(12, 5), 175 - rollxdy(12, 3)]
        ]
        HWTableFemales = [
            [Race.DWARF, 46 + rollxdy(4, 1), 46 - rollxdy(4, 1), 120 + rollxdy(10, 2), 120 - rollxdy(8, 2)],
            [Race.ELF, 54 + rollxdy(6, 1), 54 - rollxdy(4, 1), 80 + rollxdy(6, 2), 80 - rollxdy(10, 1)],
            [Race.GNOME, 39 + rollxdy(3, 1), 39 - rollxdy(3, 1), 75 + rollxdy(8, 1), 75 - rollxdy(8, 1)],
            [Race.HALF_ELF, 62 + rollxdy(6, 1), 62 - rollxdy(6, 1), 100 + rollxdy(8, 2), 100 - rollxdy(12, 1)],
            [Race.HALFLING, 36 + rollxdy(6, 1), 36 - rollxdy(3, 1), 60 + rollxdy(6, 2), 60 - rollxdy(4, 2)],
            [Race.HALF_ORC, 62 + rollxdy(3, 1), 62 - rollxdy(3, 1), 120 + rollxdy(8, 4), 120 - rollxdy(6, 3)],
            [Race.HUMAN, 66 + rollxdy(8, 1), 66 - rollxdy(6, 1), 130 + rollxdy(12, 4), 130 - rollxdy(10, 3)]
        ]
        height = 0 #inches
        weight = 0 #pounds
        for i in range(len(HWTableMales)):
            if(race == HWTableMales[i][0]):
                if(sex == Sex.MALE):
                    # gets either 1st or 2nd INDEX in table, (for plus or minus determination)
                    height = HWTableMales[i][randint(1, 2)]
                    weight = HWTableMales[i][randint(3, 4)]
                else: #female sex
                    height = HWTableFemales[i][randint(1, 2)]
                    weight = HWTableFemales[i][randint(3, 4)]
                    
                return height, weight
        return height, weight
        
    
# generates a random abilities 'table' for a character
# @character, param of type CharacterRandom required to generate ability scores
# @method, param for [1-4] method options for rolling dice, defaults method 1
class AbilitiesRandom(Abilities):
    def __init__(self, classPref=ClassPreferences.FIGHTER, methodChoice=1):
        super().__init__()
        AbilitiesRandom.assignAbilities(self, classPref)


    def assignAbilities(self, classPref=ClassPreferences.FIGHTER):
        rolls = AbilitiesRandom.method(1)
        preferences = deepcopy(classPref.value) # ensures once classes are instaniated, that a new uninstaniated class is assigned
    
        for i in range(len(preferences)):

            # gets highest of the rolls
            highest = max(rolls)

            # checks if we need to roll for special strength
            if(highest == 18 and preferences[i] == Strength):

                #only rolls for 1d100 special strength if of Fighter or Ranger class
                if(classPref == ClassPreferences.FIGHTER or classPref == ClassPreferences.RANGER):
                    onedonehundred = rollxdy(100, 1)
                    preferences[i] = preferences[i](str(highest)+"/"+str(onedonehundred))
                    continue  
            
            # if valid DEX and class is thief, ensure we assign thiefs table
            if(highest >= 9 and highest <= 18 and classPref == ClassPreferences.THIEF and preferences[i] == Dexterity):
                self.thiefAbilties = ThiefAbilities(str(highest))

            #instansiate for each preference of the class
            preferences[i] = preferences[i](str(highest))

            #remove highest roll
            rolls.remove(highest)

        # iterate through class list(lst is a list of All abilites[STR, INT, etc..])
        for i in range(len(self.lst)):
            #iterate through preferences
            for j in range(len(preferences)):
                #if the classes match, update the list
                if(isinstance(preferences[j], self.lst[i].__class__)):
                    self.lst[i] = preferences[j]

        #updates class members to be consistent with preferences list
        self.ensureList()

        # check for psionics
        AbilitiesRandom.checkPsionics(self)

        # finally assign 

    # checks for psionics
    def checkPsionics(self):
        # check psionics, must be done after as psionic ability depends on WIS, INT, and CHR
        if(int(self.CHR.CHR) >= 16 or int(self.INT.INT) >= 16 or int(self.WIS.WIS) >= 16):
            # determine ability bonuses for psionics based on appendix I of P.H.
            charismaBonus = 0.5*(int(self.CHR.CHR) - 16) if int(self.CHR.CHR) >= 16 else 0
            intelligenceBonus = 2.5*(int(self.INT.INT) - 16) if int(self.INT.INT) >= 16 else 0
            wisdomBonus = 1.5*(int(self.WIS.WIS) - 16) if int(self.WIS.WIS) >= 16 else 0

            # calculate threshold needed for psionic ability to exist
            percentileThreshold = 100 - (charismaBonus + intelligenceBonus + wisdomBonus)
            if(rollxdy(100, 1) >= percentileThreshold):
                # psionic ability exists
                # calculate psionic points
                charismaPsionicPointBonus = (int(self.CHR.CHR) - 12) if int(self.CHR.CHR) > 12 else 0
                intelligencePsionicPointBonus = (int(self.INT.INT) - 12) if int(self.INT.INT) > 12 else 0
                wisdeomPsionicPointBonus = (int(self.WIS.WIS) - 12) if int(self.WIS.WIS) > 12 else 0

                #(5-72), 5 meaning 17 charisma to beat threshold with a 100 roll
                bonuses = charismaPsionicPointBonus + intelligencePsionicPointBonus + wisdeomPsionicPointBonus
                # check if two of the abilities are above 16, resulting in a double of psionic points
                if(int(self.CHR.CHR) > 16 and int(self.INT.INT) > 16 or int(self.CHR.CHR) > 16 and int(self.WIS.WIS) > 16 or int(self.INT.INT) > 16 and int(self.WIS.WIS) > 16):
                    # if all three abilities are greater than 16, quadruple the psionic points
                    if(int(self.CHR.CHR) > 16 and int(self.INT.INT) > 16 and int(self.WIS.WIS) > 16):
                        bonuses *= 4
                    bonuses *= 2
                
                #(5-172)
                psionicStrength = rollxdy(100, 1) + bonuses
                # psionic Ability = double psionic strength, (10-344), half is att, half is def
                psionicAbility = psionicStrength*2
                # to create instance of psionicAbilities, psionicAbility (strength*2) is needed
                # determine attack, defense, and disciplines
                attackRoll = rollxdy(100, 1) 
                defenseRoll = rollxdy(100, 1)
                numAttackModes = 5 if attackRoll >= 96 else 4 if attackRoll >= 76 else 3 if attackRoll >= 51 else 2 if attackRoll >= 26 else 1
                numDefenseModes = 5 if defenseRoll >= 91 else 4 if defenseRoll >= 76 else 3 if defenseRoll >= 26 else 2 
                
                attackModes = []
                defenseModes = []
                listofattackmodes = list(AttackPsionicModes)
                listofdefensemodes = list(DefensePsionicModes)
                for i in range(numAttackModes):
                    c = choice(listofattackmodes)
                    while(c in attackModes):
                        c = choice(listofattackmodes)
                    attackModes.append(c.value)

                for i in range(numDefenseModes):
                    c = choice(listofdefensemodes)
                    while(c in defenseModes):
                        c = choice(listofdefensemodes)
                    defenseModes.append(c.value)

                # specific modes for attack and defense are to be determined by the player, this program will simply select randomly

                self.psionicAbilties = psionicAbilities(psionicAbility, attackModes, defenseModes, [])

    # roll 4d6, drop lowest roll
    def method(methodChoice):
        if(methodChoice == 1):
            rolls = [0,0,0,0,0,0,0]
            for i in range(len(rolls)):
                rolls[i] = AbilitiesRandom.roll_4d6_drop_lowest()
        return rolls

    # rolls 4d6, drops the lowest, returns the sum
    def roll_4d6_drop_lowest(): 
        rolls = [0, 0, 0, 0]
        # assign random numbers [1-6] inclusive to the indexes
        for i in range(len(rolls)):
            rolls[i] = randint(1, 6)
        # find the lowest roll in the list 
        lowest = rolls[0]
        for i in range(len(rolls)):
            if(rolls[i] < lowest):
                lowest = rolls[i]
        # remove the lowest
        rolls.remove(lowest)
        return sum(rolls)