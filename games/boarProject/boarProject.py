#-------Standard chances are as follows:-------
    #Evasion Chance is 1/2
    #Bow hit chance is 1/3
    #Dagger hit chance is 1/3

#-------Imports:-------
import random

#-------inventory:-------
arrows=0
ssword=0
coins=10
dagger=0
furPelt=0
boarMeat=0
bow=0
bandage=0
Map=0
#-------Random Var Declerations------
valeCenter2=0
boarDone=0
valeCenter=0

#-------Mob info:-------
boarDead=False

#-------Character Info:-------
name=""
life=1
#---Leveling Info:---
level=1
Experience=0
rangedWeapons=1
shortSwordsDaggers=1
evasionSkill=1
stealthSkill=1
totalSkillLevel=rangedWeapons + shortSwordsDaggers + evasionSkill + stealthSkill
PcurrentHP=50
PHPcalc=level * 25
PmaxHP=PHPcalc + 25


print ("""\n
`7MMF'     A     `7MF'     `7MM                                           
  `MA     ,MA     ,V         MM                                           
   VM:   ,VVM:   ,V .gP"Ya   MM  ,p6"bo   ,pW"Wq.`7MMpMMMb.pMMMb.  .gP"Ya 
    MM.  M' MM.  M',M'   Yb  MM 6M'  OO  6W'   `Wb MM    MM    MM ,M'   Yb
    `MM A'  `MM A' 8M8M8M8M  MM 8M       8M     M8 MM    MM    MM 8M8M8M8M
     :MM;    :MM;  YM.    ,  MM YM.    , YA.   ,A9 MM    MM    MM YM.    ,
      VF      VF    `Mbmmd'.JMML.YMbmd'   `Ybmd9'.JMML  JMML  JMML.`Mbmmd'
                                                                          """)
start=""
while start=="":
    start=input("Start? y/n: ")
    start=start.lower()
    if start=="y":
        #Name Section
        while name=="":
            name=input("What's your name?(16 characters max.) \n            ")
            if len(name)>=17:
                print("Sorry we don't support your usage of a name that is longer than 16 characters. Please eneter a shorter name.")
                name=""
                print("")
            else:
                print("")
            lenName=len(name)
        #Initial Weapon Stuff
        startWeapon=("")
        while startWeapon=="":
            startWeapon=input("What weapon would you like to start with? \nA: A Bow \nB: A Dagger \nAnswer: ")
            startWeapon=startWeapon.upper()
            if startWeapon=="A":
                rangedWeapons=rangedWeapons+0.5
                bow=1
                arrows=5
                print("\nYou get a shortbow and 5 arrows to start you journey")
            elif startWeapon=="B":
                shortSwordDagger=shortSwordDagger+0.5
                dagger=1
                print("\nYou get a dagger to start you adventure")
            else:
                print("You can only enter 'A' or 'B'.\n")
                startWeapon=""
        print("""\nYou continue your long trek in the woods, so far you haven't been too successful while hunting, but you see a wild board ahead.\nAs it approachs you, you have a few options.

              _,-"'''"-..__
         |`,-'_. `  ` ``  `--'"'".
         ;  ,'  | ``  ` `  ` ```  `.
       ,-'   ..-' ` ` `` `  `` `  ` |
     ,'    ^    `  `    `` `  ` `.  ;
    `}_,-^-   _ .  ` \ `  ` __ `   ;
       `"---"' `-`. ` \---""`.`.  `;
                  \\` ;       ; `. `,
                   ||`;      / / | |
                  //_;`    ,_;' ,_;"
        """)
        #Boar encounter
        boar=""
        while boar=="":
            boar=input("Options \n A: Shoot the Boar with an arrow \n B: Draw a dagger and charge the boar \n C: Run \n Answer: ")
            boar=boar.upper()
            print("\n")
            #Shoot the Boar with an Arrow
            if boar=="A":
                if bow==1:
                    if arrows>=1:
                        arrows=arrows-1
                        print("You take aim and fire")
                        print("\n")
                        arrowHit=random.randrange(3)+1
                        if arrowHit==1:
                            rangedWeaopns=rangedWeapons+0.5
                            print("Nice Shot! You shot the boar dead in the head, taking it down before it notices you")
                            boarDead=True
                            boarKilledByBow=True
                            boarKilledByDagger=False
                        else:
                            print("You miss, gaining the notice of the boar, it begins to charge at you")
                            print("\n")
                            boar2=""
                            while boar2=="":
                                boar2=input("As it charges, you have limited options, they are: \n A: Get to cover \n B: Wield dagger in defence \n C: Fire again \n Answer: ")
                                print("\n")
                                boar2=boar2.upper()
                                if boar2=="A":
                                    print ("You run for cover")
                                    print("\n")                    
                                    evasion=random.randrange(2)+1
                                    if evasion==1:
                                        print("You trip and fall, the boar charges straight through you, impailing you")
                                        life=0
                                    else:
                                        print("You sucsessfuly get to the bushes. Your safe...for now.")
                                        evasionSkill=evasionSkill+0.5
                                elif boar2=="B":
                                    if dagger>=1:
                                        daggerHit=random.randrange(3)+1
                                        if daggerHit==1:
                                            print("You succsesfully stab the boar")
                                            shortSwordDagger=shortSwordDagger+0.5
                                            boarDead=True
                                            boarKilledbyDagger=True
                                            boarKilledbyBow=False
                                        else:
                                            print("You miss and the boar impales you, killing you. \n")
                                            life=0
                                            boarDone=0
                                    else:
                                        boar3=""
                                        while boar3=="":
                                            boar3=input("You don't have a dagger to charge with, so you can either \n A:  Shoot at the boar with your bow \n B: Run for cover \n Answer: ")
                                            boar3=boar3.upper()
                                            if boar3=="A":
                                                boar2="C"
                                            elif boar3=="B":
                                                print ("You run for cover")
                                                print("\n")                    
                                                evasion=random.randrange(2)+1
                                                if evasion==1:
                                                    print("You trip and fall, the boar charges straight through you, impailing you")
                                                    life=0
                                                else:
                                                    print("You sucsessfuly get to the bushes. Your safe...for now.")
                                                    evasionSkill=evasionSkill+0.5
                                            else:
                                                print("You can only answer in 'A' or 'B' or 'C'.")
                                                boar3=""
                                elif boar2=="C":
                                    if bow>=1:
                                        if arrows>=1:
                                            arrowHit=random.randrange(3)+1
                                            if arrowHit==1:
                                                print("You hit the boar taking it down")
                                                rangedWeapons=rangedWeapons+0.5
                                                boarDead=True
                                                boarKilledByBow=True
                                                boarKilledByDagger=False
                                            else:
                                                print("You miss the boar, it charges impaling you")
                                                life=0
                                        else:
                                            print("You don't have any arrows. The boar imaples you.")
                                            life=0
                                    else:
                                        boar4=input("")
                                else:
                                    print("You can only answer with 'A', 'B', or 'C'.")
            #Draw your Dagger and Charge the Boar
            elif boar=="B":
                if dagger==1:
                    boarAlert=random.randrange(2)+1
                    if boarAlert==1:
                        print("The boar notices you and starts charging at you.")
                        boarCharging=""
                        while boarCharging=="":
                            boarCharging=input("You have two options to survive: \n A: Run away \n B: Keep charging and attempt stab the boar \nAnswer: ")
                            boarCharging=boarCharging.upper()
                            if boarCharging=="A":
                                evasion=random.randrange(3)+1
                                if evasion==1:
                                    if arrows>=2:
                                        print("You sucsessfully get away from the boar but you have lost 2 of your arrows while fleeing")
                                        evasionSkill=evasionSkill+1
                                        arrows=arrows-2
                                    else:
                                        print("You sucsesfully get away from the boar.")
                                        evasionSkill=evasionSkill+1
                                else:
                                    print("You are unsecsessful at fleeing from the boar, it impales you as you run away in fear.")
                                    life=0
                            if boarCharging=="B":
                                daggerHit=random.randrange(2)+1
                                if daggerHit==1:
                                    print("\nYou stab the boar in the heart just before it reaches you. It was a close call with death but you killed the boar")
                                    shortSwordDagger=shortSwordDagger+1
                                    boarDead=True
                                    boarKilledByBow=False
                                    boarKilledByDagger=True
                                else:
                                    print("You attempt to stab the boar but don't have the strength. The boar impalles you.")
                                    life=0
                        else:
                            print("You charge the bow without alerting it. You kill it silently with extreme persission.")
                            stealthSkill=stealthSkill+1
                            shortSwordDagger=shortSwordDagger+0.5
                            boarDead=True
                            boarKilledByBow=False
                            boarKilledByDagger=True
                    else:
                        print("you don't have a dagger, but you chargin alerts the bear")
                        boarCharging2=""
                        while boarCharging2=="":
                            boarCharging2=input("You can either run or try and shoot it with another arrow. \nA: Flee \nB: Shoot at the boar \nAnswer: ")
                            boarCharging2=boarCharging2.upper()
                            if boarCharging2=="A":
                                evasion=random.randrange(2)+1
                                if evasion==1:
                                    if arrows>=2:
                                        print("You escape the boar, but while running you lost two of your arrows.")
                                        arrows=arrows-2
                                        evasionSkill=evasionSkill+0.5
                                    else:
                                        print("You give the boar the slip.")
                                        evasionSkill=evasionSkill+0.5
                                else:
                                    print("As you flee the boar catches up with you and you are impaled.")
                            elif boarCharging2=="B":
                                if arrows>=1:
                                    arrowHit=random.randrange(2)+1
                                    if arrowHit==1:
                                        print("You hit the boar in the head, killing it.")
                                        boadDead=True
                                        boarKilledByBow=True
                                        boarKilledByDagger=False
                                    else:
                                        print("You miss and the boar reaches you.")
                                        life=0
                                else:
                                    print("You don't have any arrows to shoot with and so you are forced to flee.")
                                    evasion=random.randrange(2)+1
                                    if evasion==1:
                                        print("You get away safely.")
                                        evasionSkill=evasionSkill+0.5
                                    else:
                                        print("Thoe Boar cathes up to you, impaling you upon a tree.")
                                        life=0
                            else:
                                print("You can only answer with an 'A' or a 'B'.")
                                boarCharging2==""
            #Run
            elif boar=="C":
                evasion=random.randrange(3)+1
                if evasion==1:
                    print("You escape the boar to live another day")
                    evasionSkill=evasionSkill+0.5
                    #boarDone is to move to town
                    boarDone=1
                else:
                    print("The boar catches up with you and impales you on a tree.")
                    life=0
            else:
                print("You can only answer with a 'A', 'B', or 'C'.")
                boar=""
        #Looting the Dead Boar
        if boarDead==True:
            scavengeBoar=""
            while scavengeBoar=="":
                scavengeBoar=input("The boar lies dead, what would you like to do? \n A: Scavenge the boar \n B: Leave it and continue \n Answer: ")
                scavengeBoar=scavengeBoar.upper()
                if scavengeBoar=="A":
                    die0=random.randrange(8)+1
                    die1=random.randrange(10)+1
                    if die0!=1:
                        if boarKilledByBow==True:
                            arrows=arrows+1
                            coins=coins+5
                            furPelt=furPelt+1
                            boarMeat=boarMeat+1
                            print("You recovered your arrow, found 5 gold coins, a fur pelt, and some boar meat.")
                            boarDone=1
                            if die1==1:
                                ssword+1
                                print("You also find a short sword")
                            else:
                                print("")
                                print("You now have ", arrows," arrows and ", coins," coins.")
                        elif boarKilledByDagger==True:
                            coins=coins+5
                            furPelt=furPelt+1
                            boarMeat=boarMeat+1
                            print("You found 5 gold coins, 1 fur pelt, and some boar meat.")
                            boarDone=1
                            if die1==1:
                                ssword+1
                                print("You also find a short sword")
                            else:
                                print("")
                            print("You now have", coins," coins,")
                        else:
                            print("")
                    else:
                        print("")
                        print("The boar is covered in it's own blood. It would be foolish to search through it.")
                        boarDone=1
                elif scavengeBoar=="B":
                    print("You continue on your hunting after killing the boar")
                    boarDone=1
                else:
                    print("Please answer in only the letters 'A' or 'B'")
                    scavangeBoar==""
                    #Vale
        if boarDone==1:
            if life==1:
                print (" \n After continuing through the forrest for a while, you come across a small town in a clearing. There are a few builings in the center of the town, Including a store, and a few people walking about.")
                valeCenter=""
        while valeCenter=="":
            valeCenter=input ("What is your course of action? \n A: Talk to the people in the town center \n B: Visit the store \n Answer: ")
            valeCenter=valeCenter.upper()
            if valeCenter=="A":
                    print ("The townspeople look at you oddly, not used to visitors to their town. From your conversation, you gather that you are in a town called Vale, and that you have ventured far deeper into the woods than you originally intended. One man, realizing that you are lost, leads you to the store telling you that he thought he saw a map in there a few days ago.")
                    valeCenter="B"
            if valeCenter=="B":
                print (" \n You enter a well lit a neatly organized building, with shelves of various goods lined on the walls. A rather plump man smiles at you from behind a counter.")
                valeStore=""
                while valeStore=="":
                    valeStore=input (" \n See anything you want to buy? \n A: Bandage *15HP,5s* \n B: Map *5s* \n C: Nothing \n Answer: ")
                    valeStore=valeStore.upper()
                    if valeStore=="A":
                        if coins>=5:
                            if bandage==0:
                                bandage=1
                                coins=coins-5
                                print (" \n Thank you for your purchase!")
                                valeStore=""
                            else:
                                print (" \n We only had one, and you bought it pal.")
                                valeStore=""
                        else:
                            print ("You don't have enough money for this.")
                            valeStore=""
                    if valeStore=="B":
                        if coins>=5:
                            if Map==0:
                                Map=1
                                coins=coins-5
                                print (" \n Thanks for the purchase!")
                                valeStore=""
                            else:
                                print (" \n You already have a Map!")
                                valeStore=""
                        else:
                            print (" \n You don't have enough money for this!")
                            valeStore=""
                    if valeStore=="C":
                        valeCenter2=""
#Second time in town after getting a map. This currently doesn't work, and will just print gravestones. We need to figure out what comes after this.
        while valeCenter2=="":
            print (" \n You've arrived back in the center of the town. The few people who were milling about earlier seem to have left, leaving the town center earily quiet.")
            if map==1:
                valeCenter2=input (" \n With your map you see that the path leading out of the north side of the village leads to a much larger city, called Orion. Do you: \n A: Take the path and head towards Orion. \n B: Go back to the store. \n Answer ")
                valeCenter2=valeCenter2.upper()
                
                        
                    
         
       
        #Death Messages
    if life==0:
        if lenName==0:
                    print("""
                 ______
           _____/      \\_____
          |  _     ___   _   ||
          | | \     |   | \  ||
          | |  |    |   |  | ||
          | |_/     |   |_/  ||
          | | \     |   |    ||
          | |  \    |   |    ||
          | |   \. _|_. | .  ||
          |                  ||
          |       you        ||
          |                  ||
  *       | *   **    * **   |**      **
   \))....\\/.,(//,,..,,\||(,,.,\\,.((//
   """)
        elif lenName==1:
                print("""
                 ______
           _____/      \\_____
          |  _     ___   _   ||
          | | \     |   | \  ||
          | |  |    |   |  | ||
          | |_/     |   |_/  ||
          | | \     |   |    ||
          | |  \    |   |    ||
          | |   \. _|_. | .  ||
          |                  ||
          |      """, name, """         ||
          |                  ||
  *       | *   **    * **   |**      **
   \))....\\/.,(//,,..,,\||(,,.,\\,.((//
   """)
        elif lenName==2:
                print("""
                 ______
           _____/      \\_____
          |  _     ___   _   ||
          | | \     |   | \  ||
          | |  |    |   |  | ||
          | |_/     |   |_/  ||
          | | \     |   |    ||
          | |  \    |   |    ||
          | |   \. _|_. | .  ||
          |                  ||
          |      """, name, """        ||
          |                  ||
  *       | *   **    * **   |**      **
   \))....\\/.,(//,,..,,\||(,,.,\\,.((//
   """)
        elif lenName==3:
                print("""
                 ______
           _____/      \\_____
          |  _     ___   _   ||
          | | \     |   | \  ||
          | |  |    |   |  | ||
          | |_/     |   |_/  ||
          | | \     |   |    ||
          | |  \    |   |    ||
          | |   \. _|_. | .  ||
          |                  ||
          |      """, name, """       ||
          |                  ||
  *       | *   **    * **   |**      **
   \))....\\/.,(//,,..,,\||(,,.,\\,.((//
   """)
        elif lenName==4:
                print("""
                 ______
           _____/      \\_____
          |  _     ___   _   ||
          | | \     |   | \  ||
          | |  |    |   |  | ||
          | |_/     |   |_/  ||
          | | \     |   |    ||
          | |  \    |   |    ||
          | |   \. _|_. | .  ||
          |                  ||
          |      """, name, """      ||
          |                  ||
  *       | *   **    * **   |**      **
   \))....\\/.,(//,,..,,\||(,,.,\\,.((//
   """)
        elif lenName==5:
                print("""
                 ______
           _____/      \\_____
          |  _     ___   _   ||
          | | \     |   | \  ||
          | |  |    |   |  | ||
          | |_/     |   |_/  ||
          | | \     |   |    ||
          | |  \    |   |    ||
          | |   \. _|_. | .  ||
          |                  ||
          |      """, name, """     ||
          |                  ||
  *       | *   **    * **   |**      **
   \))....\\/.,(//,,..,,\||(,,.,\\,.((//
   """)
        elif lenName==6:
                print("""
                 ______
           _____/      \\_____
          |  _     ___   _   ||
          | | \     |   | \  ||
          | |  |    |   |  | ||
          | |_/     |   |_/  ||
          | | \     |   |    ||
          | |  \    |   |    ||
          | |   \. _|_. | .  ||
          |                  ||
          |     """, name, """     ||
          |                  ||
  *       | *   **    * **   |**      **
   \))....\\/.,(//,,..,,\||(,,.,\\,.((//
   """)
        elif lenName==7:
                print("""
                 ______
           _____/      \\_____
          |  _     ___   _   ||
          | | \     |   | \  ||
          | |  |    |   |  | ||
          | |_/     |   |_/  ||
          | | \     |   |    ||
          | |  \    |   |    ||
          | |   \. _|_. | .  ||
          |                  ||
          |     """, name, """    ||
          |                  ||
  *       | *   **    * **   |**      **
   \))....\\/.,(//,,..,,\||(,,.,\\,.((//
   """)
        elif lenName==8:
                print("""
                 ______
           _____/      \\_____
          |  _     ___   _   ||
          | | \     |   | \  ||
          | |  |    |   |  | ||
          | |_/     |   |_/  ||
          | | \     |   |    ||
          | |  \    |   |    ||
          | |   \. _|_. | .  ||
          |                  ||
          |   """, name, """     ||
          |                  ||
  *       | *   **    * **   |**      **
   \))....\\/.,(//,,..,,\||(,,.,\\,.((//
   """)
        elif lenName==9:
                print("""
                 ______
           _____/      \\_____
          |  _     ___   _   ||
          | | \     |   | \  ||
          | |  |    |   |  | ||
          | |_/     |   |_/  ||
          | | \     |   |    ||
          | |  \    |   |    ||
          | |   \. _|_. | .  ||
          |                  ||
          |   """, name, """    ||
          |                  ||
  *       | *   **    * **   |**      **
   \))....\\/.,(//,,..,,\||(,,.,\\,.((//
   """)
        elif lenName==10:
                print("""
                 ______
           _____/      \\_____
          |  _     ___   _   ||
          | | \     |   | \  ||
          | |  |    |   |  | ||
          | |_/     |   |_/  ||
          | | \     |   |    ||
          | |  \    |   |    ||
          | |   \. _|_. | .  ||
          |                  ||
          |  """, name, """    ||
          |                  ||
  *       | *   **    * **   |**      **
   \))....\\/.,(//,,..,,\||(,,.,\\,.((//
   """)
        elif lenName==11:
                print("""
                 ______
           _____/      \\_____
          |  _     ___   _   ||
          | | \     |   | \  ||
          | |  |    |   |  | ||
          | |_/     |   |_/  ||
          | | \     |   |    ||
          | |  \    |   |    ||
          | |   \. _|_. | .  ||
          |                  ||
          |  """, name, """   ||
          |                  ||
  *       | *   **    * **   |**      **
   \))....\\/.,(//,,..,,\||(,,.,\\,.((//
   """)
        elif lenName==12:
                print("""
                 ______
           _____/      \\_____
          |  _     ___   _   ||
          | | \     |   | \  ||
          | |  |    |   |  | ||
          | |_/     |   |_/  ||
          | | \     |   |    ||
          | |  \    |   |    ||
          | |   \. _|_. | .  ||
          |                  ||
          |  """, name, """  ||
          |                  ||
  *       | *   **    * **   |**      **
   \))....\\/.,(//,,..,,\||(,,.,\\,.((//
   """)
        elif lenName==13:
                print("""
                 ______
           _____/      \\_____
          |  _     ___   _   ||
          | | \     |   | \  ||
          | |  |    |   |  | ||
          | |_/     |   |_/  ||
          | | \     |   |    ||
          | |  \    |   |    ||
          | |   \. _|_. | .  ||
          |                  ||
          | """, name, """  ||
          |                  ||
  *       | *   **    * **   |**      **
   \))....\\/.,(//,,..,,\||(,,.,\\,.((//
   """)
        elif lenName==14:
                print("""
                 ______
           _____/      \\_____
          |  _     ___   _   ||
          | | \     |   | \  ||
          | |  |    |   |  | ||
          | |_/     |   |_/  ||
          | | \     |   |    ||
          | |  \    |   |    ||
          | |   \. _|_. | .  ||
          |                  ||
          | """, name, """ ||
          |                  ||
  *       | *   **    * **   |**      **
   \))....\\/.,(//,,..,,\||(,,.,\\,.((//
   """)
        elif lenName==15:
                print("""
                 ______
           _____/      \\_____
          |  _     ___   _   ||
          | | \     |   | \  ||
          | |  |    |   |  | ||
          | |_/     |   |_/  ||
          | | \     |   |    ||
          | |  \    |   |    ||
          | |   \. _|_. | .  ||
          |                  ||
          |""", name, """ ||
          |                  ||
  *       | *   **    * **   |**      **
   \))....\\/.,(//,,..,,\||(,,.,\\,.((//
   """)
        elif lenName==16:
                print("""
                 ______
           _____/      \\_____
          |  _     ___   _   ||
          | | \     |   | \  ||
          | |  |    |   |  | ||
          | |_/     |   |_/  ||
          | | \     |   |    ||
          | |  \    |   |    ||
          | |   \. _|_. | .  ||
          |                  ||
          |""", name, """||
          |                  ||
  *       | *   **    * **   |**      **
   \))....\\/.,(//,,..,,\||(,,.,\\,.((//
   """)
        else:
            print("You died")
    elif start=="n":
        print("\n")
        print("Okay, cya pal")
    else:
        print("\n")
        print("You have to answer 'Y' for yes or 'N' for no.")
        start=""
#Wait to Exit
exit="a"
while exit=="a":
    exit=input("\nPress 'enter' to exit")
