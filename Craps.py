print("""
 _    _      _                            _ 
| |  | |    | |                          | |
| |  | | ___| | ___ ___  _ __ ___   ___  | |
| |/\| |/ _ \ |/ __/ _ \| '_ ` _ \ / _ \ | |
\  /\  /  __/ | (_| (_) | | | | | |  __/ |_|
 \/  \/ \___|_|\___\___/|_| |_| |_|\___| (_)

""")

print ("welcome to Craps!")
print ("The objectve of the game is to bet on a roll of dice that results in a 7 or an 11")
print ("If you guess correctly you win if not, you lose :(")

import random

play = "y"
played = "n"
wins = 0
loses = 0

play = input("Would you Like to play?(y/n) ")
if play == "y":
    print("Sweet! let's get started.")
    while play == "y":
        if played == "n":
            die1 = random.randrange(6)+1
            die2 = random.randrange(6)+1
            total = die1 + die2
            print("You rolled a ", die1, "and a ", die2, "for a total of ", total)
            played = "y"
        else:
            while play == "y":
                if total == 7 or total == 11:
                    play = input("Congrats! Would you like to play again?(y/n) ")
                    print("")
                    wins = wins + 1
                    if play == "y":
                        die1 = random.randrange(6)+1
                        die2 = random.randrange(6)+1
                        total = die1 + die2
                        print("You rolled a ", die1, "and a ", die2, "for a total of ", total)
                    elif play == "n":
                        print("You won a total of ", wins, "times and lost a total of ", loses, "times.")
                        print("Ok, thanks for playing!")
                    else:
                        print("please only enter the letter 'y'to indicate yes, or the letter 'n' to indicate no.")
                else:
                    play = input("Darn! Would you like to try again?(y/n) ")
                    print("")
                    loses = loses +1
                    if play == "y":
                        die1 = random.randrange(6)+1
                        die2 = random.randrange(6)+1
                        total = die1 + die2
                        print("You rolled a ", die1, "and a ", die2, "for a total of ", total)
                    elif play == "n":
                        print("You won a total of ", wins, "times and lost a total of ", loses, "times.")
                        print("Ok, thanks for playing!")
                    else:
                        print("please only enter the letter 'y'to indicate yes, or the letter 'n' to indicate no.")
elif play == "n":
    print("OK, have a good day!")
else:
    print("Please answer with a 'y' for yes or a 'n' for no.")
