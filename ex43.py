# this will be useful for the keypad
import random
import time
import sys

class Item(object):
    def __init__(self, name, weight, size):
        self.name = name
        self.weight = weight
        self.size = size

    def disp_item(self):
        print(f"Name: {self.name}, Weight: {self.weight}, Size: {self.size}")


class Character(object):
# default values must follow non-default values (argumennts!)
    def __init__(self, name, hp=10.0, score=0, location='b2'):
        self.name = name
        self.inventory = {}
        self.score = score
        self.hp = hp
        # How can I get the player to start at the central corridor...
        self.location = location

    def add_item(self, item):
        # item must have name, weight, and size
        self.inventory[item.name] = item

    def print_items(self):
        print('\t'.join(['Name','weight','size']))
        for item in self.inventory.values():
            # this prints the values that I've entered for the three attributes from Item class.
            print('\t'.join([str(x) for x in [item.name, item.weight, item.size]]))

    def user_greeting(self):
        print(f"Greetings {self.name}")

    def print_location(self):
        print('\n' + ('#' * (4 + len(zone_map[self.location][ZONENAME]))))
        print('#' + zone_map[self.location][ZONENAME] + '#')
        print('#' + zone_map[self.location][DESCRIPTION] + '#')
        print('\n' + ('#' * (4 + len(zone_map[self.location][ZONENAME]))))
#ok he didn't put any of this stuff within a class.. so he put myAction inside the function parentheses...
# I might need to leave this as self... change to myAction... or move it to outside of the character class.

    def char_move(self, myAction):
        ask = "Where would you like to move to? \n"
        dest = input(ask)
        if dest in ['up', 'north']:
            destination = zone_map[self.location][UP]
            # I updated the syntax for this... lets see if it works.
            Character.movement_handler(self, destination)
        elif dest in ['right', 'east']:
            destination = zone_map[self.location][RIGHT]
            Character.movement_handler(self, destination)
        elif dest in ['down', 'south']:
            destination = zone_map[self.location][DOWN]
            Character.movement_handler(self, destination)
        elif dest in ['left', 'west']:
            destination = zone_map[self.location][LEFT]
            Character.movement_handler(self, destination)

    def movement_handler(self, destination):
        print("\n" + "You have moved to the " + destination + ".")
        self.location = destination
        #this might need to be in a different class...
        Character.print_location(self)
        Engine.prompt(self)



    def char_examine(self, action):
        #assumes this is true
        if zone_map[self.location][SOLVED] == True:
            print("You have already exhausted this zone.")
        elif zone_map[self.location] [SOLVED] == False:
            print(zone_map[self.location] [EXAMINATION])
            Engine.prompt(self)
            #I need to somehow link the self.location to the different scenes!
        else:
            print("You can trigger the main game here")



## stuff up here is stuff I'ved added ^^^^^^^
class Scene(object):

    def __init__(self, challenge = False):
        self.items = []
        # self.gothons = gothons
        self.challenge = challenge




class CentralCorridor(Scene):

    def __init__(self):
        # this is the syntax for python 3 apparently...
        super(CentralCorridor, self).__init__()
        self.items = ['cheese','hairbrush']

    def get_items(self):
        print(f'{self.items}')

    def Cor_act(self):
        print("what will you do next?")

        resp = input("> ")

        if resp.lower == 'fight':
            fight(self)

    def fight(self):
        print("oh no! It's a slippery slimey Gothon! Time for battle!")
        fight_act = input("What will you do? ")
        accept_act = ['punch','tell joke','slap','draw sword','draw gun','hide','tackle']
        while fight_act not in accept_act:
            print('the Gothon stares at you confusedly')
            fight_act = input("> ")
        if fight_act in ['punch','tackle']:
            print('Ouch! ')
            # I probably did not call this class object correctly... do I need to inistantiate it again?
        elif fight_act == 'tell joke' and Character.location == 'b2':
            joke_fight(self)

    def joke_fight(self):
        print("--------")
        print("Gothon: a joke you say? please, do tell!")
        print('''Please pick a joke...
        a. Knock Knock...
        b. I never understood why Marijuana being a gateway drug was a bad thing
        c. You know what I don't get about intergalactic cosmic rays?''')
        joke = input("> ")
        while joke.lower() == 'b':
            print('Gothon chuckles')
            joke = input("> ")
        if joke.lower() == 'a':
            print('you die')
        if joke.lower() == 'c':
            print('Gothon starts uncontrollably laughing, and explodes.')
            #this is still pseudo code b/c idk how to reference the dictionary inside the dictionary thing
            d = {'b2' : {SOLVED: True}}
            zone_map.update(d)
            # put the SOLVED portion here! yayyyy!
            # (1) this gets me back to the prompt, but I loose my character location




class Engine(object):
# zed had a scene_map parameter... I'm going to take that out for now.
    def __init__(self, name, location='b2'):
        self.name = name
        self.location = location
### game interactivity ####
# his equivalent of mCharacter is also defined in his player class! yay!
    def prompt_loop(self, action):
        action = input("> ")
        acceptable_actions= ['move', 'dance', 'go', 'examine', 'quit', 'inspect', 'travel', 'walk', 'interact', 'look', 'help']
        while action.lower() not in acceptable_actions:
            print("Unknown action, try again.\n")
            action = input("> ")
        if action.lower() == 'quit':
            sys.exit()
        elif action.lower() in ['move', 'go', 'travel', 'walk']:
            #this syntax is muy importante!
            Character.char_move(self, action.lower())
        elif action.lower() == 'help':
            self.instructions()
        elif action.lower() in ['examine', 'inspect', 'interact', 'look']:
            Character.char_examine(self, action.lower())
        elif action.lower() == 'dance':
            print("you shake your bootay! woot woot!")
            Engine.prompt_loop(self, action.lower())

    # def scene_stuff(self, name):
    #     if self.name.lower() == 'CentralCorridor':
    #         b2 = CentralCorridor()
    #         CentralCOrridor.check(b2)
    #     else:
    #         print("poop")
    #         quit(0)


    def prompt(self):
        print('\n' + "----------")
        print("What would you like to do?")
        action = input("> ")
        acceptable_actions= ['move', 'fight', 'test', 'hp', 'dance', 'go', 'examine', 'quit', 'inspect', 'travel', 'walk', 'interact', 'look', 'help']
        while action.lower() not in acceptable_actions:
            print("Unknown action, try again.\n")
            action = input("> ")
        if action.lower() == 'quit':
            sys.exit()
        elif action.lower() in ['move', 'go', 'travel', 'walk']:
            #this syntax is muy importante!
            Character.char_move(self, action.lower())
        elif action.lower() == 'help':
            self.instructions()
        elif action.lower() == 'test':
            CentralCorridor.check(self, action.lower())
        elif action.lower() == 'tell joke':
            CentralCorridor.check(self, action.lower())
        elif action.lower() in ['examine', 'inspect', 'interact', 'look']:
            Character.char_examine(self, action.lower())
        elif action.lower() == 'dance':
            print("you shake your bootay! woot woot!")
            print('''
            ----------------
            What would you like to do?''')
            Engine.prompt_loop(self, action.lower())





    def instructions(self):
        print('''
                Welcome to Gothons from Planet Percal #25 the game!

This is a text-based adventure, which requires you, the hero, to input
your actions via text commands.

Here is a list of the available text commands that will allow you to perform
an action:

Movement/Map Commands:
description - you get a general description of the room
examine - you can examine part of the room
go, walk, travel, move - will allow you to choose which direction to move in
north or up - you will move north on the Map
east or right - you will move east on the Map
south or down - you will move south on the Map
west or left - you will move west on the Map

Character actions:
fight -



         ''')
        self.prompt()

# class Death(Scene):
#
#     def enter(self):
#         pass
#
#
#
# class LaserWeaponArmory(Scene):
#
#     def enter(self):
#         pass
#
# class TheBridge(Scene):
#
#     def enter(self):
#         pass
#
# class EscapePod(Scene):
#
#     def enter(self):
#         pass
#
#
# class Map(object):
#
#     def __init__(self, start_scene):
#         pass
#
#     def next_scene(self, scene_name):
#         pass
#
#     def opening_scene(self):
#         pass

######### MAP #############
#'''
# a1    a2     a3
# --------------------
# | EP |  BR  |      | a3
# --------------------
# |    |  CR  |      | b3
# --------------------
# |    |  LWA |      | c3
# -------------------


ZONENAME = ' '
DESCRIPTION = 'description'
EXAMINATION = 'examine'
SOLVED = False
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'
# SHORTCUT for editing multiple keys at once = select each key start while holding command then type the letter u want to replace it with
# useful for re-factoring code! (renaming functions nd stuff)
solved_places = {'a1': False, 'a2' : False, 'a3': False,
                'b1': False, 'b2' : False, 'b3': False,
                'c1': False, 'c2' : False, 'c3': False }
# dictionary within a dictionary. This is also useful for creating a local database within your own computer
# this makes every zone unique and navigatable.
#the player starts in b2...
zone_map = {
'a1' : {
        ZONENAME: "Escape Pod",
        #I'm getting a syntax error here but idk why
        DESCRIPTION : 'You\'ve entered a room full of escape pods!',
        EXAMINATION : 'They are all open for entry, hurry!',
        SOLVED : False,
        UP : 'escape',
        DOWN : 'b1',
        LEFT : 'wall',
        RIGHT : 'a2'
},
'a2' : {
        ZONENAME: "Bridge",
        DESCRIPTION : 'There is a bridge',
        EXAMINATION : '''As you take a step onto the bridge, a gothon jumps from
         the wall and stands on the middle of the bridge.''',
        SOLVED : False,
        UP : 'wall',
        DOWN : 'b2',
        LEFT : 'a1',
        RIGHT : 'a3',
},
'a3' : {
        ZONENAME: "",
        DESCRIPTION : 'description',
        EXAMINATION : 'examine',
        SOLVED : False,
        UP : 'wall',
        DOWN : 'b3',
        LEFT : 'a2',
        RIGHT : 'wall'
},
'b1' : {
        ZONENAME: "",
        DESCRIPTION : 'description',
        EXAMINATION : 'examine',
        SOLVED : False,
        UP : 'a1',
        DOWN : 'c1',
        LEFT : 'wall',
        RIGHT : 'b2'
},
'b2' : {
        ZONENAME: "Central Corridor",
        DESCRIPTION : 'You are in a white corridor with doors on all four sides.',
        EXAMINATION : f'There isn\'t much to see - but you get the feeling you have company.',
        SOLVED : False,
        UP : 'a2',
        DOWN : 'c2',
        LEFT : 'b1',
        RIGHT : 'b3'
},
'b3' : {
        ZONENAME: "",
        DESCRIPTION : 'description',
        EXAMINATION : 'examine',
        SOLVED : False,
        UP : 'a3',
        DOWN : 'c3',
        LEFT : 'b2',
        RIGHT : 'wall'
},
'c1' : {
        ZONENAME: "",
        DESCRIPTION : 'description',
        EXAMINATION : 'examine',
        SOLVED : False,
        UP : 'b1',
        DOWN : 'wall',
        LEFT : 'wall',
        RIGHT : 'c2'
},
'c2' : {
        ZONENAME: "Laser Weapon Armory",
        DESCRIPTION : 'You\'ve entered an armory!',
        EXAMINATION : 'You search the room and notice a keypad in the back right corner.',
        SOLVED :False,
        UP : 'b2',
        DOWN : 'wall',
        LEFT : 'c1',
        RIGHT : 'c3'
},
'c3' : {
        ZONENAME: "Spa",
        DESCRIPTION : 'MmmMmm bubbles, a minty fragrance in the air, looks like you\'ve happend upon the ships spa!',
        EXAMINATION : 'You notice a hottub, a rack full of shampoos, and a wall covered in a giant shag towel.',
        SOLVED : False,
        UP : 'b3',
        DOWN : 'wall',
        LEFT : 'c2',
        RIGHT : 'wall'
},


}



# a_map = Map('central_corridor')
# a_game = Engine(a_map)
# a_game.play()

def start():
    print("\t\tWelcome to Gothons from Planet Percal #25 the game!\n\n")
    time.sleep(0.5)
    char1 = Character(input("Please enter your character's name: "))
    # print(Character.location(char1))
    Character.user_greeting(char1)
    Character.print_location(char1)
    game_eng = Engine("CentralCorridor")
    Engine.prompt(game_eng)
    # Engine.scene_stuff(game_eng)

start()
# User Set up
# pop_tart = Item("pop-tart","0.25 lbs","small")
# character2 = Character("Charles")
# Character.add_item(character2, pop_tart)
# Character.print_items(character2)
# Character.user_greeting(character2)
