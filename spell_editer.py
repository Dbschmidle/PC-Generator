SPELLS_FILE = open("spells.txt", "r", encoding="ascii", errors="ignore")
PY_FILE = open("spells_new.txt", "w")

SPELLS = SPELLS_FILE.readlines()

SPELLS_FILE.close()

spell_tracker = []

for i in range(len(SPELLS)):
    if(SPELLS[i].find("(") != -1 and SPELLS[i].startswith("Explanation") == False and SPELLS[i+1].startswith("Level") == True):
        uppercase_name = SPELLS[i][:SPELLS[i].find("(")-1].upper().replace(" ", "_")
        spell_attributes = SPELLS[i+1]
        level = spell_attributes[7:8]
        range = "\""+spell_attributes[spell_attributes.find("Range: ")+7:spell_attributes.find("Casting")].strip().replace("\"", "\\\"")+"\""
        casting_time = "\""+spell_attributes[spell_attributes.find("Casting Time: ")+14:spell_attributes.find("Duration")].strip().replace("\"", "\\\"")+"\""
        duration = "\""+spell_attributes[spell_attributes.find("Duration: ")+10:spell_attributes.find("Saving Throw")].strip().replace("\"", "\\\"")+"\""
        saving_throw = "\""+spell_attributes[spell_attributes.find("Saving Throw: ")+14:spell_attributes.find("Area of Effect")].strip().replace("\"", "\\\"")+"\""
        area_of_effect =  "\""+spell_attributes[spell_attributes.find("Area of Effect: "):spell_attributes.find("\n")].strip().replace("\"", "\\\"")+"\""
        description = "\""+SPELLS[i+2].strip("\n").replace("\"", "\\\"")+"\""
        
        if(uppercase_name in spell_tracker):
            uppercase_name = "#"+uppercase_name
        spell_tracker.append(uppercase_name)
        
        uppercase_name = uppercase_name.replace("&", "AND")
        uppercase_name = uppercase_name.replace("'", "")
        uppercase_name = uppercase_name.replace(",", "")
        uppercase_name = uppercase_name.replace("-", "_")
        py_line = uppercase_name+" = Spell(\""+SPELLS[i].strip("\n")+"\",level="+ level+",range="+range+",castingTime="+casting_time+",duration="+duration+", savingThrow="+saving_throw+", areaOfEffect="+area_of_effect+",description="+description+")\n    "
        
        PY_FILE.write(py_line)


PY_FILE.close()