#boarProject v2.0
#------Standard Chances:-----
    #Hit Chance:
        #(skill level)*(player level)=attackSucsessfulChance
        #(difficulty level)*(player level)=

#-----Imports:----
import random
import time

#-----Itmes:-----
items={
	"2) Rawhide Armor": "Rough form of protection, stitched together.(+5 protection)",
	"1) Leather Satchel": "An old, raggedy sack that carries the few things you have.",
	"3) Quiver": "An old quiver you father used, there is a family seal on it's front."
}

#-----Random Temporary Variables:-----

#-----Mob Info:-----
boar1Dead=False

#-----Character Info:-----
name=""
alive=True
inventory={"Rawhide Armor"
           "Quiver"
           "Leather Satchel"
}

#-----Leveling Info:-----
level=1
totalExperience=0
    #Skill Specific Levels:
rangedWeapons=1
shortSwordsDaggers=1
evasionSkill=1
Stealthskill=1
total skill level=(rangedWeapons + shortSwordsDaggers + evasionSkill + stealthSkill)/4
