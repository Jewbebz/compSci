import random
die1 = random.randrange(6)+1
die2 = random.randrange(6)+1
total1 = die1+die2

player1 = input("What is your name, player1?")
print(player1, "you rolled a ", die1, "and a ", die2)
print("For a total of ", total1)

die3 = random.randrange(6)+1
die4 = random.randrange(6)+1
total2 = die3+die4
player2 = (input("What is your name, player 2? "))

print(player2, "you rolled a ", die3, "and a ", die4)
print("For a total of ", total2)

if total1>total2:
    print(player1, " is the winner")
elif total2>total1:
    print(player2, " is the winner")
else:
    print("It's a tie!")
