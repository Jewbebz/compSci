name=""
start=input("Start? y/n: ")
start=start.lower()
if start=="y":
    while name=="":
        name=input("What's your name?(6 characters max.) \n            ")
        if len(name)==6:
            print("")
            print("Thats a super cool name dude!")
        elif len(name)<<6:
            
            print("Thats a nice name you have")

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
          |""", name, """||
          |                  ||
  *       | *   **    * **   |**      **
   \))....\\/.,(//,,..,,\||(,,.,\\,.((//
   """)
exit = "a"
while exit == "a":
    print("\n")
    exit=input("Press 'enter' to exit")
