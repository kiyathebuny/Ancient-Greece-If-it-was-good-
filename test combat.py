#Hi Mr. Nagra its me your favorite comp sci student
import time# time.time() method of Time module is used to get the time in seconds
import sys#The sys module provides access to system-specific parameters and functions in Python. 
#It allows you to interact with the Python interpreter and access command-line arguments
from collections import Counter #counter is the number counter and collections
import random #this is for random number generator 
import os
#Hi Mr.Nagra it's time for 2000 lines of code again

def clear(): #this is our clear function it clear our terminal
    if(os.name == "nt"):
        os.system("cls") #here is for our very cool windows users
    else:
        os.system("clear") #this is for people who overpaid on Apple laptops

def print1(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush() #this two line input and prints each character one by one
        time.sleep(0.045) #our typing delay
    print()#for spacing

def print2(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.5)
    print()

def get_input(prompt=""): # Yeah this is 100% irrelevant rn but it might be useful later
    choice = input(prompt).strip().lower()# you know you love it .strip().lower() .strip mean basically remove any spaces in our choice and .lower makes everything lowercase
    return choice  # Return the actual input otherwise

name = ("dave")
enemy_HP = 100
player_HP = 100
damage = 10
evasion = 10
charisma = 10

print1 ("Press enter to wake up")
input()
clear()#I stole this from Ivan but I can explain it
for i in range(3):#this loops are three dots a total of three times
    for j in range(4): #this basically puts our dots in it starts at 0 and goes up to three because python with its funny numbers
        print (j*(".")) #for every number in J for example 0 1 2 3 it will multiply it by the amount of dots so for example right now it will be 1 * 0 = 0 1 * 1 = 1
        time.sleep(0.1) #delays out text
        clear()
time.sleep(1.5)
print1 ("as you're about to enter the next room you come across a very tall Dragon like creature with fire on its tail and with orange scales")
print1 (name + (": this is just a Pokémon..."))
print1 ("you find urself with a Sprigatito")
print1 ("you are about to start combat")
while enemy_HP > 0:
    #enemy bar
    enemy_bar = enemy_HP // 10
    health_bar1 = '█' * enemy_bar
    empty_space1 = ' ' * (10 - enemy_bar)
    #player bar
    player_bar = player_HP // 10
    health_bar2 = '█' * player_bar
    empty_space2 = ' ' * (10 - player_bar)

    print(f"\rEnemy HP: [{health_bar1}{empty_space1}] {enemy_HP}", end='', flush=True)
    print1("")
    print1("")
    print(f"\rplayer HP: [{health_bar2}{empty_space2}] {player_HP}", end='', flush=True)
    print("")

    if enemy_HP <= 0:
        break

    print ("what would you like to do:"),
    choice = get_input("")
    if choice in ["1" , "yes"]:
        enemy_HP = max(0, enemy_HP - damage)  # Prevent negative HP during loop
        clear()
        print1 (f"You deal {damage} damage!")

    else:
        print1 ("you heal")
        clear()

    if enemy_HP <= 0:
        break
        
    time.sleep(0.5)
print(f"\rEnemy HP: [          ] 0", end='', flush=True)