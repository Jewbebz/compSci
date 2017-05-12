#boarProject v2.0
#------Standard Chances:-----
    #Hit Chance:
        #(skill level)*(player level)=attackSucsessfulChance
        #(difficulty level)*(player level)=

#-----Imports:----
import random
import time

#-----Itmes:-----
Items={
	"2) Rawhide Armor": "Rough form of protection, stitched together.(+5 protection)",
	"1) Leather Satchel": "An old, raggedy sack that carries the few things you have.",
	"3) Quiver": "An old quiver you father used, there is a family seal on it's front."
}

#-----Random Temporary Variables:-----

#-----Mob Info:-----
Boar1Dead=False

#-----Mob Interaction System:-----
def choose(op1, op2, op3, ou1, ou2, ou3):
    choice = ""
    while choice == "":
        print("Your options are: \n1) ", op1, ",\n2) ", op2, ", or \n3) ", op3, )
        print("Which would you like to chose?(1/2/3)\n      Answer: ")
        choice = input()
        if choice == 1:
            print(ou1)
            Consequence()
        elif choice == 2:
            print(ou1)
            Consequence()
        elif choice == 3:
            print(ou1)
            Consequence()
        else:
            print("Sorry, you can only respond with a '1', '2'. and '3'")
            choice = ""

def Consequence():
    print("")

#-----Character Info:-----
Name=""
Alive=True
Inventory={"Rawhide Armor"
           "Quiver"
           "Leather Satchel"
}

#-----Leveling Info:-----
Level=1
TotalExperience=0
    #Skill Specific Levels:
RangedWeapons=1
ShortSwordsDaggers=1
EvasionSkill=1
StealthSkill=1
TotalSkillLevel=(RangedWeapons + ShortSwordsDaggers + EvasionSkill + StealthSkill)/4

#-----Actual Game:-----
print ("""\n
`7MMF'     A     `7MF'     `7MM                                           
  `MA     ,MA     ,V         MM                                           
   VM:   ,VVM:   ,V .gP"Ya   MM  ,p6"bo   ,pW"Wq.`7MMpMMMb.pMMMb.  .gP"Ya 
    MM.  M' MM.  M',M'   Yb  MM 6M'  OO  6W'   `Wb MM    MM    MM ,M'   Yb
    `MM A'  `MM A' 8M8M8M8M  MM 8M       8M     M8 MM    MM    MM 8M8M8M8M
     :MM;    :MM;  YM.    ,  MM YM.    , YA.   ,A9 MM    MM    MM YM.    ,
      VF      VF    `Mbmmd'.JMML.YMbmd'   `Ybmd9'.JMML  JMML  JMML.`Mbmmd'
                                                                          """)
