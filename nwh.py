import random
import time
while(True):
    time.sleep(1.3)
    response = random.randint(1,4)
    if response == 1:
        print("I hate this place!")
    if response == 2:
        print("The medications don't work!")
    if response == 3:
        print("I've been here for 7 years!")
    if response ==4:
        print("Nothing works here!")
