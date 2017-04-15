import time
import random

car=("Focus", "Van", "Mustang", "Lamborghini ")

def wait_time():
    time.sleep(2)
    print ("Calculating...")
    time.sleep(2)

def car_choice():
    car1=random.choice(car)
    input("Press return to see what kind of car you will own...")
    wait_time()
    print ("You will be driving around in a: ", car1)
    

car_choice()







