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
    You continue your long trek in the woods, you haven't been too successful while hunting. You have only 5 arrows remaining, and you see a wild board ahead. As it approachs you, you ready your hunting bow.


       
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
while boar == "A":
    print ("You take aim and fire")
    print("\n")

    import random

    die1=random.randrange(3)+1
    boar="k"
    
    if die1 == 1:
        print("You shot the boar dead in the head, taking it down before it notices you")
        break
    else:
        print("You miss, gaining the notice of the boar, it begins to charge at you")
        print("\n")
        boar2=input("As it charges, you have limited options, they are: \n A: Get to cover \n B: Wield dagger in defence \n C: Fire again ")
        while boar2 == "A":
            break
            print ("You run for cover")
            print("\n")

            import random

            die2=random.randrange(2)+1
            if die2 == 1:
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
                print("egg")
        
print("\n")
print("The boar lies dead, \n A: Scavenge the boar \n B: Leave it and continue ")
