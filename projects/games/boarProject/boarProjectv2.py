#boarProject v2.0
#------Standard Chances:-----
    #Hit Chance:
        #(skill level)*(player level)=attackSucsessfulChance
        #(difficulty level)*(player level)=

#-----Imports:----
import random
import time

#-----Itmes:-----
ItemDescriptions={
	"2) Rawhide Armor": "Rough form of protection, stitched together.(+5 protection)",
	"1) Leather Satchel": "An old, raggedy sack that carries the few things you have.",
	"3) Quiver": "An old quiver you father used, there is a family seal on it's front."
}

#-----Random Variables and Defs:-----
def Intro():
    iteration = 0
    while not iteration >= 35:
        print("\n")
        time.sleep(0.03)
        iteration = iteration + 1

#-----Mob Info:-----
Boar1Dead=False

#-----Mob Interaction System:-----
def choose3_3(in1, in2, in3, out1, out2, out3):
    choice = ""
    while choice == "":
        print("Your options are: \n1) ", in1, ",\n2) ", in2, ", or \n3) ", in3)
        print("Which would you like to chose?(1/2/3)\n      Answer: ")
        choice = input()
        choice = int(choice)
        if choice == "1":
            print(out1)
            Consequence1()
        elif choice == "2":
            print(out2)
            Consequence2()
        elif choice == "3":
            print(out3)
            Consequence3()
        else:
            print("Sorry, you can only respond with a '1', '2'. and '3'")
            choice = ""

def choose2_2(in1, in2, out1, out2):
    choice = ""
    while choice == "":
        print("Your options are: \n1) ", in1, "\n2) ", in2)
        choice = input("Which would you like to chose?(1/2)\n      Answer: ")
        if choice == "1":
            print(out1)
            Consequence1()
        elif choice == "2":
            print(out2)
            Consequence2()
        else:
            print("Sorry, you can only respond with a '1' or '2'")
            choice = ""

def Consequence1():
    print("")

def Consequence2():
    print("")

def Consequence3():
    print("")

#-----Character Info:-----
Name=""
Alive=True
Inventory={
    "Rawhide Armor"
    "Quiver"
    "Leather Satchel"
}
Ammo={
    "Arrows"
    "Bolts"
    "Throwing Knives"
    "Throwing Knives"
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
GameIsPlaying = True
while GameIsPlaying == True:
    Play = input("Would you like to play?(y/n)")
    Play = Play.upper()
    if Play.startswith("Y") and "NO" not in Play:
        print("Great! Let's get started then.")
        while Name == "":
            Name = input("What's your name!(16 characters max.) \n              ")
            if len(Name)>=17:
                print("Sorry we don't support your usage of a name that is longer than 16 characters. Please eneter a shorter name.\n")
                Name = ""
            else:
                print("\n")
            LenName = len(Name)
        StartWeapon = ""
        while StartWeapon =="":
            print("What weapon would you like to start your adventure with?")
            in1 = "Bow"
            in2 = "Dagger"
            out1 = "You start out your hunting trip with a Bow and 10x arrows. Good luck!"
            out2 = "You start your hunting trip with a dagger to defend yourself with."
            def Consequence1():
                dict["Ammo"]["Amount"] = dict["Ammo"]["Amount"] + 10
                Inventory["Bow"]
                print("YEET")
            choose2_2(in1, in2, out1, out2)
        time.sleep(3)
        Intro()
        print("You continue your long trek in the woods, so far you haven't been too successful while hunting, but you see a wild board ahead.\nAs it approachs you, you have a few options.")
    else:
        print("That's too bad :(")
        print("Well have a good day")
        GameIsPlaying = False
        
