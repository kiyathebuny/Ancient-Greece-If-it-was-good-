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

def print2(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.5)
    print()

game_state = {
    "murder":False,
    "theft":False,
    "funny":False,
    "pleading 1":False,
    "pleading 2":False,

}

def get_input(prompt=""): # Yeah this is 100% irrelevant rn but it might be useful later
    choice = input(prompt).strip().lower()
    return choice  # Return the actual input otherwise



#opening sequenceeee
print1 ("You start hearing cheers and yells coming from all around you")
print1 ("Press enter to wake up")
input()
clear()
for i in range(3):
    for j in range(4):
        print (j*("."))
        time.sleep(0.1)
        clear()
time.sleep(1.5)
print1("You force yourself up from the sand reluctantly")
print1("--: 'Wait, who even am I?'") # This one is not a subsitute
name = input("Who are you?: ")
print1(name +": Oh, right, I'm " + name) #-his name is cannonically dave. like, all lowercase.
print1("You look around to find yourself in a sort of, arena?")
print1("Before you can think of your surroudings, you hear the ringing of a bell, and the sounds of cheers get quieter...") # queue mizu5
print1("You look up to see the Emperor sitting on his throne, all eyes on him") #yall i cant write for shit
print1("The Emperor shouts,")
print1("Emperor: TODAY, EVERYONE WILL WATCH THE TRIALS OF AMENDMENT, FOR THE HEINOUS CRIMES OF... wait, hold on, oh right THE CRIMES OF " + name.upper())
print1("Random Audience Member: ...What did they even do though?")
print2("...")
print1("The Emperor prompts one of the guards, and he beheads him immediately")
print2("...")
clear()
print1("Emperor: ...With that out of the way, would you like to tell us what you've done? You criminal scum")
 # guys i swear i didnt copy and paste this
 
while True: # Crime choice sequence
    print1 (name +": 'What crime did I commit again?' \n1. Murder \n2. Theft \n3. Attempts to overthrow the current political system through multistage conspiracy and bribery of government officials \n4. I'm not a criminal!") 
    choice = get_input("")
    if choice in ["1", "Murder"]:
        if game_state ["murder"] == False:
            print1(name + ": I... killed a man")
            print1("Emperor: Well! There you have it! They killed someone in cold blood!")
            print1(name + ": No, thats not what I mea-")
            print1("You're promptly cut off by the booing of the crowd")
            game_state["murder"] == True
            break

    elif choice in ["2", "Theft"]:
        if game_state ["theft"] == False:
            print1(name + ": I stole some bread so my family wouldn't starv-")
            print1("Emperor: I see! So you stole food from a poor vendor trying to make a living... How horrible!")
            print1(name + ": No, thats not what I mea-")
            print1("You're promptly cut off by the booing of the crowd")
            game_state["theft"] == True
            break

    elif choice in ["3", "Attempts to overthrow the current political system through multistage conspiracy and bribery of government officials"]:
        if game_state ["funny"] == False: #yeah im not checking the gamestate system to see if it works we'll suffer later XD
            print1(name +": Oh, uh, I tried to overthrow the current political system through multistag-... (wait what the hell no I didn't, who would even think of doing that??)")
            print1("Emperor: ...")
            print1("Emperor: I mean, uh, you wouldn't be the first, I guess?")
            print1("Emperor: But what did you REALLY do?")
            game_state["funny"] = True
            
        else: 
            print1(name +": 'No I didn't...'")

    elif choice in ["4", "I'm not a criminal!"]:
        if game_state ["pleading 1"] == False:
            print1(name  + ": I didn't do anything!")
            print1("Emperor: Well, you certainly did something, otherwise you wouldn't be here right now, so don't lie to us.")
            game_state["pleading 1"] = True
            
        else:
            print1(name  + ": uhhhhh I swear on the name of.... (wait I don't even remember their names)... anyway I swear on god I ain't do nothin'") 
            print1("Emperor: Fine then, keep your secrets")
            game_state["pleading 2"] = True
            break
# Murder = Damage, Theft = Evasion, Pleading(2) = Charisma        
print1("Emperor: Well, onto the TRIALS OF AMENDMENT!!")
print1(name + ": 'The... what?'")
print1("Emperor: Now! In front of you are 3 doors!")
print1(name + ":What is this, the Monty Hall Problem? ")
print1("Emperor: uhhh no, shut up")
print1(name + ": T-T")
print1("Emperor: Ahem! Now, in front of you are 3 doors!")
print1("Emperor: The first one leads to the TRIALS OF FIRE!!")
print1("Emperor: The second one leads to the TRIALS OF DISTAIN!!")
print1("Emperor: And finally, the third one leads to the TRIALS OF ICE!!")
print1("Emperor: (personally this one is my favorite)") #no biases but im just saying yknow
print1("Emperor: Although you don't really have any rights, I'll give you the liberty of choice!")
print1("Emperor: Which door do you want to choose? \n1. Trial of Fire \n2. Trial of Distain \n3. Trial of Ice")
while True: # Crime choice sequence
    print1 (name +": 'What crime did I commit again?' \n1. Murder \n2. Theft \n3. Attempts to overthrow the current political system through multistage conspiracy and bribery of government officials \n4. I'm not a criminal!") 
    choice = get_input("")
    if choice in ["1", "Murder"]:
        if game_state ["murder"] == False:
            print1(name + ": I... killed a man")
            print1("Emperor: Well! There you have it! They killed someone in cold blood!")
            print1(name + ": No, thats not what I mea-")
            print1("You're promptly cut off by the booing of the crowd")
            game_state["murder"] == True
            break

    elif choice in ["2", "Theft"]:
        if game_state ["theft"] == False:
            print1(name + ": I stole some bread so my family wouldn't starv-")
            print1("Emperor: I see! So you stole food from a poor vendor trying to make a living... How horrible!")
            print1(name + ": No, thats not what I mea-")
            print1("You're promptly cut off by the booing of the crowd")
            game_state["theft"] == True
            break

    elif choice in ["3", "Attempts to overthrow the current political system through multistage conspiracy and bribery of government officials"]:
        if game_state ["funny"] == False: #yeah im not checking the gamestate system to see if it works we'll suffer later XD
            print1(name +": Oh, uh, I tried to overthrow the current political system through multistag-... (wait what the hell no I didn't, who would even think of doing that??)")
            print1("Emperor: ...")
            print1("Emperor: I mean, uh, you wouldn't be the first, I guess?")
            print1("Emperor: But what did you REALLY do?")
            game_state["funny"] = True
            
        else: 
            print1(name +": 'No I didn't...'")

    elif choice in ["4", "I'm not a criminal!"]:
        if game_state ["pleading 1"] == False:
            print1(name  + ": I didn't do anything!")
            print1("Emperor: Well, you certainly did something, otherwise you wouldn't be here right now, so don't lie to us.")
            game_state["pleading 1"] = True
            
        else:
            print1(name  + ": uhhhhh I swear on the name of.... (wait I don't even remember their names)... anyway I swear on god I ain't do nothin'") 
            print1("Emperor: Fine then, keep your secrets")
            game_state["pleading 2"] = True
            break
# have the door closing text and clear happen before loading the chamber please and thank you
# pick your poison:
def chamber1(): # Flame
    while True:
        pass

def chamber2(): # Sewer
    while True:
        pass

def chamber3(): # Frost
    while True:
        pass
