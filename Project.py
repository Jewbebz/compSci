import random
arrows=5
ssword=0
coins=10
dagger=0
print ("""/n                             ,,                                           
`7MMF'     A     `7MF'     `7MM                                           
  `MA     ,MA     ,V         MM                                           
   VM:   ,VVM:   ,V .gP"Ya   MM  ,p6"bo   ,pW"Wq.`7MMpMMMb.pMMMb.  .gP"Ya 
    MM.  M' MM.  M',M'   Yb  MM 6M'  OO  6W'   `Wb MM    MM    MM ,M'   Yb
    `MM A'  `MM A' 8M""""""  MM 8M       8M     M8 MM    MM    MM 8M""""""
     :MM;    :MM;  YM.    ,  MM YM.    , YA.   ,A9 MM    MM    MM YM.    ,
      VF      VF    `Mbmmd'.JMML.YMbmd'   `Ybmd9'.JMML  JMML  JMML.`Mbmmd'
                                                                          """)

start=input("Start? y/n: ")
if start == "y":
    print("""
    You continue your long trek in the woods, you haven't been too successful while hunting. \nYou have only 5 arrows remaining, and you see a wild board ahead.\nAs it approachs you, you ready your hunting bow.


       
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
    boar=input("Options \n A: Shoot Boar with arrow \n B: Run \n C: Draw dagger and charge \n Answer: ")
    boar=boar.upper()
    print("\n")
    if boar == "A":
        if arrows >= 1:
            arrows=arrows-1
            print("You take aim and fire")
            print("\n")
            arrowHit=random.randrange(3)+1
            if arrowHit == 1:
                print("You shot the boar dead in the head, taking it down before it notices you")
            else:
                print("You miss, gaining the notice of the boar, it begins to charge at you")
                print("\n")
                boar2=input("As it charges, you have limited options, they are: \n A: Get to cover \n B: Wield dagger in defence \n C: Fire again ")
                print("\n")
                boar2=boar2.upper()
                if boar2 == "A":
                    print("\n")
                    print("\n")
                    print ("You run for cover")
                    print("\n")
                    evasion=random.randrange(2)+1
                    if evasion == 1:
                        print("""You trip and fall, the boar charges straight through you, impailing you \n
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
                    else:
                        print("You sucsessfuly get to the bushes. Your safe...for now.")
                elif boar2 == "B":
                    if dagger == 1:
                        daggerHit = random.randrange(3)+1
                        if daggerHit == 1:
                            print("You succsesfully stab the boar")
                        else:
                            print("You miss and the boar impales you, killing you.")
                    else:
                        print("You have no dagger, the boar charges you and you are impaled.")
                elif boar2 == "C":
        if arrows >= 1:
            arrowHit=random.randrange(3)+1
            if arrowHit == 1:
                print("You hit the boar taking it down")
            else:
                print("You miss the boar, it charges impaling you")
        else:
            print("You don't have any arrows. The bor imaples you.")
    else:
        print("")
                
    print("\n")
    scavenge1=input("The boar lies dead, \n A: Scavenge the boar \n B: Leave it and continue ")
    scavenge1=scavenge1.upper()
    if scavenge1=="A":
        die3=random.randrange(2)+1
        die4=random.randrange(10)+1
        if die3==1:
            arrows=arrows+1
            coins=coins+5
            print("You scavenged an arrow and 5 gold coins")
            if die4==1:
                print("And a short sword")
                ssword=1
            
elif start=="n":
    print("Okay, cya pal")
else:
    print("y or n pal, nothing else")
