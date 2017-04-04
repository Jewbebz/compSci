import random
answer = random.randrange(10)+1

tries = 1
guess = int(input("Guess the number: "))

while guess != answer:
    if guess < answer:
        print("Too Low")
    else:
        print("Too High")
    guess = int(input("Guess the number: "))
    tries = tries+1

print("Correct. You've guess it in ", tries,"tries.")
