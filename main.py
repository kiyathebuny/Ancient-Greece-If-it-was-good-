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
        time.sleep(0.005) #our typing delay 
    print()#for spacing

def print2(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.5)
    print()

def print3(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.3)

def print4(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush() #this two line input and prints each character one by one
        time.sleep(0.045) #our typing delay



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
    "bridge_investigation":False,
    "room_investigation":False,
    "infernal_knight":False,
    "totem":False,
    "lich":False,
    "ghost":False,

}

player_HP = 100
enemy_HP = 0
damage = 0
evasion = 0
enemy_miss_chance = 10 # change later
player_miss_chance = 10
attack_name_1 = "Attack 1"
attack_name_2 = "Attack 2"
attack_name_3 = "Attack 3"

def get_input(prompt=""): # Yeah this is 100% irrelevant rn but it might be useful later
    choice = input(prompt).strip().lower()# you know you love it .strip().lower() .strip mean basically remove any spaces in our choice and .lower makes everything lowercase
    return choice  # Return the actual input otherwise

def fighting():
    global enemy_HP, player_miss_chance, player_HP
    max_HP = 100
    counter = 0
    attack_1 = 0
    attack_2 = 0
    heal = 0
    shuffle_counter = 0
    talk = 0

    def enemy_attack_type():
        global player_HP, enemy_HP, evasion, enemy_miss_chance, freeze
        enemy_attack = random.randint(1 , enemy_miss_chance)
        if enemy_HP > 0:
            if game_state["ghost"] == True:
                print1("The ghost quietly weeps in the corner")
            elif 0 <= enemy_attack <= 2:
                print1("The enemies attack bounced off your shield!")

            elif evasion >= 2 and 0 <= enemy_attack <= 3:
                print1("You dodged the enemies attack!")
                
            else:
                enemy_attack_type = random.randint(1,10)
                if 0 <= enemy_attack_type <= 5:
                    enemy_dmg = random.randint(15, 20)
                    print1 (f"The Enemy used {attack_name_1}")
                    player_HP = max(0, player_HP - enemy_dmg)
                    clear()
                    print1(f"The enemy strikes you for {enemy_dmg} damage!")
                    return

                elif 6 <= enemy_attack_type <= 9:
                    enemy_dmg = random.randint(15, 25)
                    print1 (f"The Enemy used {attack_name_2}")
                    player_HP = max(0, player_HP - enemy_dmg)
                    clear()
                    print1(f"The enemy strikes you for {enemy_dmg} damage!")
                    return

                elif enemy_attack_type == 10:
                    enemy_dmg = random.randint(25, 30)
                    print1 (f"The Enemy used {attack_name_3}")
                    player_HP = max(0, player_HP - enemy_dmg)
                    clear()
                    print1(f"The enemy strikes you for {enemy_dmg} damage!")
                    return

    while enemy_HP > 0:
        #enemy bar
        enemy_bar = enemy_HP // 10
        health_bar1 = '█' * enemy_bar
        empty_space1 = ' ' * (10 - enemy_bar)
        #player bar
        player_bar = player_HP // 10
        health_bar2 = '█' * player_bar
        empty_space2 = ' ' * (10 - player_bar)
        counter += 1
        print(f"[Slash: {attack_1}/3 | Stab: {attack_2}/4 | Talk: N/A]")
        print(f"\rEnemies HP:[{health_bar1}{empty_space1}] {enemy_HP}", end='', flush=True)
        print("")
        print(f"\rPlayers HP:[{health_bar2}{empty_space2}] {player_HP}", end='', flush=True)
        print("")

        if enemy_HP <= 0 or player_HP <= 0:
            break
        

        if game_state["cube_south"]: print1 ("What would you like to do: \n1. Slash \n2. Stab \n3. Talk \n4. Slide forwards")
        elif (game_state["lich"] == True): print1("You're frozen by the lich!")
        else:print1 ("What would you like to do: \n1. Slash \n2. Stab \n3. Talk"),
        choice = get_input("")
        if choice in ["1" , " slash"]:
            damage_rate = random.randint(15 , 30) + damage
            clear()
            player_attack = random.randint(1 , player_miss_chance)
            if 0 <= player_attack <= 2:
                enemy_attack_type()
                print1("Your attack missed!")
                counter -= 1
            elif attack_1 >= 3 and 0 <= player_attack <= 9:
                enemy_attack_type()
                print1("Your attack missed!")
            else:
                attack_1 += 1
                enemy_HP = max(0, enemy_HP - damage_rate)
                enemy_attack_type()
                print1(f"You deal {damage_rate} damage!")

        elif choice in [f"2" , "stab"]:
            damage_rate = random.randint(10, 20) + damage
            clear()
            player_attack = random.randint(1 , player_miss_chance)
            if 0 <= player_attack <= 2:
                enemy_attack_type()
                print1("Your attack missed!")
                counter -= 1
            
            elif attack_2 >= 4 and 0 <= player_attack <= 9:
                enemy_attack_type()
                print1("Your attack missed!")

            else:
                attack_2 += 1
                enemy_HP = max(0, enemy_HP - damage_rate)
                enemy_attack_type()
                print1(f"You deal {damage_rate} damage!")


        elif choice in ["3" , "talk"]:
            if game_state["ghost"] == False:
                heal = random.randint(15, 25)
                player_HP = min(max_HP, player_HP + heal)
                clear()
                enemy_attack_type()
                print1("You attempt to talk to the entity")
                if game_state["lich"]: print1("It responds with an unintelligble shriek. Although you can't tell what it said, you can assume they were some kind words")
                if game_state["infernal_knight"]: print1("It points its sword at you as its flames burn brigher. You feel fired up!")
                else:print1("Although it doesn't respond, you feel invigorated") # I can spell i swear T-T
                print1(f"You heal {heal} HP!")
                counter -= 1
            else:
                print1("You attempt to talk to the ghost")
                if talk == 0:
                    print1(name+"Hey, uh, is everything alright")
                    print1("??????: Everyone keeps forgetting who I am...")
                    print2(name+": Oh, thats rough buddy")
                    talk += 1
                elif talk == 1:
                    print1("??????: Why does no one want to play to me...")
                    print4("They're all")
                    print3("...")
                    print1("afraid")
                    print2(name+": But why?")
                    talk += 1
                elif talk == 2:
                    print1("??????: My sister is always busy, she never has time for me")
                    print1(name+": Maybe she's earning money for your family?")
                    print1("??????: ...")
                    talk += 1
                elif talk == 3:
                    print("??????: ...")
                    print1(name+": Do you... want to talk about it?")
                    print("??????: ...Really?")
                    print1(name+": Uh, yeah!")
                    print("??????: Aren't you... afraid of me?")
                    print1(name+": No? Why would I be?")
                    talk += 1
                elif talk == 4:
                    print("??????: ...Thank you..")
                    print(name+": You're... welcome?")
                    print("??????: It was a pleasure to meet you") # Try not to incorperate koishi reference challenge impossible
                    print(name+": Oh, um, thanks")
                    break
                    

        elif choice in ["4" , "shuffle"]:
            if game_state["cube_south"] == True:
                clear()
                print("You shuffle ever so closer to the enemy")
                shuffle_counter += 1
            else: continue

        else:
            counter -= 1
            clear()
        
        if counter == 5:
            counter *= 0
            attack_1 *= 0
            attack_2 *= 0

        if shuffle_counter >= 5:
            print1("You enter melee range of the totem")
            player_miss_chance = 100

        if enemy_HP <= 0 or player_HP <= 0:
            attack_1 *= 0
            attack_2 *= 0
            counter *= 0
            time.sleep(0.5)
            print(f"\rEnemies HP: [{health_bar1}{empty_space1}] {enemy_HP}", end='', flush=True)
            print("")
            print(f"\rPlayers HP: [{health_bar2}{empty_space2}] {player_HP}", end='', flush=True)
            print("")
            break

# have the door closing text and clear happen before loading the chamber please and thank you
# pick your poison:
def FirePuzzle1():
    global player_HP
    while True:
        player_bar = player_HP // 10
        health_bar2 = '█' * player_bar #player bar
        empty_space2 = ' ' * (10 - player_bar)
        print(f"\rplayer HP: [{health_bar2}{empty_space2}] {player_HP}", end='', flush=True)
        print()
        print1(name + ": 'How should I go about this?' \n1. Step on the first tile\n2. Step on the second tile\n3. Step on the third tile\n4. Observe your surroundings")
        choice = get_input("")
        
        if choice in ["1", "first" "step on the first tile"]: 
            if game_state["wrong_tile_1-1"] == False:
                print1("As you step onto the first tile, you feel the ground underneath you sink in, as a pillar of fire erupts from your current location")
                if evasion == 2: 
                    print1("You barely manage to stumble back to where you started, lucky you!")
                else:
                    print1("You burn your leg badly as you stumble back to where you started. Ouch.")
                    player_HP -= 34
                if game_state["wrong_tile"] == False:
                    print1(name+": JESUS CHRIS- oh wait wrong religion uhhhh ouch owie owww ):")
                    game_state["wrong_tile_1-1"] = True
                    game_state["wrong_tile"] = True
                    
                else: 
                    print1(name+": 'Damn... Again?'")
                    game_state["wrong_tile_1-1"] = True

            else: print1(name+": I'm not stepping on that tile again...")
            
        if choice in ["3", "third" "step on the third tile"]: 
            if game_state["wrong_tile_1-2"] == False:
                print1("As you step onto the third tile, you feel the ground underneath you sink in, as a pillar of fire erupts from your current location")
                if evasion == 2: 
                    print1("You barely manage to stumble back to where you started, lucky you!")

                else:
                    print1("You burn your leg badly as you stumble back to where you started. Ouch.")
                    player_HP -= 34

                if game_state["wrong_tile"] == False:
                    print1(name+": JESUS CHRIS- oh wait wrong religion uhhhh ouch owie owww ):")
                    game_state["wrong_tile_1-2"] = True
                    game_state["wrong_tile"] = True
                else: 
                    print1(name+": 'Damn... Again?'")
                    game_state["wrong_tile_1-2"] = True
            else: print1(name+": I'm not stepping on that tile again...")

        if choice in ["2", "second" "step on the second tile"]: #
            print1("As you step onto the second tile, you feel... nothing?")
            if game_state["wrong_tile"] == True: print1(name+": So it's this tile...")
            else: print1(name+": That's... strange")
            FirePuzzle2()
            break #idk if this is needed but just incase yknow

        if choice in ["4", "observe" "observe your surroundings"]: #
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

def FirePuzzle2():
    global player_HP
    print1("Well, you managed to step on the right tile, but theres 2 more sets in front of you. Good luck!")
    while True:
        player_bar = player_HP // 10
        health_bar2 = '█' * player_bar #player bar
        empty_space2 = ' ' * (10 - player_bar)
        print(f"\rplayer HP: [{health_bar2}{empty_space2}] {player_HP}", end='', flush=True)
        print()
        if player_HP <= 0:
            firedeath()
        print1(name + ": 'How should I go about this?' \n1. Step on the first tile\n2. Step on the second tile\n3. Step on the third tile\n4. Observe your surroundings")
        choice = get_input("")
        
        if choice in ["1", "first" "step on the first tile"]: 
            if game_state["wrong_tile_2-1"] == False:
                print1("As you step onto the first tile, you feel the ground underneath you sink in, as a pillar of fire erupts from your current location")
                if evasion == 2: 
                    print1("You barely manage to stumble back to where you started, lucky you!")
                else:
                    print1("You burn your leg badly as you stumble back to where you started. Ouch.")
                    player_HP -= 34
                if game_state["wrong_tile"] == False:
                    print1(name+": JESUS CHRIS- oh wait wrong religion uhhhh ouch owie owww ):")
                    game_state["wrong_tile_2-1"] = True
                    game_state["wrong_tile"] = True
                    
                else: 
                    print1(name+": 'Damn... Again?'")
                    game_state["wrong_tile_2-1"] = True

            else: print1(name+": I'm not stepping on that tile again...")
            
        if choice in ["2", "second" "step on the second tile"]: #
            if game_state["wrong_tile_2-2"] == False:
                print1("As you step onto the second tile, you feel the ground underneath you sink in, as a pillar of fire erupts from your current location")
                if evasion == 2: 
                    print1("You barely manage to stumble back to where you started, lucky you!")

                else:
                    print1("You burn your leg badly as you stumble back to where you started. Ouch.")
                    player_HP -= 34

                if game_state["wrong_tile"] == False:
                    print1(name+": JESUS CHRIS- oh wait wrong religion uhhhh ouch owie owww ):")
                    game_state["wrong_tile_2-2"] = True
                    game_state["wrong_tile"] = True
                else: 
                    print1(name+": 'Damn... Again?'")
                    game_state["wrong_tile_2-2"] = True
            else: print1(name+": I'm not stepping on that tile again...")

        if choice in ["3", "third" "step on the third tile"]: #
            print1("As you step onto the third tile, you feel... nothing?")
            if game_state["wrong_tile"] == True: print1(name+": It's number 3 this time")
            else: print1(name+": Do these tiles even do anything?")
            FirePuzzle3()
            break #idk if this is needed but just incase yknow

        if choice in ["4", "observe" "observe your surroundings"]: #
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
        
def FirePuzzle3():
    global player_HP
    print1("That's another one down, and one more to go")
    while True:
        player_bar = player_HP // 10
        health_bar2 = '█' * player_bar #player bar
        empty_space2 = ' ' * (10 - player_bar)
        print(f"\rplayer HP: [{health_bar2}{empty_space2}] {player_HP}", end='', flush=True)
        print()
        if player_HP <= 0:
            firedeath()
        print1(name + ": 'How should I go about this?' \n1. Step on the second tile\n2. Step on the third tile\n3. Observe your surroundings")
        choice = get_input("")
        
        if choice in ["1", "second" "step on the second tile"]: 
            if game_state["wrong_tile_3"] == False:
                print1("As you step onto the second tile, you feel the ground underneath you sink in, as a pillar of fire erupts from your current location")
                if evasion == 2: 
                    print1("You barely manage to stumble back to where you started, lucky you!")
                else:
                    print1("You burn your leg badly as you stumble back to where you started. Ouch.")
                    player_HP -= 34
                if game_state["wrong_tile"] == False:
                    print1(name+": JESUS CHRIS- oh wait wrong religion uhhhh ouch owie owww ):")
                    game_state["wrong_tile_3"] = True
                    game_state["wrong_tile"] = True
                    
                else: 
                    print1(name+": 'Damn... Again?'")
                    game_state["wrong_tile_3"] = True

            else: print1(name+": I'm not stepping on that tile again...")
            
        if choice in ["2", "third" "step on the third tile"]: #
            print1("As you step onto the third tile, you feel nothing again")
            if game_state["wrong_tile"] == True: print1(name+": It's number 3 again...")
            else: print1(name+": Huh, that was suprisingly easy!")
            break

        if choice in ["3", "observe" "observe your surroundings"]: #
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
            
def Fire(): # Flame <--- this is the equivalent of our folder of code ig basically when we called to it it'll basically open up this entire folder and run it line by line
    #ok sick so now we gotta add chamber specific traps - 3x3 tile, the order is 2, 3, 3
    global enemy_HP, enemy_miss_chance, player_miss_chance, attack_name_1, attack_name_2, attack_name_3, player_HP
    print1("Walking through the fiery hall in front of you leads to a room with a square, checkered floor")
    print1("You're greeted by a 3x3 set of tiles, and across from it is, well, more hallway...")
    print1(name + ": Well, I guess it's a trial for a reason")
    FirePuzzle1()
     
    print1("As you continue walking through the blazing heat of the hallway, you come across a split path")
    print1(name + ": Yeah, what did I expect...")
    while True:
        print1 (name +": 'Which path should I go down?' \n1. The first path\n2. The second path\n3. Maybe I should explore a bit more..")
        choice = get_input("")
        if choice in ["1", "first" "the first path"]:
            print1("You walk through the first path, and find yourself facing the back of an enormous creature")
            print1("As you look closer, you realize that it resembles a mythical creature, the 'Dragon'")
            print1("Before you can do anything else, it turns around and looks down at you")
            print1(name+": Uh, hi?")
            print1("Yeah it doesn't speak human, or, at least it doesn't respond to what you said")
            print1("You prepare for combat...")
            enemy_HP = 100 # Stats for the Dragon boss
            enemy_miss_chance = 10
            player_miss_chance = 10
            attack_name_1 = "Dragon Claw"
            attack_name_2 = "Dragon Breath"
            attack_name_3 = "Flamethrower"
            fighting()
            if player_HP <= 0:
                print1("The heat from the dragon scorches your body")
                print1("You're engulfed in flames, and all the scars on your body melt")
                print1("You feel your eyes liquify, unable to scream")
                print2("...")
                print3("ENDING 7")
                print(" | 'The human eye is a delicate structure, and while the term 'melt' isn't technically accurate, extreme heat can cause significant damage. The proteins in the eye, particularly in the cornea and lens, begin to denature at temperatures above 60°C (140°F). Prolonged exposure to temperatures around 100°C (212°F), such as boiling water, could lead to severe damage to the eye's tissues.'")
                print()
                print("However, it's important to note that actual melting of the eyeball tissues is unlikely to occur in a literal sense, as the eye is composed of various tissues rather than a single material that would melt. Instead, high temperatures would cause burning, charring, and irreversible damage. ")
                print() # This some LCE E.G.O Lantern Yi Sang stuff I can't lie
                print1("Always exercise caution to protect your eyes from extreme conditions.")
            else:
                print1("As your last strike reaches the dragon, it flails around a bit, before collapsing")
                print1("It seems to be dead, or maybe unconscious. Hopefully dead")
                print1(name+": Alright... what's next...")
                print1("Actually, the door behind the dragon opens up, and through it you see...")
                print1(name+": Light?")
                end_sequence()
                print1("As you leave the colloseum with joy in your eyes, you fail to notice the horse carriage behind you")
                print1("It turns out, the horses went out of control. Directly on the road behind you")
                print1("Before you have time to react, you get trampled to death by these horses, before they are promptly put down")
                print3("ENDING 5")
                print1(" | 'cooked lil bro'")
                sys.exit
        elif choice in ["2", "second" "the second path"]:
            game_state["infernal_knight"] = True
            print1("Walking through the second path, you find yourself facing a suit of armor")
            print1("It's dressed up in flame decals, and some of them are moving")
            print1("Oh, wait, no it's just on fire")
            print1(name+": Who would leave a suit of armor here? And how has it not melted?")
            print1("As if in response to your question, its eyes light up, and it points its sword at you")
            print1(name+": are you genuienly kidding me")
            enemy_HP = 100 # Stats for the Infernal Knight boss
            enemy_miss_chance = 10
            player_miss_chance = 10
            attack_name_1 = "Flaming Slash"
            attack_name_2 = "Explosive Blast"
            attack_name_3 = "Set your heart ablaze" #This does 1-100 damage randomly
            fighting()
            if player_HP <= 0:
                game_state["infernal_knight"] = False
                print1("The knight cleaves off one of your limbs")
                print1("Luckily, the wound immediately cauterizes")
                print1("Unluckily, the knight beheads you immediately afterwards")
                print1("At least it was a quick death...")
                print2("...")
                print3("ENDING 8")
                print1(" | 'Was that a demon slayer reference?'") # nooooooo... (maybee)
            else:
                print1("You manage to hit one of the knights joints, as the armor starts to fall apart")
                print1("The flames die down, and the room feels cooler")
                print1(name+": 'Am I finally done?'")
                print1("The door behind the knight opens to your thought, and through it you see...")
                print1(name+": Light?")
                end_sequence()
                print1("You leave the colloseum, under th extreme heat, and incredibly fatigue")
                print1(name+": Man, its... really.... hot outside...")
                print1("Before you can finish your sentence, you collapse of heatstroke")
                print1("Maybe you should've gotten an ice pack")
                print2("...")
                print3("ENDING 9")
                print1(" | 'You're literally on fire for like 30 minutes of the game how does the sun get you'")
                sys.exit
        elif choice in ["3", "explore" "maybe i should explore a bit more"]:
            print1("You search around the hallway, but aside from the molten rock embedded in the wall, nothing stands out")
            print1(name+": Nothing useful...")

def firedeath(): 
    global player_HP
    print1("I'm going to go out on a limb here (lol) and say you burned your leg too much")
    print1("Eventually, the pain gets to you, and you pass out")
    print1("And also bleed out, and before you say the wound would cauterize itself, uhhh")
    print1("Yeah this is my world and I make the rules so like, deal with it lmao")
    print3("ENDING 2")
    print1(" | 'MYY LEGGGGGG  - Fred the Fish'")
    game_state["check_board"] = False
    game_state["wrong_tile"] = False
    game_state["wrong_tile_1-1"] = False
    game_state["wrong_tile_1-2"] = False
    game_state["wrong_tile_2-1"] = False
    game_state["wrong_tile_2-2"] = False
    game_state["wrong_tile_3"] = False
    player_HP = 100
    FirePuzzle1()

def DistainBridge():
    distance_counter = 0
    while True:
        if distance_counter >= 10:
            print1("You've crossed 10/10 meters of the bridge!")
            print1("You make it to the other side of the bridge, intact, very impressive!")
            print1("The hallway in front of you clears up, increasing the visibility a little")
            print1(name+": 'Guess I'll keep moving...'")
            break
        else:
            print1(f"You've crossed {distance_counter}/10 meters of the bridge!")
            print1("'How should I cross this part of the bridge' \n1. Fast and dangerous\n2. Steady and careful\n3. Slow and cautious")
            choice = get_input("")
            if choice in ["1", "fast", "fast and dangerous"]:
                print1("You cross the section of the bridge very quickly")
                print2("...")
                motionchance = random.randint(1,5)
                if motionchance <= evasion:
                    distance_counter += 5
                else:
                    print1("One of the statues catches you, and launches a projectile at your feet, destroying the bridge")
                    distaindeath()
            elif choice in ["2", "steady", "steady and careful"]:
                print1("You cross the section of the bridge moderately quickly")
                print2("...")
                motionchance = random.randint(1,3)
                if motionchance <= evasion:
                    distance_counter +=3
                else:
                    print1("One of the statues manages to catch you, and launches a projectile at your feet, destroying the bridge")
                    distaindeath()
            elif choice in ["3", "slow", "slow and cautious"]: # This is guarenteed to avoid getting stuck by being unlucky
                print4("You cross the section of the bridge ")
                print3("INCREDIBLY")
                print1(" slowly")
                distance_counter += 1
            print1("The statues open their eyes, and you freeze in time, holding your breath, waiting for their eyes to close")
            print2("...")
            print1("Eventually, your chance comes")

def DistainPuzzle():
    while True:
        if game_state["room_investigation"] == False: print1 (name +": 'How should I cross this bridge' \n1. Quickly\n2. Slowly\n3. Investigate")
        else: print1 (name +": 'How should I cross this bridge' \n1. Quickly\n2. Slowly\n3. Investigate \n4. Carefully")
        choice = get_input("")
        if choice in ["1", "quickly"]:
            print1("You attempt to run as fast as you can across this damaged bridge, which, I mean I don't know what you expected")
            print1("Fully focused on the end, you don't see why the bridge snaps, all you see is that it snaps")
            distaindeath()
        elif choice in ["2", "slowly"]:
            print1("You cautiously walk across this bridge, focused on the flayed rope that holds it in place, and the stability of the planks under your feet")
            print1(name+": 'Man I really hope this bridge doesn't blow up directly underneat-'")
            print1("And with that, you notice a bolt of, something, fly out from something on your left")
            evadechance = random.randint(1, 4)
            if evadechance >= evasion:
                print1("You manage to swiftly get out of the way, and whatever flew at you didn't hit the bridge!")
                print1("As your eyes dart to the location of the projectile, you notice several statues")
                print1("They seem to be watching the bridge, and also...")
                print1(name+": 'They're... blinking?'")
                game_state["room_investigation"] = True
            else:
                print1("You deflect the projectile with your shield, but it hits one of the tethers, causing the bridge to collapse")
                distaindeath()
        elif choice in ["3", "investigate"]:
            if game_state["bridge_investigation"] == False:
                print1("Upon closer inspection of the bridge, you realize that...")
                print1("It's really old... and also would shatter if more than one people walked on it")
                game_state["bridge_investigation"] = True
            else: 
                print1("Upon closer inspection of the room itself, you notice peculiar statues on the left and right")
                print1("They seem to be watching the bridge, and also...")
                print1(name+": 'They're... blinking?'")
                game_state["room_investigation"] = True
        elif choice in ["4", "carefully"]:
            if game_state["room_investigation"] == False:
                continue #essentially so you cant just type 4 and get away with it
            else: 
                print1("You start to cross the bridge carefully, and as your foot moves towards the bridge, you notice one of the statues change")
                print1("It's looking directly at you")
                print1("You freeze in terror")
                print1(name+": What the...")
                print1("Your train of thought is interupted by the statues blink, its gaze no longer focused on you")
                print4("It's as if")
                print3("...")
                print1("it can't see you anymore")
                print1(name+": Maybe it's triggered by... movement?")
                DistainBridge()
                break


def Distain(): # Sewer
    global enemy_HP, enemy_miss_chance, player_miss_chance, attack_name_1, attack_name_2, attack_name_3, player_HP
    print1("Walking through the smokey hallway in front of you leads you to a rickety looking bridge")
    print1("The bridge seems to be made of old planks, tethered with flayed ropes, and held together by a highschool students hopes and dreams") #just like pygame
    print1("wait a minute...")
    print1(name+": 'How is there a bridge in this narrow cavern?'")
    print1("(uhh worldbuilding you gotta believe me)")
    DistainPuzzle()


    print1("As you continue to walk through the seemingly normal hallway, you come across a split path")
    print1(name + ": Yeah, what did I expect...")
    while True:
        print1 (name +": 'Which path should I go down?' \n1. The first path\n2. The second path\n3. Maybe I should explore a bit more..")
        choice = get_input("")
        if choice in ["1", "first" "the first path"]:
            print1("You head down the first path, and enter a chamber that looks, normal?")
            print1("By all means, it defintely looks like you're in a cave, but also similar to a house")
            print1(name+": What the..")
            print1("In one of the corners, you see a ghastly figure in the fetal position")
            print1(name+": Uh, hey, you ok bro?")
            print1("It pretends not to hear you")
            game_state["ghost"] = True
            enemy_HP = 1 # Stats for the depressed ghost boss
            enemy_miss_chance = 2
            player_miss_chance = 2
            attack_name_1 = "Quiet Weeping"
            attack_name_2 = "Insomniac Stare"
            attack_name_3 = "Life Contemplation" # These names dont actually do anything since she shouldn't be able to attack
            fighting()
            print1("You see the ghost fade away, leaving behind a key")
            print1("You pick up the key and unlock the back door of the house-cave thing (even I have no idea how this room looks)")
            print1("The door opens to reveal the daylight you've missed so badly")
            end_sequence()
            print1("You leave the colloseum in a great mood, and nothing can bring you down")
            print1("Except for the massive explosion you just heard")
            print1("Your head darts over to the sound of the explosion, and you notice an active volcano, yknow, being active")
            print1("Oh and you're very much in the danger radius")
            print1("Even after you run as fast as you can, the debris and lava manage to catch up")
            print1("You're caught and burned alive, quite painfully, but at least it was faster than being engulfed in fire")
            print3("ENDING 11")
            print1(" | 'Maybe you can hang out with that ghost in the afterlife, if they're even dead (they aren't)'")
            sys.exit
        elif choice in ["2", "second" "the second path"]:
            print1("You slide down the second path, and find yourself in an...")
            print1("Unloaded room?")
            print1("wait hold on, theres nothing here, like literally nothing")
            print1("(hold on lemme fix this real quick)")
            print1("OK! well, uh, you find yourself in an empty void, with a door. It's... just a lone door")
            print1("It seems to be unlocked, but theres a key anyway")
            print1(name+": Can I just... leave?")
            print1("You walk through the unlocked door, leaving the key behind")
            end_sequence()
            print1("You leave the colloseum in shambles, but its fine because you're finally freeee!")
            print1(name+": Oh yeah I'm finally free!")
            print1("Yeah, yeah you are")
            print1("Man I feel reaallyy bad for whats about to happen")
            print1(name+": I really hope nothing bad happens in the next 5.13 seconds")
            print1("In 5.14 seconds, your foot gets caught on a pebble in the road, and you faceplant right into the pavement")
            print1("The force was enough to break your neck")
            print1("Immediately")
            print3("ENDING 12")
            print1(" | 'I genueinly ran out of ideas. Its been like 5 straight days of writing code and creating concepts, Mr. Nagra please let me out of the basement'")
            sys.exit

            fighting()
        elif choice in ["3", "explore" "maybe i should explore a bit more"]:
            print1("You search around the hallway, but aside from the stones decorating the floor, nothing stands out")
            print1(name+": Nothing useful...")

def distaindeath():#L BOZO
    print1("And with it, you plummet down below")
    print1("[*insert really funny falling noises, followed by the flesh being dissolved, accompanied by the screams of the damned*]")
    print2("...")
    print1("Uh, ok skipping past that horrifying experience, you died!")
    print1("If you couldn't tell")
    print3("ENDING 3")
    print1(" | 'No, I would never steal this puzzle idea of a D&D reddit post, you gotta believe me'")
    if game_state["room_investigation"] == False:
        game_state["bridge_investigation"] = False
        DistainPuzzle()
    else: 
        # gamestates check
        DistainBridge()

def EastWall():
    global player_HP
    while True:
        player_HP -= 5
        player_bar = player_HP // 10
        health_bar2 = '█' * player_bar #player bar
        empty_space2 = ' ' * (10 - player_bar)
        print(f"\rplayer HP: [{health_bar2}{empty_space2}] {player_HP}", end='', flush=True)
        print()
        if player_HP <= 0:
            icedeath()
        print1(name+": 'Awesome! What now...' \n1. Press a random button\n2. Press all 3 buttons \n3. Just slash the ice and take it")
        choice = get_input("")
        if choice in ["1", "press a random button"]:
            print1("You press a random button, and nothing happens")
            print1(name+": Hm. What if...")
            print1("You press another, different button, and nothing happens")
            print1(name+": Okkk...")
            print1("You press the last, other button, and nothing happens. Again")
            print1(name+": Wait, WHAT?")
            if game_state ["randombutton"] == True:
                print1("What, did you just expect it to work if you did tried it again? Have you heard of textbook insanity?")
            else:game_state ["randombutton"] = True
        elif choice in ["2", "press all 3 buttons"]:
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
        elif choice in ["3", "just slash the ice and take it"]:
            print1("You raise up your sword and just cut down the ice, expertly avoiding the pristine cube in the middle") # Holy glaze
            if game_state ["randombutton"] == True: print1("Honestly this feels more reasonable then just pressing random buttons")
            print1("The ice shatters and the cube rolls to your feet. Good job!")
            print1(name+": Huh, nice.")
            game_state ["cube_east"] = True
            break

def WestWall():
    global player_HP
    while True:
        player_HP -= 5
        player_bar = player_HP // 10
        health_bar2 = '█' * player_bar #player bar
        empty_space2 = ' ' * (10 - player_bar)
        print(f"\rplayer HP: [{health_bar2}{empty_space2}] {player_HP}", end='', flush=True)
        print()
        if player_HP <= 0:
            icedeath()
        print1(name+": 'What does this mural want me to do?' \n1. Start worshipping the cube\n2.  Sacrifice yourself to the cube\n3. Smash the mural and take the cube")
        choice = get_input("")
        if choice in ["1", "worship", "start worshipping the cube"]:
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
        elif choice in ["2", "sacrifice", "sacrifice yourself to the cube"]:
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
                print1(name +": Oh nice! I actually survived!")
                print1("Did you not expect to?? Just, just go...")
                game_state["attempted_sacrifice"] = True
            else: 
                print2("NO")
                print1("Don't do that again...")
                player_HP += 5
        elif choice in ["3", "smash", "smash the mural and take the cube"]:
            print1("You attempt to smash the mural")
            print1("Your sword bounces off with a resounding thud")
            print1("The cube god frowns upon you")

def IcePuzzle():
    global player_HP
    print1("You feel the frigid cold ramp up as the light goes out")
    print1("Suprisingly, there's still a bit of light left, just enough to see")
    print1(name +": This cold reaally hurts, I won't lie")
    print2("...")
    print1(name +": I wont get hypothermia right?")
    print1("uhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh yeah uh huh for sure (foreshadowing.jpg)")
    clear()
    while True:
        print1("The cold grows, uh, colder... as you feel the effects of frostbite get ever so stronger")
        player_HP -= 5
        player_bar = player_HP // 10
        health_bar2 = '█' * player_bar #player bar
        empty_space2 = ' ' * (10 - player_bar)
        print(f"\rplayer HP: [{health_bar2}{empty_space2}] {player_HP}", end='', flush=True)
        print()
        if player_HP <= 0:
            icedeath()
        print1(" "+name +": 'What should I do now?' \n1. Check the northern wall\n2. Check the eastern wall\n3.Check the southern wall\n4.Check the western wall")
        choice = get_input("")
        if choice in ["1", "north", "check the northern wall"]:
            if game_state ["cube_east"] == True and game_state ["cube_west"] == True and game_state ["cube_south"] == True and game_state ["checked_door"] == True: # the == true on all of them is most likely redundant but who cares its 2am
                print1("You place all 3 of the cubes into the slot in the door")
                print1("Unsuprisingly, it opens up")
                print1("The air ahead is MUCH warmer than in that icebox")
                print1(name +": Finally... out of the cold")
                break
            else:
                print1("You walk up to the northern wall, and find a door with 3 cubes carved out of it")
                print1("The door has a sign that reads: -- ---- --- ----- ---")
                print1(name +": ...What?")
                print1("Oh, uh, right, you can't read...")
                print2("...")
                print1(name +": Very helpful")
                game_state["checked_door"] = True
        elif choice in ["2", "east", "check the eastern wall"]:
            if game_state ["cube_east"] == False:
                print1("You slide up to the eastern wall, and find a cool looking cube encased in ice")
                print1("Under the cube reads: --- ---- ---- ----, with 3 buttons underneath")
                print2("...")
                print1("You should've worked on your reading comprehension before going to jail...")
                print1("Would you like to investigate the encased cube? \n1. Yes \n2. No")
                choice = get_input("")
                if choice in ["1", "Yes"]:
                    player_HP += 5
                    EastWall()
                else: 
                    print1(name +": I'll check this out later")
                    print1("You return to the center of the room")
            else: print1(name +": I don't think I need anything else from the eastern wall")
        elif choice in ["3", "south", "check the southern wall"]:
            if game_state ["cube_south"] == False:
                print1("You shimmy back over to the south wall, where you entered the room from, when you notice something shiny on the floor")
                print1(name +": Is that a convieniently placed cube directly at the entrance so that the person who made this chamber doesn't have to think about creating a real puzzle for this?")
                print2("...") # Look I was tired and I'm not really known for being creative ok :(
                print1("That was... incredibly accurate... kind of scary actually...")
                print1("Anyway! you've found a cube!")
                game_state ["cube_south"] = True
            else: print1(name +": I don't think I need anything else from the southern wall")
        elif choice in ["4", "west", "check the western wall"]:
            if game_state ["cube_west"] == False:
                print1("You shuffle over to the west wall, where you see a mural placed in clear view... well... however clear this dark room is")
                print1("Would you like to investigate the mural cube? \n1. Yes \n2. No")
                choice = get_input("")
                if choice in ["1", "yes"]:
                    print1("The mural shows a diagram of 4 people worshipping a cube. The next panel shows the cube, uh, (wait am I seeing this right)")
                    print1("Ahem, the next mural shows 3 of those people being sacrificed to the cube. Brutally. In fact, this would probably be rated M if there were visuals")
                    print1(name +": oh that's, that's gore...")# HE SAID IT HE SAID THE THING OH MY GOD
                    print1("The last panel has a mirror, along with the cube that was being worshipped.")
                    player_HP += 5
                    WestWall()
                else: 
                    print1(name +": I'll check this out later")
                    print1("You return to the center of the room")
            else: print1(name +": I don't think I need anything else from the western wall")

def Ice(): # Frost 
    global enemy_HP, enemy_miss_chance, player_miss_chance, attack_name_1, attack_name_2, attack_name_3, player_HP
    print1("Walking through the blistering winds in front of you, you find a room with a campfire and torches, somehow unextinguished")
    print1("It feels... warm")
    print1(name + ": 'Should I go in?' \n1. Go in the room \n2. Stay in the hallway")
    choice = get_input("")
    if choice in ["1", "go in the room", "room"]:
        print1(name + ": That's a nice break...")
        print2("...")
        print1(name+": ...Wait a minute")
        print1("As you come to realize that theres no way a 'trial' would have a room for a break, the path you took quickly closes itself off to you")
        print1("Just as you turn to look at it, the campfire and torches extinguish simultaneously")
    elif choice in ["2", "stay in the hallway", "stay"]:
        print1(name + ": There's no way this isn't a trap")
        print2("...")
        print1("And you're right about that. But we've got to progress somehow, right?") # Railroading isn't real you made that up | could make this a death ending if needed
        print1("You quickly notice the walls closing in around you, as the room in front of you becomes your way of escape")
        print1(name + ": ...I expected as much")
        print1("The pathway you took closes, and you notice the torches and campfire extinguish simultaneously")
    print1(name+": Damn it...")
    IcePuzzle()
    
    print1("Oh, it's still really cold though")
    print2("...")
    print1("As you continue walking through the freezing cold of the hallway, you come across a split path")
    print1(name + ": Yeah, what did I expect...")
    while True:
        print1 (name +": 'Which path should I go down?' \n1. The first path\n2. The second path\n3. Maybe I should explore a bit more..")
        choice = get_input("")
        if choice in ["1", "first" "the first path"]:
            game_state["totem"] = True
            print1("You walk through what seems to be an exit, only to find yourself in an arena made of pure ice")
            print1("In the middle, you see what seems to be a frozen 'totem pole', about 10 meters from you")
            print1("Its eyes light up in response to your presence")
            print1(name+": Uh, hi?")
            print1("It looks pretty hostile I won't lie")
            print1("Also, you notice the floor is VERY slippery beneath you")
            print1("Ok great good luck dont die I belieevee in you")
            print1(name+": WHAT")
            enemy_HP = 31 # Stats for the Ice totem boss
            enemy_miss_chance = 5
            player_miss_chance = 2
            attack_name_1 = "Snowball"
            attack_name_2 = "Icicle Toss"
            attack_name_3 = "Spear of Ice"
            fighting()
            if player_HP <= 0:
                game_state["totem"] = False
                print1("As you attempt to keep moving forward, the ice in your body causes you to freeze")
                print1("No longer able to move, the totem hits every strike")
                print1("Your body shatters")
                print2("...")
                print3("ENDING 6")
                print1(" | 'Death by being Canadian'")
            else:
                print1("The totem pole shatters upon your strike")
                print1("You notice the door on the other side of the room open up")
                print1(name+"Am I finally free?")
                print1("You walk through the open door and see...")
                print2("...")
                print1(name+": Is that... light?")
                print1("The bright light of the outside shines on your face, as you walk back into the arena, triumphantly")
                end_sequence()
                print1("As you leave the colloseum, tired and ready to go home (wherever that is), you get stopped on the road by a mysterious figure")
                print1("???: Yo! Hand over everything you got")
                print1(name+": Oh, uh, I don't have any mone-")
                print1("Before you can finish your sentence, you get viciosly stabbed through the gut, as the robber makes off with your sword")
                print4(name+": Ain't no way that just")
                print2("...")
                print1("You pass out from blood loss")
                print3("ENDING 4")
                print1(" | 'You managed to kill a magic wielding ice totem, and you died to a robber?'")
                sys.exit

        elif choice in ["2", "second" "the second path"]:
            print("You walk through the path on the right, and find yourself looking at a frozen human")
            game_state["lich"] = True
            enemy_HP = 100 # Stats for the Ice Lich
            enemy_miss_chance = 10
            player_miss_chance = 10
            attack_name_1 = "Frostbite"
            attack_name_2 = "Stalactite"
            attack_name_3 = "Pillar of Ice"
            fighting()
            if player_HP <= 0:
                game_state["lich"] = False
                print1("The lich manages to freeze one of your legs")
                print1(name+": 'Oh, I can't move, damn'")
                print1("Wow, real enthusiatic for someone about to die")
                print1("You notice as frost slowly creeps up from the bottom, eventually encasing your whole body")
                print1("And then you feel, well, actually you don't")
                print3("ENDING 10")
                print1(" | 'School nurse if she could legally prescribe more ice'")
            else:
                print1("The lich screeches as your sword pierces its skull")
                print1("You notice the door on the other side of the room open up")
                print1(name+"That... really sucked")
                print2("...")
                print1(name+": 'Does that lead outside?'")
                print1("You walk through the newly opened door")
                end_sequence()
                print1("You leave the arena, head empty, no thoughts")
                print1("As you start to realize you have nowhere to go, you hear a creak")
                print1(name+": What was that?")
                print1("You notice the structural integrity of the nearby buildings fail")
                print4(name+": There's no way")
                print2("...")
                print1("Before you can make it out in time, a sinkhole opens beneath you, and you're crushed by the debris")
                print3("ENDING 10")
                print1(" | 'Mmmm ancient rome smoothie mmm delicious'")
                sys.exit
        elif choice in ["3", "explore" "maybe I should explore a bit more"]:
            print1("You search around the hallway, but aside from the seemingly random sets of icicles, nothing stands out")
            print1(name+": Nothing useful...")

def icedeath():
    global player_HP
    print1("Your body, no longer able to withstand the cold, shrivels up and collapses")
    print1("Man, I really didn't think those puzzles were that hard, I mean its like 5 hp every loop")
    print1("That means it takes 20 seperate choices to manage to die here")
    print1("Honestly, this hypothermia mechanic is just for making the boss fight harder, you weren't even supposed to die here")
    print3("ENDING 1")
    print1(" | 'How did you manage this one?'")
    print1("Well, uh, I guess we can just come back to when you entered")
    game_state["cube_east"] = False
    game_state["cube_south"] = False
    game_state["cube_west"] = False
    game_state["randombutton"] = False
    game_state["checked_door"] = False
    game_state["attempted_sacrifice"] = False
    player_HP = 100
    IcePuzzle()

def end_sequence():
    print1("The Emperor sits there in stunned silence, watching you walk out alive")
    print1("Emperor: Well, uh, no one has ever survived these trials. (uh what do we do now)")
    print2("...")
    print1("Emperor: Ok! Due to lack of procedure, you're uh, free to go")
    print1(name+": Oh for realsies?")
    print1("Emperor: Yeah! yeah, just go. We uh, don't want you here anymore")
    print1(name+": Ok cool byeee")

#opening sequenceeee
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
fighting()
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
    if choice in ["1", "murder"]:
        if game_state ["murder"] == False:
            print1(name + ": I... killed a man")
            print1("Emperor: Well! There you have it! They killed someone in cold blood!")
            print1(name + ": No, thats not what I mea-")
            print1("You're promptly cut off by the booing of the crowd")
            game_state["murder"] == True
            break

    elif choice in ["2", "theft"]:
        if game_state ["theft"] == False:
            print1(name + ": I stole some bread so my family wouldn't starv-")
            print1("Emperor: I see! So you stole food from a poor vendor trying to make a living... How horrible!")
            print1(name + ": No, thats not what I mea-")
            print1("You're promptly cut off by the booing of the crowd")
            game_state["theft"] == True
            break

    elif choice in ["3", "attempts to overthrow the current political system through multistage conspiracy and bribery of government officials"]:
        if game_state ["funny"] == False: #yeah im not checking the gamestate system to see if it works we'll suffer later XD
            print1(name +": Oh, uh, I tried to overthrow the current political system through multistag-... (wait what the hell no I didn't, who would even think of doing that??)")
            print1("Emperor: ...")
            print1("Emperor: I mean, uh, you wouldn't be the first, I guess?")
            print1("Emperor: But what did you REALLY do?")
            game_state["funny"] = True
            
        else: 
            print1(name +": 'No I didn't...'")

    elif choice in ["4", "i'm not a criminal!"]:
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
# roll variable out of 4 or something idk
damage = 0
if game_state ["murder"] == True:
    damage += 2
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
    if choice in ["1", "fire", "trial of fire"]:
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
        Fire()
    elif choice in ["2", "distain", "trial of distain"]:
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
        Distain()
    elif choice in ["3", "ice", "trial of ice"]:
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
        Ice()