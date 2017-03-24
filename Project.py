#Standard chances are as follows:
#Evasion Chance is 1/2
#Bow hit chance is 1/3
#Dagger hit chance is 1/3

import random

arrows=0
ssword=0
coins=10
dagger=0
furPelt=0
boarMeat=0

boarDead=False

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
    while name=="":
        name=input("What's your name?(16 characters max.) \n            ")
        if len(name)==6:
            print("")
            print("Thats a super cool name dude!")
            lenName=6
        elif len(name)>>6:
            print("")
            print("You can only have a six character name for now, we're working on allowng longer names.")
        elif len(name)<<6:
            print("Thats a nice name you have")
            print("")
            lenName=len(name)
    startWeapon=input("What weapon would you like to start with? \nA: A Bow \nB: A Dagger \nAnswer: ")
    startWeapon=startWeapon.upper()
    if startWeapon=="A":
        bow=1
        arrows=5
        print("You get a shortbow and 5 arrows to start you journey")
    elif startWeapon=="B":
        dagger=1
        print("You get a dagger to start you adventure")
    else:
        print("You can only have two options. 'A' or 'B' it really not that hard dude.")
    print("""\nYou continue your long trek in the woods, you haven't been too successful while hunting. You have only 5 arrows remaining, and you see a wild board ahead.\nAs it approachs you, you ready your hunting bow.


       
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
    boar=input("Options \n A: Shoot the Boar with an arrow \n B: Draw a dagger and charge the boar \n C: Run \n Answer: ")
    boar=boar.upper()
    print("\n")
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
                                print("You can only answer in 'A' or 'B' or 'C' dude!")
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
                        print("dude, you can only answe in 'A', 'B', or 'C'")
    elif boar=="B":
        if dagger==1:
            boarAlert=random.randrange(4)+1
            if boarAlert==1:
                print("The boar notices you and starts charging at you.")
                boarCharging=input("You have two options to survive: \n A: Run away \n B: Keep chargin and attempt stab the boar \nAnswer: ")
                boarCharging=boarChargin.upper()
                if boarCharging=="A":
                    evasion=random.randrange(3)+1
                    if evasion==1:
                        print("You sucsessfully get away from the boar but you have lost 2 of your arrows while fleeing")
                        arrows=arrows-2
                    else:
                        print("You are unsecsessful at fleeing from the boar, it impales you as you run away in fear.")
                        life=0
                else:
                    daggerHit = random.randrange(2)+1
                    if daggerHit == 1:
                        print("You stab the boar in the heart just before it reaches you. It was a close call with death but you killed the boar")
                        boarDead = True
                        boarKilledByBow = False
                        boarKilledByDagger = True
                    else:
                        print("You attempt to stab the boar but don't have the strength. The boar impalles you.")
        else:
            print("you don't have a dagger, but you chargin alerts the bear")
            boarCharging=input("You can either run or try and shoot it with another arrow. \nA: Flee \nB: Shoot at the boar \nAnswer: ")
            boarCharging=boarCharging.upper()
            if boarCharging=="A":
                evasion=random.randrange(2)+1
                if evasion==1:
                    print("You escape the boar, but while running you lost two of your arrows.")
                    arrows=arrows-2
                else:
                    print("As you flee the boar catches up with you and you are impaled.")
            elif boarChargin=="A":
                if arrows >= 1:
                    arrowHit = random.randrange(2)+1
                    if arrowHit == 1:
                        print("You hit the boar in the head, killing it.")
                        boadDead = True
                        boarKilledByBow = True
                        boarKilledByDagger = False
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
    elif boar=="C":
        evasion=random.randrange(3)+1
        if evasion==1:
            print("You escaoe the boar to live another day")
        else:
            print("The boar catches up with you and impales you on a tree.")
    else:
        print("You done goofed. Dude, only y's and n's it's not that hard.")
    if boarDead==True:
        scavenge=input("The boar lies dead, what would you like to do? \n A: Scavenge the boar \n B: Leave it and continue \n Answer: ")
        scavenge=scavenge.upper()
        if scavenge=="A":
            die0=random.randrange(6)+1
            die1=random.randrange(10)+1
            if die0!=1:
                arrows=arrows+1
                coins=coins+5
                furPelt=furPelt+1
                boarMeat=boarMeat+1
                print("You recovered your arrow, found 5 gold coins, a fur pelt, and some boar meat.")
                print("You now have ", arrows," arrows and ", coins," Coins.")
            else:
                print("")
                print("The boar is covered in it's own blood. It would be foolish to search through it.")
                if die1==1:
                    print("You also find a short sword")
                    ssword=1
                else:
                    print("")
        elif scavenge=="B":
            print("You continue on your hunting after killing the boar")
        else:
            print("Dude, you can only use the letters 'A' and 'B' for this one")
    else:
        print("")
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
    
exit = "a"
while exit == "a":
    print("\n")
    exit=input("Press 'enter' to exit")
