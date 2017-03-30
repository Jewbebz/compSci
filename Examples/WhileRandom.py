#Import Random Numbers

print ("Random Number Generator")

import random

die1=random.randrange(6)+1
die2=random.randrange(6)+1

total=die1 + die2



while total != 5:
    password = input("\nBad Roll ")
    die1=random.randrange(6)+1
    die2=random.randrange(6)+1

    total=die1 + die2

print("Noice")

