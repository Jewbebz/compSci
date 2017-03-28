#Standard chances are as follows:
    #Evasion Chance is 1/2
    #Bow hit chance is 1/3
    #Dagger hit chance is 1/3

#Imports:
import random

#inventory:
arrows=0
ssword=0
coins=10
dagger=0
furPelt=0
boarMeat=0
bow=0

#Mob info:
boarDead=False

#Character Info:
name=""
life=1
experience=0
level=1

print ("""\n
`7MMF'     A     `7MF'     `7MM                                           
  `MA     ,MA     ,V         MM                                           
   VM:   ,VVM:   ,V .gP"Ya   MM  ,p6"bo   ,pW"Wq.`7MMpMMMb.pMMMb.  .gP"Ya 
    MM.  M' MM.  M',M'   Yb  MM 6M'  OO  6W'   `Wb MM    MM    MM ,M'   Yb
    `MM A'  `MM A' 8M8M8M8M  MM 8M       8M     M8 MM    MM    MM 8M8M8M8M
     :MM;    :MM;  YM.    ,  MM YM.    , YA.   ,A9 MM    MM    MM YM.    ,
      VF      VF    `Mbmmd'.JMML.YMbmd'   `Ybmd9'.JMML  JMML  JMML.`Mbmmd'
                                                                          """)
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
            bow=1
            arrows=5
            print("\nYou get a shortbow and 5 arrows to start you journey")
        elif startWeapon=="B":
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
                            elif boar2=="B":
                                if dagger>=1:
                                    daggerHit=random.randrange(3)+1
                                    if daggerHit==1:
                                        print("You succsesfully stab the boar")
                                        boarDead=True
                                        boarKilledbyDagger=True
                                        boarKilledbyBow=False
                                    else:
                                        print("You miss and the boar impales you, killing you. \n")
                                        life=0
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
                                        else:
                                            print("You can only answer in 'A' or 'B' or 'C'.")
                                            boar3=""
                            elif boar2=="C":
                                if bow>=1:
                                    if arrows>=1:
                                        arrowHit=random.randrange(3)+1
                                        if arrowHit==1:
                                            print("You hit the boar taking it down")
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
                                print("You sucsessfully get away from the boar but you have lost 2 of your arrows while fleeing")
                                arrows=arrows-2
                            else:
                                print("You are unsecsessful at fleeing from the boar, it impales you as you run away in fear.")
                                life=0
                        if boarCharging=="B":
                            daggerHit=random.randrange(2)+1
                            if daggerHit==1:
                                print("\nYou stab the boar in the heart just before it reaches you. It was a close call with death but you killed the boar")
                                boarDead=True
                                boarKilledByBow=False
                                boarKilledByDagger=True
                            else:
                                print("You attempt to stab the boar but don't have the strength. The boar impalles you.")
                                life=0
                    else:
                        print("You charge the bow without alerting it. You kill it silently with extreme persission.")
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
                                print("You escape the boar, but while running you lost two of your arrows.")
                                arrows=arrows-2
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
            elif scavengeBoar=="B":
                print("You continue on your hunting after killing the boar")
            else:
                print("Please answer in only the letters 'A' or 'B'")
                scavangeBoar==""
    else:
        print("")
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
    print("'y' or 'n' pal, nothing else")
#Wait to Exit
exit="a"
while exit=="a":
    exit=input("\nPress 'enter' to exit")
