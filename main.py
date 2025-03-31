#Hi Mr. Nagra its us your favorite comp sci students!!
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

board = [
        ["X", "X", "O"],
        [" ", "X", "O"],
        [" ", "O", "X"]
    ]


def print_board(board):
    for i, row in enumerate(board):
        print(" " + " | ".join(row))
        if i < 2:
            print("═══╬═══╬═══")

game_state = { #our game updates
    "murder":False,
    "theft":False,
    "funny":False,
    "pleading 1":False,
    "pleading 2":False,
    "check_board":False,
    "wrong_tile":False,
    "wrong_tile_1-1":False,
    "wrong_tile_1-2":False,
    "wrong_tile_2-1":False,
    "wrong_tile_2-2":False,
    "wrong_tile_3":False,
    "randombutton":False,
    "cube_east":False,
    "cube_west":False,
    "cube_south":False,
    "attempted_sacrifice":False,
    "checked_door":False,

}

#Ok so ignore the autism that is player hp being an argument for everything, uh was struggling with globals and just decided to screw it and slap a bandaid on the code lmao

def get_input(prompt=""): # Yeah this is 100% irrelevant rn but it might be useful later
    choice = input(prompt).strip().lower()# you know you love it .strip().lower() .strip mean basically remove any spaces in our choice and .lower makes everything lowercase
    return choice  # Return the actual input otherwise

# have the door closing text and clear happen before loading the chamber please and thank you
# pick your poison:
def FirePuzzle1(player_HP):
    while True:
        player_bar = player_HP // 10
        health_bar2 = '█' * player_bar #player bar
        empty_space2 = ' ' * (10 - player_bar)
        print(f"\rplayer HP: [{health_bar2}{empty_space2}] {player_HP}", end='', flush=True)
        print1(" " +name + ": 'How should I go about this?' \n1. Step on the first tile\n2. Step on the second tile\n3. Step on the third tile\n4. Observe your surroundings")
        choice = get_input("")
        
        if choice in ["1", "First" "Step on the first tile"]: 
            if game_state["wrong_tile_1-1"] == False:
                print1("As you step onto the first tile, you feel the ground underneath you sink in, as a pillar of fire erupts from your current location")
                if evasion == 2: 
                    print1("You barely manage to stumble back to where you started, lucky you!")
                else:
                    print1("You burn your leg badly as you stumble back to where you started. Ouch.")
                    player_HP -= 20
                if game_state["wrong_tile"] == False:
                    print1(name+": JESUS CHRIS- oh wait wrong religion uhhhh ouch owie owww ):")
                    game_state["wrong_tile_1-1"] = True
                    game_state["wrong_tile"] = True
                    
                else: 
                    print1(name+": 'Damn... Again?'")
                    game_state["wrong_tile_1-1"] = True

            else: print1(name+": I'm not stepping on that tile again...")
            
        if choice in ["3", "Third" "Step on the third tile"]: #
            if game_state["wrong_tile_1-2"] == False:
                print1("As you step onto the third tile, you feel the ground underneath you sink in, as a pillar of fire erupts from your current location")
                if evasion == 2: 
                    print1("You barely manage to stumble back to where you started, lucky you!")

                else:
                    print1("You burn your leg badly as you stumble back to where you started. Ouch.")
                    player_HP -= 20

                if game_state["wrong_tile"] == False:
                    print1(name+": JESUS CHRIS- oh wait wrong religion uhhhh ouch owie owww ):")
                    game_state["wrong_tile_1-2"] = True
                    game_state["wrong_tile"] = True
                else: 
                    print1(name+": 'Damn... Again?'")
                    game_state["wrong_tile_1-2"] = True
            else: print1(name+": I'm not stepping on that tile again...")

        if choice in ["2", "Second" "Step on the second tile"]: #
            print1("As you step onto the second tile, you feel... nothing?")
            if game_state["wrong_tile"] == True: print1(name+": So it's this tile...")
            else: print1(name+": That's... strange")
            FirePuzzle2(player_HP)
            break #idk if this is needed but just incase yknow

        if choice in ["4", "Observe" "Observe your surroundings"]: #
            if game_state["check_board"] == False:
                print1("You look around the walls of the cavern, you notice various different carvings in the walls")
                print1("Notably, one of them resembles something you recognize, a game of Tic-Tac-Toe")
                print_board(board)
                print()
                print1(name+": Huh, maybe they got bored?")
                game_state["check_board"] = True
            else:
                print_board(board)
                print()
                print1(name+": Does this... mean something?")

def FirePuzzle2(player_HP):
    print1("Well, you managed to step on the right tile, but theres 2 more sets in front of you. Good luck!")
    while True:
        player_bar = player_HP // 10
        health_bar2 = '█' * player_bar #player bar
        empty_space2 = ' ' * (10 - player_bar)
        print(f"\rplayer HP: [{health_bar2}{empty_space2}] {player_HP}", end='', flush=True)
        print1(" " +name + ": 'How should I go about this?' \n1. Step on the first tile\n2. Step on the second tile\n3. Step on the third tile\n4. Observe your surroundings")
        choice = get_input("")
        
        if choice in ["1", "First" "Step on the first tile"]: 
            if game_state["wrong_tile_2-1"] == False:
                print1("As you step onto the first tile, you feel the ground underneath you sink in, as a pillar of fire erupts from your current location")
                if evasion == 2: 
                    print1("You barely manage to stumble back to where you started, lucky you!")
                else:
                    print1("You burn your leg badly as you stumble back to where you started. Ouch.")
                    player_HP -= 20
                if game_state["wrong_tile"] == False:
                    print1(name+": JESUS CHRIS- oh wait wrong religion uhhhh ouch owie owww ):")
                    game_state["wrong_tile_2-1"] = True
                    game_state["wrong_tile"] = True
                    
                else: 
                    print1(name+": 'Damn... Again?'")
                    game_state["wrong_tile_2-1"] = True

            else: print1(name+": I'm not stepping on that tile again...")
            
        if choice in ["2", "Second" "Step on the second tile"]: #
            if game_state["wrong_tile_2-2"] == False:
                print1("As you step onto the second tile, you feel the ground underneath you sink in, as a pillar of fire erupts from your current location")
                if evasion == 2: 
                    print1("You barely manage to stumble back to where you started, lucky you!")

                else:
                    print1("You burn your leg badly as you stumble back to where you started. Ouch.")
                    player_HP -= 20

                if game_state["wrong_tile"] == False:
                    print1(name+": JESUS CHRIS- oh wait wrong religion uhhhh ouch owie owww ):")
                    game_state["wrong_tile_2-2"] = True
                    game_state["wrong_tile"] = True
                else: 
                    print1(name+": 'Damn... Again?'")
                    game_state["wrong_tile_2-2"] = True
            else: print1(name+": I'm not stepping on that tile again...")

        if choice in ["3", "Third" "Step on the third tile"]: #
            print1("As you step onto the third tile, you feel... nothing?")
            if game_state["wrong_tile"] == True: print1(name+": It's number 3 this time")
            else: print1(name+": Do these tiles even do anything?")
            FirePuzzle3(player_HP)
            break #idk if this is needed but just incase yknow

        if choice in ["4", "Observe" "Observe your surroundings"]: #
            if game_state["check_board"] == False:
                print1("You look around the walls of the cavern, you notice various different carvings in the walls")
                print1("Notably, one of them resembles something you recognize, a game of Tic-Tac-Toe")
                print_board(board)
                print()
                print1(name+": Huh, maybe they got bored?")
                game_state["check_board"] = True
            else:
                print_board(board)
                print()
                print1(name+": Does this... mean something?")
        
def FirePuzzle3(player_HP):
    print1("That's another one down, and one more to go")
    while True:
        player_bar = player_HP // 10
        health_bar2 = '█' * player_bar #player bar
        empty_space2 = ' ' * (10 - player_bar)
        print(f"\rplayer HP: [{health_bar2}{empty_space2}] {player_HP}", end='', flush=True)
        print1(" " +name + ": 'How should I go about this?' \n1. Step on the second tile\n2. Step on the third tile\n3. Observe your surroundings")
        choice = get_input("")
        
        if choice in ["1", "Second" "Step on the second tile"]: 
            if game_state["wrong_tile_3"] == False:
                print1("As you step onto the second tile, you feel the ground underneath you sink in, as a pillar of fire erupts from your current location")
                if evasion == 2: 
                    print1("You barely manage to stumble back to where you started, lucky you!")
                else:
                    print1("You burn your leg badly as you stumble back to where you started. Ouch.")
                    player_HP -= 20
                if game_state["wrong_tile"] == False:
                    print1(name+": JESUS CHRIS- oh wait wrong religion uhhhh ouch owie owww ):")
                    game_state["wrong_tile_3"] = True
                    game_state["wrong_tile"] = True
                    
                else: 
                    print1(name+": 'Damn... Again?'")
                    game_state["wrong_tile_3"] = True

            else: print1(name+": I'm not stepping on that tile again...")
            
        if choice in ["2", "Third" "Step on the third tile"]: #
            print1("As you step onto the third tile, you feel nothing again")
            if game_state["wrong_tile"] == True: print1(name+": It's number 3 again...")
            else: print1(name+": Huh, that was suprisingly easy!")
            break

        if choice in ["3", "Observe" "Observe your surroundings"]: #
            if game_state["check_board"] == False:
                print1("You look around the walls of the cavern, you notice various different carvings in the walls")
                print1("Notably, one of them resembles something you recognize, a game of Tic-Tac-Toe")
                print_board(board)
                print()
                print1(name+": Huh, maybe they got bored?")
                game_state["check_board"] = True
            else:
                print_board(board)
                print()
                print1(name+": Does this... mean something?")
            
def Fire(player_HP): # Flame <--- this is the equivalent of our folder of code ig basically when we called to it it'll basically open up this entire folder and run it line by line
    #ok sick so now we gotta add chamber specific traps - 3x3 tile, the order is 2, 3, 3
    print1("Walking through the fiery hall in front of you leads to a room with a square, checkered floor")
    print1("You're greeted by a 3x3 set of tiles, and across from it is, well, more hallway...")
    print1(name + ": Well, I guess it's a trial for a reason")
    FirePuzzle1(player_HP)
     
    print1("As you continue walking through the blazing heat of the hallway, you come across a split path")
    print1(name + ": Yeah, what did I expect...")
    while True:
        print1 (name +": 'Which path should I go down?' \n1. The first path\n2. The second path\n3. Maybe I should explore a bit more..")
        choice = get_input("")
        if choice in ["1", "First" "The first path"]:
            clear()
            pass
        elif choice in ["2", "Second" "The second path"]:
            clear()
            pass
        elif choice in ["3", "Explore" "Maybe I should explore a bit more"]:
            clear()
            pass

def Distain(player_HP): # Sewer
    print1("As you walk through the seemingly normal hallway, you come across a split path")
    print1(name + ": Yeah, what did I expect...")
    while True:
        print1 (name +": 'Which path should I go down?' \n1. The first path\n2. The second path\n3. Maybe I should explore a bit more..")
        choice = get_input("")
        if choice in ["1", "First" "The first path"]:
            clear()
            pass
        elif choice in ["2", "Second" "The second path"]:
            clear()
            pass
        elif choice in ["3", "Explore" "Maybe I should explore a bit more"]:
            clear()
            pass

def EastWall(player_HP):
    while True:
        player_HP -= 5
        player_bar = player_HP // 10
        health_bar2 = '█' * player_bar #player bar
        empty_space2 = ' ' * (10 - player_bar)
        print(f"\rplayer HP: [{health_bar2}{empty_space2}] {player_HP}", end='', flush=True)
        print1(" "+name+": 'Awesome! What now...' \n1. Press a random button\n2. Press all 3 buttons \n3. Just slash the ice and take it")
        choice = get_input("")
        if choice in ["1", "Press a random button"]:
            print1("You press a random button, and nothing happens")
            print1(name+": Hm. What if...")
            print1("You press another, different button, and nothing happens")
            print1(name+": Okkk...")
            print1("You press the last, other button, and nothing happens. Again")
            print1(name+": Wait, WHAT?")
            if game_state ["randombutton"] == True:
                print1("What, did you just expect it to work if you did tried it again? Have you heard of textbook insanity?")
            else:game_state ["randombutton"] = True
        elif choice in ["2", "Press all 3 buttons"]:
            if game_state ["randombutton"] == False:
                print1("You just... wait hold on did you just press all 3 of them at the same time??")
                print1("Ok... You press all 3 of the buttons at the same time andddd...")
                print2("...")
                print1("Nothing happens.")
                print1(name+": Man, I really thought that would work...")
                print1("...Why?")
            else:
                print1("You just... wait hold on did you just press all 3 of them at the same time??")
                print1("Yeah I'm... not suprised at this point")
                print1("Well...")
                print1("Nothing happens.")
                print1(name+": Man, I really thought that would work...")
                print1("...Why?")
        elif choice in ["3", "Just slash the ice and take it"]:
            print1("You raise up your sword and just cut down the ice, expertly avoiding the pristine cube in the middle") # Holy glaze
            if game_state ["randombutton"] == True: print1("Honestly this feels more reasonable then just pressing random buttons")
            print1("The ice shatters and the cube rolls to your feet. Good job!")
            print1(name+": Huh, nice.")
            game_state ["cube_east"] = True
            break

def WestWall(player_HP):
    while True:
        player_HP -= 5
        player_bar = player_HP // 10
        health_bar2 = '█' * player_bar #player bar
        empty_space2 = ' ' * (10 - player_bar)
        print(f"\rplayer HP: [{health_bar2}{empty_space2}] {player_HP}", end='', flush=True)
        print1(" "+name+": 'What does this mural want me to do?' \n1. Start worshipping the cube\n2.  Sacrifice yourself to the cube\n3. Smash the mural and take the cube")
        choice = get_input("")
        if choice in ["1", "Worship", "Start worshipping the cube"]:
            print1("You... You get down on your knees and start worshipping the cube, prayers and everything")
            print1("This is, genuienly the funniest thing I have ever seen, in my entire life")
            print1("And I'm like, immortal or something")
            print1("Anyway, as you start bowing down before (pfft).. before a cube (lmao), the mural opens up and reveals the bloodstained cube to you")
            print1(name+": Thanks cube god")
            print1("Who?")
            print1("Cube God: You're welcome homie")
            print2("...")
            print1("What...")
            print1("Yknow on second thought I don't get paid enough to think") # Literally self-insert
            print1("Anyway, theres your cube")
            game_state ["cube_west"] = True
            break
        elif choice in ["2", "Sacrifice", "Sacrifice yourself to the cube"]:
            if game_state ["attempted_sacrifice"] == False:
                print1("As you raise your sword up to stab yourse- wait... WHAT?? my brother in christ...")
                print1("HOW IS THAT THE MESSAGE YOU GOT FROM THE MURAL??")
                print1("Actually I'm not gonna stop you, go for it.")
                print1("You raise your sword up and stab a hole through most of your vital organs ")
                print1("The cube god smiles upon you")
                print2("...")
                print1("Wait what")
                print1("Your wound heals, and the room feels a bit warmer")
                print1("This... yeah, yeah I give up")
                print1(name+": Oh nice! I actually survived!")
                print1("Did you not expect to?? Just, just go...")
                game_state["attempted_sacrifice"] = True
            else: 
                print2("NO")
                print1("Don't do that again...")
                player_HP += 5
        elif choice in ["3", "Smash", "Smash the mural and take the cube"]:
            print1("You attempt to smash the mural")
            print1("Your sword bounces off with a resounding thud")
            print1("The cube god frowns upon you")

def IcePuzzle(player_HP):
    print1("You feel the frigid cold ramp up as the light goes out")
    print1("Suprisingly, there's still a bit of light left, just enough to see")
    print1(name+": This cold reaally hurts, I won't lie")
    print2("...")
    print1(name+": I wont get hypothermia right?")
    print1("uhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh yeah uh huh for sure (foreshadowing.jpg)")
    clear()
    while True:
        print1("The cold grows, uh, colder... as you feel the effects of frostbite get ever so stronger")
        player_HP -= 5
        player_bar = player_HP // 10
        health_bar2 = '█' * player_bar #player bar
        empty_space2 = ' ' * (10 - player_bar)
        print(f"\rplayer HP: [{health_bar2}{empty_space2}] {player_HP}", end='', flush=True)
        print1(" "+name+": 'What should I do now?' \n1. Check the northern wall\n2. Check the eastern wall\n3.Check the southern wall\n4.Check the western wall")
        choice = get_input("")
        if choice in ["1", "North", "Check the northern wall"]:
            if game_state ["cube_east"] == True and game_state ["cube_west"] == True and game_state ["cube_south"] == True and game_state ["checked_door"] == True: # the == true on all of them is most likely redundant but who cares its 2am
                print1("You place all 3 of the cubes into the slot in the door")
                print1("Unsuprisingly, it opens up")
                print1("The air ahead is MUCH warmer than in that icebox")
                print1(name+": Finally... out of the cold")
                break
            else:
                print1("You walk up to the northern wall, and find a door with 3 cubes carved out of it")
                print1("The door has a sign that reads: -- ---- --- ----- ---")
                print1(name+": ...What?")
                print1("Oh, uh, right, you can't read...")
                print2("...")
                print1(name+": Very helpful")
                game_state["checked_door"] = True
        elif choice in ["2", "East", "Check the eastern wall"]:
            if game_state ["cube_east"] == False:
                print1("You slide up to the eastern wall, and find a cool looking cube encased in ice")
                print1("Under the cube reads: --- ---- ---- ----, with 3 buttons underneath")
                print2("...")
                print1("You should've worked on your reading comprehension before going to jail...")
                print1("Would you like to investigate the encased cube? \n1. Yes \n2. No")
                if choice in ["1", "Yes"]:
                    player_HP += 5
                    EastWall(player_HP)
                else: 
                    print1(name+": I'll check this out later")
                    print1("You return to the center of the room")
            else: print1(name+": I don't think I need anything else from the eastern wall")
        elif choice in ["3", "South", "Check the southern wall"]:
            if game_state ["cube_south"] == False:
                print1("You shimmy back over to the south wall, where you entered the room from, when you notice something shiny on the floor")
                print1(name+": Is that a convieniently placed cube directly at the entrance so that the person who made this chamber doesn't have to think about creating a real puzzle for this?")
                print2("...") # Look I was tired and I'm not really known for being creative ok :(
                print1("That was... incredibly accurate... kind of scary actually...")
                print1("Anyway! you've found a cube!")
                game_state ["cube_south"] = True
            else: print1(name+": I don't think I need anything else from the southern wall")
        elif choice in ["4", "West", "Check the western wall"]:
            if game_state ["cube_west"] == False:
                print1("You shuffle over to the west wall, where you see a mural placed in clear view... well... however clear this dark room is")
                print1("Would you like to investigate the mural cube? \n1. Yes \n2. No")
                if choice in ["1", "Yes"]:
                    print1("The mural shows a diagram of 4 people worshipping a cube. The next panel shows the cube, uh, (wait am I seeing this right)")
                    print1("Ahem, the next mural shows 3 of those people being sacrificed to the cube. Brutally. In fact, this would probably be rated M if there were visuals")
                    print1(name+": oh that's, that's gore...")# HE SAID IT HE SAID THE THING OH MY GOD
                    print1("The last panel has a mirror, along with the cube that was being worshipped.")
                    player_HP += 5
                    WestWall(player_HP)
                else: 
                    print1(name+": I'll check this out later")
                    print1("You return to the center of the room")
            else: print1(name+": I don't think I need anything else from the western wall")

def Ice(player_HP): # Frost
    print1("Walking through the blistering winds in front of you, you find a room with a campfire and torches, somehow unextinguished")
    print1("It feels... warm")
    print1(name + ": 'Should I go in?' \n1. Go in the room \n2. Stay in the hallway")
    choice = get_input("")
    if choice in ["1", "Go in the room", "Room"]:
        print1(name + ": That's a nice break...")
        print2("...")
        print1(name+": ...Wait a minute")
        print1("As you come to realize that theres no way a 'trial' would have a room for a break, the path you took quickly closes itself off to you")
        print1("Just as you turn to look at it, the campfire and torches extinguish simultaneously")
    elif choice in ["2", "Stay in the hallway", "Stay"]:
        print1(name + ": There's no way this isn't a trap")
        print2("...")
        print1("And you're right about that. But we've got to progress somehow, right?") # Railroading isn't real you made that up
        print1("You quickly notice the walls closing in around you, as the room in front of you becomes your way of escape")
        print1(name + ": ...I expected as much")
        print1("The pathway you took closes, and you notice the torches and campfire extinguish simultaneously")
    print1(name+": Damn it...")
    IcePuzzle(player_HP)
    
    print1("Oh, it's still really cold though")
    print2("...")
    print1("As you continue walking through the freezing cold of the hallway, you come across a split path")
    print1(name + ": Yeah, what did I expect...")
    while True:
        print1 (name +": 'Which path should I go down?' \n1. The first path\n2. The second path\n3. Maybe I should explore a bit more..")
        choice = get_input("")
        if choice in ["1", "First" "The first path"]:
            clear()
            pass
        elif choice in ["2", "Second" "The second path"]:
            clear()
            pass
        elif choice in ["3", "Explore" "Maybe I should explore a bit more"]:
            clear()
            pass


#opening sequenceeee
player_HP = 100
print1 ("You start hearing cheers and yells coming from all around you")
print1 ("Press enter to wake up")
input()
clear()#I stole this from Ivan but I can explain it
for i in range(3):#this loops are three dots a total of three times
    for j in range(4): #this basically puts our dots in it starts at 0 and goes up to three because python with its funny numbers
        print (j*(".")) #for every number in J for example 0 1 2 3 it will multiply it by the amount of dots so for example right now it will be 1 * 0 = 0 1 * 1 = 1
        time.sleep(0.1) #delays out text
        clear()
time.sleep(1.5)
print1("You force yourself up from the sand reluctantly")
print1("--: 'Wait, who even am I?'") # This one is not a subsitute
name = input("Who are you?: ")
print1(name +": Oh, right, I'm " + name) #-his name is canonically dave. like, all lowercase.
print1("You look around to find yourself in a sort of, arena?")
print1("Before you can think of your surroudings, you hear the ringing of a bell, and the sounds of cheers get quieter...") # queue mizu5
print1("You look up to see the Emperor sitting on his throne, all eyes on him") #yall i cant write for shit
print1("The Emperor shouts,")
print1("Emperor: TODAY, EVERYONE WILL WATCH THE TRIALS OF AMENDMENT, FOR THE HEINOUS CRIMES OF... wait, hold on, oh right THE CRIMES OF " + name.upper()) #makes it uppercase the opposite of .lower
print1("Random Audience Member: ...What did they even do though?")
print2("...")
print1("The Emperor prompts one of the guards, and he beheads him immediately") #L bozo
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
            clear()
            print1(name  + ": I didn't do anything!")
            print1("Emperor: Well, you certainly did something, otherwise you wouldn't be here right now, so don't lie to us.")
            game_state["pleading 1"] = True
            
        else:
            print1(name  + ": uhhhhh I swear on the name of.... (wait I don't even remember their names)... anyway I swear on god I ain't do nothin'") 
            print1("Emperor: Fine then, keep your secrets")
            game_state["pleading 2"] = True
            break
# Murder = Damage, Theft = Evasion, Pleading(2) = Charisma
# roll variable out of 4
damage = 0
if game_state ["murder"] == True:
    damage += 21
evasion = 1
if game_state ["theft"] == True:
    evasion += 1
charisma = 1
if game_state ["pleading 2"] == True:
    charisma += 1

print1("Emperor: Well, onto the TRIALS OF AMENDMENT!!")
print1(name + ": 'The... what?'")
print1("Emperor: Now! In front of you are 3 doors!")
print1(name + ": What is this, the Monty Hall Problem? ")
print1("Emperor: uhhh no, shut up")
print1(name + ": T-T")
print1("Emperor: Ahem! Now, in front of you are 3 doors!")
print1("Emperor: The first one leads to the TRIALS OF FIRE!!")
print1("Emperor: The second one leads to the TRIALS OF DISTAIN!!")
print1("Emperor: And finally, the third one leads to the TRIALS OF ICE!!")
 #no biases but im just saying yknow the ice door is the goat
print1("Emperor: Although you don't really have any rights, I'll give you the liberty of choice!")
while True: # Door choice sequence
    print1("Emperor: Which door do you want to choose? \n1. Trial of Fire \n2. Trial of Distain \n3. Trial of Ice")
    choice = get_input("")
    if choice in ["1", "Fire", "Trial of Fire"]:
        clear()
        print1(name + ": I choose... the first door")
        print1("Emperor: Oh come on, say it with enthusiasm! This is a joyous occasion!")
        print1(name + ": fine... I choose The Trial of Fire!")
        print1("Emperor: Then go on, criminal!")
        print1("As you walk through the door of the chamber, the cheers quiet down...")
        print1("It's hot. Go figure")
        print1(name + ": 'Finally, it's quiet...'")
        print1("And then the door slams shut, directly behind you")
        print1(name + ": HOLY SH-")
        print1("Family friendly game, brother")
        print1(name + ": Oh. My bad")
        print2("...")
        print1(name + ": Wait, who am I talking to?")
        Fire(player_HP)
    elif choice in ["2", "Distain", "Trial of Distain"]:
        clear()
        print1(name + ": I choose... the second door")
        print1("Emperor: Oh... the Trial of Distain, huh...")
        print1("Emperor: Well then, go on criminal")
        print1("As you walk through the door of the chamber, the cheers quiet down...")
        print1(name + ": 'Finally, it's quiet...'")
        print1("And then the door slowly melds into place behind you")
        print1(name + ": ...What the f-")
        print1("Family friendly game, brother")
        print1(name + ": Oh. My bad")
        print2("...")
        print1(name + ": Wait, who am I talking to?")
        Distain(player_HP)
    elif choice in ["3", "Ice", "Trial of Ice"]:
        clear()
        print1(name + ": I choose... the third door")
        print1("Emperor: Say it's name.")
        print1(name + ": fine... I choose The Trial of Ice...")
        print1("Emperor: Then go, criminal")
        print1("As you walk through the door of the chamber, the cheers quiet down...")
        print1("It's cold. Go figure")
        print1(name + ": 'Finally, it's quiet...'")
        print1(name + ": 'and also freezing':/")
        print1("And then the door slowly slides into place")
        print1(name + ": Oh, that's... that's nice")
        Ice(player_HP)