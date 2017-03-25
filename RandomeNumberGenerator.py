print ("Random Number Generator")

import random

die1=random.randrange(6)+1
die2=random.randrange(6)+1

total=die1 + die2
print ("You rolled a ", die1, "and a ", die2, "for a total of ", total)
