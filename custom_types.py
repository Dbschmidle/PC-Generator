class Diety:
    def __init__(self, fullName, race, cclasses, worshipper_alignments):
        self.fullName = fullName
        self.race = race
        self.cclasses = cclasses
        self.worshipper_alignments = worshipper_alignments

    def __str__(self):
        return f"{self.fullName} {self.race}"

class Spell:
    def __init__(self, name, level=0, range="0\"", duration="0", areaOfEffect = "0", components=[], castingTime = "0", savingThrow = "", description=""):
        self.name = name
        self.level = level
        self.range = range
        self.duration = duration
        self.areaOfEffect = areaOfEffect
        self.components = components
        self.castingTime = castingTime
        self.savingThrow = savingThrow
        self.description = description

    def __str__(self):
        return f"{self.name}"

    def getLevel(self):
        return self.level

class PsionicMode:
    # attack range only applicable to attack spells, area protected only applicable to defense spells
    def __init__(self, name, pointCost, attackRange="N/A", areaProtected="N/A"):
        self.name = name
        self.pointCost = pointCost
        self.attackRange = attackRange
        self.areaProtected = areaProtected
    def __str__(self):
        return f"{self.name}"

class Abilities:

    def __init__(self, STR="0", INT="0", WIS="0", DEX="0", CON="0", CHR="0", COM="0"):
        self.STR = Strength(STR)
        self.INT = Intelligence(INT)
        self.WIS = Wisdom(WIS)
        self.DEX = Dexterity(DEX)
        self.CON = Constitution(CON)
        self.CHR = Charisma(CHR)
        self.COM = Comeliness(COM)
        self.thiefAbilties = None #not initalized unless thief or maybe monk
        self.psionicAbilties = None
        self.lst = [self.STR, self.INT, self.WIS, self.DEX, self.CON, self.CHR, self.COM, self.thiefAbilties, self.psionicAbilties]

    def __str__(self):
        #TODO
        return f"""
        {str(self.STR)}
        {str(self.INT)}
        {str(self.WIS)}
        {str(self.DEX)}
        {str(self.CON)}
        {str(self.CHR)}
        {str(self.COM)}
        Thief Abiltiies: {str(self.thiefAbilties)}
        Psionic Abilities: {str(self.psionicAbilties)}
        """

    def ensureList(self):
        # ensures the data of self.lst is equal to the class members of Abilities
        self.STR = self.lst[0]
        self.INT = self.lst[1]
        self.WIS = self.lst[2]
        self.DEX = self.lst[3]
        self.CON = self.lst[4]
        self.CHR = self.lst[5]
        self.COM = self.lst[6]

class Strength:
    # based on Strength Table II: Ability Adjustments (P.H.)
    strengthTable = [
        #str, toHit, dmgAdj, wgtAllow, openDoors, brs/gates
        ["3", "-3", "-1", "-350", "1", "0%"],
        ["4", "-2", "-1", "-250", "1", "0%"],
        ["5", "-2", "-1", "-250", "1", "0%"],
        ["6", "-1","0", "-150", "1", "0%"],
        ["7", "-1","0", "-150", "1", "0%"],
        ["8", "0", "0", "0", "1-2", "1%"],
        ["9", "0", "0", "0", "1-2", "1%"],
        ["10", "0", "0", "0", "1-2", "2%"],
        ["11", "0", "0", "0", "1-2", "2%"],
        ["12", "0", "0", "+100", "1-2", "4%"],
        ["13", "0", "0", "+100", "1-2", "4%"],
        ["14", "0", "0", "+200", "1-2", "7%"],
        ["15", "0", "0", "+200", "1-2", "7%"],
        ["16", "0", "+1", "+350", "1-3", "10%"],
        ["17", "+1", "+1", "+500", "1-3", "13%"],
        ["18", "+1", "+2", "+750", "1-3", "16%"],
        ["18/50", "+1", "+3", "+1000", "1-3", "20%"],
        ["18/75", "+2", "+3", "+1250", "1-4", "25%"],
        ["18/90", "+2", "+4", "+1500", "1-4", "30%"],
        ["18/99", "+2", "+5", "+2000", "1-4(1)", "35%"],
        ["18/100", "+3", "+6", "+3000", "1-5(2)", "40%"]
    ]
    default = ["", "", "", "", "", ""]
    def __init__(self, STR="0"):
        for i in range(len(Strength.strengthTable)):
            #TODO: cases where 18 strength

            #int representation of the first col in strengthTable
            strengthValue = int(Strength.strengthTable[i][0]) if len(Strength.strengthTable[i][0]) <= 2 else int(Strength.strengthTable[i][0][:2])

            #int representation of STR parameter
            STRvalue = int(STR) if len(STR) <= 2 else int(STR[:2])

            #if representation == STR representation
            if(strengthValue == STRvalue):
                if(STR[:2] == "18"):
                    eightteenSecondValue = int(STR[3:]) if len(STR) > 2 else 0          
                    currSecondValue = int(Strength.strengthTable[i][0][3:]) if len(Strength.strengthTable[i][0]) > 2 else -1
                    #print(str(eightteenSecondValue) +" <= " +str(currSecondValue))
                    if(eightteenSecondValue <= currSecondValue):
                        self.STR = STR
                        self.toHit = Strength.strengthTable[i][1]
                        self.damageAdjustment = Strength.strengthTable[i][2]
                        self.weightAllowance = Strength.strengthTable[i][3]
                        self.openDoors = Strength.strengthTable[i][4]
                        self.barsGates = Strength.strengthTable[i][5]
                        return
                    else:
                        continue

                self.STR = STR
                self.toHit = Strength.strengthTable[i][1]
                self.damageAdjustment = Strength.strengthTable[i][2]
                self.weightAllowance = Strength.strengthTable[i][3]
                self.openDoors = Strength.strengthTable[i][4]
                self.barsGates = Strength.strengthTable[i][5]
                return
    
        # case: never found a match, use default table
        self.STR = STR
        self.toHit = Strength.default[1]
        self.damageAdjustment = Strength.default[2]
        self.weightAllowance = Strength.default[3]
        self.openDoors = Strength.default[4]
        self.barsGates = Strength.default[5]
    
    def __str__(self):
        return f"STR[{self.STR}] +/-To Hit[{self.toHit}] +/- Damage Adj[{self.damageAdjustment}] +/- W[{self.weightAllowance}] Open-Doors[{self.openDoors}] Bars/Gates[{self.barsGates}]"

    def abilType(self):
        return f"STR"

class Intelligence:
    # based Intelligence Table II (P.H.)
    intelligenceTable = [
        #ability, chance to know spell, min spells/level, max spells/level
        ["9","35%","4","6"],
        ["10","45%","5","7"],
        ["11","45%","5","7"],
        ["12","45%","5","7"],
        ["13","55%","6","9"],
        ["14","55%","6","9"],
        ["15","65%","7","11"],
        ["16","65%","7","11"],
        ["17","75%","8","14"],
        ["18","85%","9","18"],
        ["19","95%","10","all"]
    ]
    nonMagicUser = ["anyOther","N/A","N/A","N/A"]
    
    def __init__(self, INT = "0"):
        try:
            INTvalue = int(INT)
        except:
            raise ValueError(f"INT must be of type string, [3-19] inclusive")
        if(INTvalue >= 18):
            self.numLanguages = 7
        elif(INTvalue >= 17):
            self.numLanguages = 6
        elif(INTvalue >= 16):
            self.numLanguages = 5
        elif(INTvalue >= 14):
            self.numLanguages = 4
        elif(INTvalue >= 10):
            self.numLanguages = 2
        elif(INTvalue >= 8):
            self.numLanguages = 1
        else:
                self.numLanguages = 0
        for row in Intelligence.intelligenceTable:
            if(INT == row[0]):
                self.INT = INT
                self.perToKnowSpell = row[1]
                self.minSpellPerLevel = row[2]
                self.maxSpellPerLevel = row[3]
                return
        self.INT = INT
        self.perToKnowSpell = Intelligence.nonMagicUser[1]
        self.minSpellPerLevel = Intelligence.nonMagicUser[2]
        self.maxSpellPerLevel = Intelligence.nonMagicUser[3]

    def __str__(self):
        return f"INT[{self.INT}] Add.Lang [{self.numLanguages}] %toKnow Spell[{self.perToKnowSpell}] Min Spell/Level[{self.minSpellPerLevel}] Max Spell/Level[{self.maxSpellPerLevel}]"

class Wisdom:
    clericalAdjustment = [
        #leve, spell bonus, chance of spell failure
        ["9", "none", "20%"],
        ["10", "none", "15%"],
        ["11", "none", "10%"],
        ["12", "none", "5%"],
        ["13", "One 1st level", "0%"],
        ["14", "One 1st level", "0%"],
        ["15", "One 2nd level", "0%"],
        ["16", "One 2nd level", "0%"],
        ["17", "One 3rd level", "0%"],
        ["18", "One 4th level", "0%"]
    ]
    def __init__(self, WIS="0"):
        try:
            WISvalue = int(WIS)
        except:
            raise ValueError(f"WIS must be of type string, [3-19] inclusive")
        if(WISvalue >= 18):
            self.magicAttackAdj = "+4"
        elif(WISvalue >= 17):
            self.magicAttackAdj = "+3"
        elif(WISvalue >= 16):
            self.magicAttackAdj = "+2"
        elif(WISvalue >= 15):
            self.magicAttackAdj = "+1"
        elif(WISvalue >= 8):
            self.magicAttackAdj = "none"
        elif(WISvalue >= 5):
            self.magicAttackAdj = "-1"
        elif(WISvalue >= 4):
            self.magicAttackAdj = "-2"
        elif(WISvalue >= 3):
            self.magicAttackAdj = "-1"
        else:
            self.magicAttackAdj = "unknown"

        for row in Wisdom.clericalAdjustment:
            if(WIS == row[0]):
                self.WIS = WIS
                self.spellBonus = row[1]
                self.chanceOfSpellFailure = row[2]
                return
        self.WIS = WIS
        self.spellBonus = row[1]
        self.chanceOfSpellFailure = row[2]
    def __str__(self):
        return f"WIS[{self.WIS}] Magic Att. Adj[{self.magicAttackAdj}] Prayer Bonus[{self.spellBonus}] % Spell failure[{self.chanceOfSpellFailure}]"

class Dexterity:
    # does not handle, thief abilities, see thiefAbilities class
    def __init__(self, DEX="0"):
        try:
            DEXvalue = int(DEX)
        except:
            raise ValueError(f"DEX must be of type string, [3-19] inclusive")
        if(DEXvalue >= 18):
            self.reactionAdj = "+3"
            self.armorClassAdj = "-4"
        elif(DEXvalue >= 17):
            self.reactionAdj = "+2"
            self.armorClassAdj = "-3"        
        elif(DEXvalue >= 16):
            self.reactionAdj = "+1"
            self.armorClassAdj = "-2"
        elif(DEXvalue >= 15):
            self.reactionAdj = "0"
            self.armorClassAdj = "-1"
        elif(DEXvalue >= 7):
            self.reactionAdj = "0"
            self.armorClassAdj = "0"      
        elif(DEXvalue >= 6):
            self.reactionAdj = "0"
            self.armorClassAdj = "+1"                 
        elif(DEXvalue >= 5):
            self.reactionAdj = "-1"
            self.armorClassAdj = "+2"     
        elif(DEXvalue >= 4):
            self.reactionAdj = "-2"
            self.armorClassAdj = "+3"     
        else:
            self.reactionAdj = "-3"
            self.armorClassAdj = "+4"
        self.DEX = DEX            

    def __str__(self):
        return f"DEX[{self.DEX}] Reaction & Missle Adj[{self.reactionAdj}] AC Adj[{self.armorClassAdj}]"

class Constitution:
    constitutionTable = [
        #ability score, HP adj, system shock survival, resurection survival
        ["3", "-2", "35%", "40%"],
        ["4", "-1", "40%", "45%"],
        ["5", "-1", "45%", "50%"],
        ["6", "-1", "50%", "55%"],
        ["7", "0", "55%", "60%"],
        ["8", "0", "60%", "65%"],
        ["9", "0", "65%", "70%"],
        ["10", "0", "70%", "75%"],
        ["11", "0", "75%", "80%"],
        ["12", "0", "80%", "85%"],
        ["13", "0", "85%", "90%"],
        ["14", "0", "88%", "92%"],
        ["15", "+1", "91%", "94%"],
        ["16", "+2", "95%", "96%"],
        ["17", "+2(+3)*", "97%", "98%"],
        ["18", "+2(+4)*", "99%", "100%"]

    ]
    constitutionTableAsterisk = "Bonus Applies only to fighters; all other classes may be given a maxiumum hit point bonus adjustment for constituion of +2"
    defaultConstitutionTable = ["0", "0", "0", "0"]

    def __init__(self, CON="0"):
        try:
            CONvalue = int(CON)
        except:
            raise ValueError(f"CON must be of type string, [3-19] inclusive")
        for row in Constitution.constitutionTable:
            if(CON == row[0]):
                self.CON = CON
                self.hitPointAdj = row[1]
                self.sysShockSurvival = row[2]
                self.resurectionSurvival = row[3]
                return
        self.CON = CON
        self.hitPointAdj = Constitution.defaultConstitutionTable[1]
        self.sysShockSurvival = Constitution.defaultConstitutionTable[2]
        self.resurectionSurvival = Constitution.defaultConstitutionTable[3]

    def __str__(self):
        return f"CON[{self.CON}] HP Adj/level[{self.hitPointAdj}] Shock[{self.sysShockSurvival}] Resur[{self.resurectionSurvival}]"

class Charisma:
    charismaTable = [
        #ability score, max no. of henchmen, "loyalty base", "reaction adj"
        ["3", "1", "-30%", "-25%"],
        ["4", "1", "-25%", "-20%"],
        ["5", "2", "-20%", "-15%"],
        ["6", "2", "-15%", "-10%"],
        ["7", "3", "-10%", "-5%"],
        ["8", "3", "-5%", "normal"],
        ["9", "4", "normal", "normal"],
        ["10", "4", "normal", "normal"],
        ["11", "4", "normal", "normal"],
        ["12", "5", "normal", "normal"],
        ["13", "5", "normal", "+5%"],
        ["14", "6", "+5%", "+10%"],
        ["15", "7", "+15%", "+15%"],
        ["16", "8", "+20%", "+25%"],
        ["17", "10", "+30%", "+30%"],
        ["18", "15", "+40%", "+35%"]
    ]
    defaultCharismaTable = ["0", "0", "0", "0"]
    def __init__(self, CHR="0"):
        try:
            CHRvalue = int(CHR)
        except:
            raise ValueError(f"CHR must be of type string, [3-19] inclusive")
        for row in Charisma.charismaTable:
            if(CHR == row[0]):
                self.CHR = CHR
                self.henchmen = row[1]
                self.loyaltyBase = row[2]
                self.reactionAdj = row[3]
                return
        self.CHR = CHR
        self.henchmen = Charisma.defaultCharismaTable[1]
        self.loyaltyBase = Charisma.defaultCharismaTable[2]
        self.reactionAdj = Charisma.defaultCharismaTable[3]
    def __str__(self):
        return f"CHR[{self.CHR}] Max # Henchmen[{self.henchmen}] Loyalty Base[{self.loyaltyBase}] Reaction Adj[{self.reactionAdj}]"

class Comeliness:
    def __init__(self, COM = "0"):
        try:
            COMvalue = int(COM)
        except:
            raise ValueError(f"COM must be of type string, [3-19] inclusive")
        self.COM = COM

    def __str__(self):
        #TODO find out what these tables are
        return f"COM[{self.COM}] Description[] Reaction[]"

class ThiefAbilities:
    thievesAdjustment = [
        #abiility score, picking pockets, opening locks, locating/removing traps, moving silently, hiding in shadows
        ["9", -15, -10, -10, -20, -10],
        ["10", -10, -5, -10, -15, -5],
        ["11", -5, 0, -5, -10, 0],
        ["12", 0, 0, 0, -5, 0],
        ["13", 0, 0, 0, 0, 0],
        ["14", 0, 0, 0, 0, 0],
        ["15", 0, 0, 0, 0, 0],
        ["16", 0, 5, 0, 0, 0],
        ["17", 5, 10, 0, 5, 5],
        ["18", 10, 15, 5, 10, 10]

    ]
    levelOneThiefAbiltiies = [30, 25, 20, 15, 10, 10, 85, 0]
    # should only be initialized if the class is a thief, handled in generator
    def __init__(self, DEX="0"): 
        for row in ThiefAbilities.thievesAdjustment:
            if(DEX == row[0]):
                self.DEX = DEX
                self.pickingPockets = str(ThiefAbilities.levelOneThiefAbiltiies[0] + row[1])+"%"
                self.openingLocks = str(ThiefAbilities.levelOneThiefAbiltiies[1] + row[2])+"%"
                self.locateRemoveTraps = str(ThiefAbilities.levelOneThiefAbiltiies[2] + row[3])+"%"
                self.moveSilently = str(ThiefAbilities.levelOneThiefAbiltiies[3] + row[4])+"%"
                self.hideShadows = str(ThiefAbilities.levelOneThiefAbiltiies[4] + row[5])+"%"
                self.hearNoise = str(ThiefAbilities.levelOneThiefAbiltiies[5])+"%"
                self.climbWalls = str(ThiefAbilities.levelOneThiefAbiltiies[6])+"%"
                self.readLanguages = str(ThiefAbilities.levelOneThiefAbiltiies[7])+"%"
                return

    def __str__(self):
        return f"""
            Picking Pockets[{self.pickingPockets}] 
            Open Locks[{self.openingLocks}] 
            Find/Remove Traps[{self.locateRemoveTraps}] 
            Move Silently[{self.moveSilently}] 
            Hide In Shadows[{self.hideShadows}]
            Hear Nosie[{self.hearNoise}]
            Climb Walls[{self.climbWalls}]
            Read Languages[{self.readLanguages}]
        """

class psionicAbilities:
    def __init__(self, psionicAbility, attackModes, defenseModes, disciplines):
        self.psionicAbility = psionicAbility
        self.psionicStrength = psionicAbility/2
        self.attackModes = attackModes
        self.defenseModes = defenseModes
        self.disciplines = disciplines

    def __str__(self):
        attackModesStr = ""
        defenseModesStr = ""
        for i in range(len(self.attackModes)):
            attackModesStr += str(self.attackModes[i])+", "

        for i in range(len(self.defenseModes)):
            defenseModesStr += str(self.defenseModes[i])+", "

        return f"""
            [{self.psionicStrength}/{self.psionicStrength}]
            Attack Modes: {attackModesStr[:len(attackModesStr)-2]}
            Defense Modes: {defenseModesStr[:len(defenseModesStr)-2]}
            Disciplines: {str(self.disciplines)}
        """
        
class Traits:
    # D.M.S guide page 100
    def __init__(self):
        return