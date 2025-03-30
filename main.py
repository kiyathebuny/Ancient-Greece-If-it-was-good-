#Hi Mr. Nagra its me your favorite comp sci student
import time# time.time() method of Time module is used to get the time in seconds
import sys#The sys module provides access to system-specific parameters and functions in Python. 
#It allows you to interact with the Python interpreter and access command-line arguments
from collections import Counter #counter is the number counter and collections
import random #this is for random number generator 
import os

def clear():
    if(os.name == "nt"):
        os.system("cls")
    else:
        os.system("clear")

def print1(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.045)
    print()

game_state = {
    #uhhhh shhh
}

def get_input(prompt=""): # Yeah this is 100% irrelevant rn but it might be useful later
    choice = input(prompt).strip().lower()
    return choice  # Return the actual input otherwise



#opening sequenceeee
print1 ("..." * 3)
print1 ("'You start hearing cheers and yells coming from all around you'")
print1 ("Press enter to wake up")
input()
print1("You force yourself up from the sand reluctantly")
print1("--: 'Wait, who even am I?'") # This one is not a subsitute
name = input("Who are you?: ")
print1(name +": 'Oh, right, I'm" + name + "'") #-- subsituting name variable that i dont have
print1("You look around to find yourself in a sort of, arena?")
print1("")