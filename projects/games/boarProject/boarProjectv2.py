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
    while not iteration >= 7:
        print("\n")
        time.sleep(0.03)
        iteration = iteration + 1

#-----Mob Info:-----
Boar1Dead=False

#-----Mob Interaction System:-----
def choose3_3(in1, in2, in3):
    choice = ""
    while choice == "":
        print("Your options are: \n1) ", in1, ",\n2) ", in2, ", or \n3) ", in3)
        print("Which would you like to chose?(1/2/3)\n      Answer: ")
        choice = input()
        choice = int(choice)
        if choice == "1":
            Con1()
        elif choice == "2":
            Con2()
        elif choice == "3":
            Con3()
        else:
            print("Sorry, you can only respond with a '1', '2'. and '3'")
            choice = ""

def choose2_2(in1, in2):
    choice = ""
    while choice == "":
        print("Your options are: \n1) ", in1, "\n2) ", in2)
        choice = input("Which would you like to chose?(1/2)\n      Answer: ")
        if choice == "1":
            Con1()
        elif choice == "2":
            Con2()
        else:
            print("Sorry, you can only respond with a '1' or '2'")
            choice = ""

#-----Character Info:-----
Name=""
Alive=True
Inventory={
    "Rawhide Armor":True,
    "Quiver":True,
    "Leather Satchel":True
}

Ammo = {"Arrows": {"Normal":0, "Fire":0, "Water":0, "Blinking":0},
        "Throwing Knives": {"Normal":0, "Fire":0, "Water":0, "Blinking":0}
        }

#-----Leveling Info:-----
Level=1
TotalExperience=0
    #Skill Specific Levels:
RangedWeapons=1
ShortSwordsDaggers=1
EvasionSkill=1
StealthSkill=1
Scavange=1
TotalSkillLevel=(Scavange + RangedWeapons + ShortSwordsDaggers + EvasionSkill + StealthSkill)/5

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
time.sleep(1.5)
Intro()
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
        SWeap = False
        while SWeap == False:
            print("What weapon would you like to start your adventure with?")
            in1 = "Bow"
            in2 = "Dagger"
            def Con1():
                Ammo["Arrows"]["Normal"] = Ammo["Arrows"]["Normal"]+10
                Inventory["Bow"] = True
                SWeap = True
            def Con2():
                Inventory["Dagger"] = True
                SWeap = True
            choose2_2(in1, in2)
        time.sleep(3)
        print("You continue your long trek in the woods, so far you haven't been too successful while hunting, but you see a wild board ahead.\nAs it approachs you, you have a few options.")
        print("As you walk into the edge of a clearing you can see a wild boar grazing on some grass.")
        print("""
            _,-"'''"-..__
         |`,-'_. `  ` ``  `--'"'".
         ;  ,'  | ``  ` `  ` ```  `.
       ,-'   ..-' ` ` `` `  `` `  ` |
     ,'    ^    `  `    `` `  ` `.  ;
    `}_,-^-   _ .  ` \ `  ` __ `   ;
       `"---"' `-`. ` \---""`.`.  `;
                  \\` ;       ; `. `,
                   ||`;      / / | |
                  //_;`    ,_;' ,_;" """)
        print("What would you like to do?")
        in1 = "Shoot at the boar with a bow"
        in2 = "Try to stab the boar"
        in3 = "Attempt to sneak past it and keep hunting"
        def Con1():
            if Inventory[Bow] == True:
                chance = random.randrange(2)+1 +RangedWeapons
                if chance >= 2:
                    print("You are able to hit the boar while he is not looking and kill it humanely")
                    RangedWeapons = RangedWeapons +1
                    print("+1 Skill to Ranged Weapons\nWould you like to loot the Boar?(y/n)")
                    Loot = input().Upper()
                    if Loot == "Y":
                        print("You loot the boar")
                        LootChance = random.randrange(10)+1
                        if LootChance >= 2:
                            print("You are able to quickly skin the boar and get a good portion of meat from it.")
                            Inventory[BoarMeat]=True
        def Con2():
            print("")
        def Con3():
            print("")
        print("What would you like to do now?")
                            
    else:
        print("That's too bad :(")
        print("Well have a good day")
        GameIsPlaying = False
