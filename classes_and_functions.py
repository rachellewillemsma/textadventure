vowels = ['a','e','i','o','u']

npcs = {}
places = {}
things = {}

# functions

def add_name_pair(dict, object):
    dict[object.name] = object

# making sure routes between places should be reciprocal
def add_route(place1, place2, type, locked=0):
    match type:
        case 'ns':
            place1.routes['s'] = ['to the south is', place2.name, place2]
            place2.routes['n'] = ['to the north is', place1.name, place1]
        case 'ew':
            place1.routes['w'] = ['to the west is', place2.name, place2]
            place2.routes['e'] = ['to the east is', place1.name, place1]
        case 'ud':
            place1.routes['d'] = ['below you is', place2.name, place2]
            place2.routes['u'] = ['above you is', place1.name, place1]
        case 'oi':
            place1.routes['i'] = ['you can enter', place2.name, place2]
            place2.routes['o'] = ['you can exit to', place1.name, place1]
        case _:
            pass
            # raise error

# a thing can be abstract or physical
# when abstract, it is more akin to a topic
# you can ASK npcs (ABOUT) things
# you can TAKE and DROP portable items, as well as BUY and SELL most of them
# you can EQUIP and UNEQUIP equipable things
# you can EAT, DRINK, USE or CONSUME consumable things
# unique objects are quest objects or similar, of which the player should only ever have one at most

class thing:
    def __init__(self, name, desc, portable=0, equipable=0, consumable=0, pl=0, unique=0):
        self.name = name
        self.desc = desc
        self.portable = portable
        self.equipable = equipable
        self.consumable = consumable

        if pl == 0:
            self.pl = f'{name}s'
        else:
            self.pl = pl
        
        if name[0] in vowels:
            self.indef = f'an {name}'
        else:
            self.indef = f'a {name}'

        if unique:
            self.article = f'the {name}'
        else:
            self.article = self.indef

        add_name_pair(things, self)


# this is you, the player
# as this is a multiplayer game, this will have to be reworked to connect each player instance with an account

class player:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.inv = {}
        self.equiped = {}
        self.desc = f'you are carrying {self.inv}. you have {self.equiped} equiped.'

# you can TALK (TO/WITH) npcs (ABOUT) things
# sometimes you can BUY things (FROM) or SELL things (TO) npcs

class npc:
    def __init__(self, name, desc=0):
        self.name = name
        self.desc = desc
        self.inv = {}
        add_name_pair(npcs, self)

# places are just that, places the player can visit
# upon entry, descriptive text will appear
# some extra description should be added to appear depending on variables such as quest progress, and number of visits

class place:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        self.visited = 0
        self.rooms = {}
        self.inv = {}
        self.routes = {}
        self.exits = []
        add_name_pair(places, self)

    def visit(self):
        p.location = self
        print(f'\033[1m--- {self} ---\033[0m')
        print(self.desc, end='.\n')

        if self.rooms:
            print("there is", end=' ')
            for item in self.rooms:
                print(f"{self.rooms[item].article}", sep=', ', end='. ')
        if self.inv:                
            print("on the ground you see", end=' ')
            for item in self.inv:
                print(f"{self.inv[item].article}", sep=', ', end='.\n')

        self.exits = []
        self.neighbours = []

        for key in self.routes:
            self.exits.append(key)
            self.neighbours.append(self.routes[key][1])
            print(f"{self.routes[key][0]} {self.routes[key][1]}", end='.\n')

        self.visited += 1



    def __str__(self):
        return f'{self.name}'

# rooms are "smaller" locations inside a place, and appear as objects
# you can ENTER and EXIT most rooms, although this might require centain skills
# for example, to CLIMB a tree, wall, or ladder, you will need sufficient climbing skills
# trying to ENTER a tree should work as well but CLIMB is more intuitive and thus should also work
# you can OPEN and CLOSE some rooms, in which case the room is likely a type of container
# for now, rooms are considered to be both places and things

class room:
    def __init__(self, name, desc=0, enterable=0, openable=0, lockable=0):
        self.name = name
        self.desc = desc
        self.enterable = enterable
        self.openable = openable
        self.lockable = lockable
        add_name_pair(places, self)
        add_name_pair(things, self)

        
        if name[0] in vowels:
            self.article = f'an {name}'
        else:
            self.article = f'a {name}'
        
    def __str__(self):
        return f'{self.name}'



# instances

apple = thing("apple", "bright red and crunchy", 1, 0, 1)
knife = thing("knife", "not too sharp", 1, 1)

alley = place("alley",
    "you are in an alley")
orchard = place("orchard",
    "you are in an orchard")

apple_tree = room("apple tree", 'full of tasty fruit')




# add instances to places

add_name_pair(orchard.rooms, apple_tree)
add_name_pair(orchard.inv, apple)

add_route(alley, orchard, 'ns')



# player

p = player('adventurer', orchard)



# custom text generation variables

welcome_message = f'\033[1m--- welcome, {p.name}! ---\033[0m'


# verb definitions

# no args

def rest():
    pass

def inventory():
    print('you are carrying', end=' ')
    for key in p.inventory:
        print(key, sep=', ', end='.')

# 1 arg

def look(direct):
    if direct == []:
        print(p.location.desc)
    elif direct in p.location.rooms.keys():
        object = p.location.rooms.get(direct) 
        print(object.desc)
    elif direct in p.location.inv.keys():
        object = p.location.inv.get(direct) 
        print(object.desc)
    else:
        print(f"you don't see anything unusual about the {direct}")

def go(direct):
    if direct in p.location.exits:
        p.location.routes[direct][2].visit()
    elif direct in p.location.neighbours:
        places.get(direct).visit()
    else:
        print("you can't go that way")

def take(direct):
    if direct in p.location.inv.keys():
        object = p.location.inv.get(direct) 
        add_name_pair(p.inv, object)
        print(f'you took {direct} successfully')
    else:
        print("you can't take that from here")

def drop(direct):
    if direct in p.inv.keys():
        del p.inv[direct]
        print(f'you dropped {direct} successfully')
    else:
        print("you aren't carrying that")




def equip(direct):
    pass

def unequip(direct):
    pass

def buy(direct):
    pass

def sell(direct):
    pass

def hit(direct):
    pass

# 2 args

def put(direct, indirect):
    pass

def talk(direct, indirect):
    pass