vowels = ['a','e','i','o','u']

lookups = {} # leave empty
places = [] # leave empty
things = [] # leave empty


class player:
    def __init__(self):
        pass

p = player()

class thing:
    def __init__(self, name):
        self.name = name
        add_to_lookups(self)

class place():
    def __init__(self):
        self.inv = {'potato': 7}
        self.routes = {}
          
    def visit(self):
        p.location = self
        print(f'\033[1m--- {self.name} ---\033[0m')
        print(self.desc, end='.\n')

    def lookup_inv(self, object):
        if object in self.inv.keys():
            return self.inv.get(object)
        else:
            print('that is not here')

    def lookup_exits(self, direction):
        if direction in self.routes.keys():
            return self.routes.get(direction)
        else:
            print('that is not here')

# place classes – will manually add

start = type('start',(place,),{
    'name': 'start', 
    'desc': 'a really nice start'})
forest = type('forest',(place,),{
    'name': 'green forest', 
    'desc': 'a really nice forest'}) 




# automate instance creation

def add_to_places(class_type):
    places.append([class_type][0])

def add_to_things(class_type):
    things.append([class_type][0])

def add_to_lookups(object):
    # add strings up to three words long
    input_single = object.name.lower().split(' ')
    input_double = []
    input_triple = []
    for x in range(len(input_single)-1):
        input_double.append(f'{input_single[x]} {input_single[x+1]}')
    for x in range(len(input_single)-2):
        input_triple.append(f'{input_single[x]} {input_single[x+1]} {input_single[x+2]}')
    inputs = input_triple + input_double + input_single

    for word in inputs:
        lookups[word] = object

def add_route(place1, place2, direction):
    match direction:
        case 'n':
            place1.routes['n'] = place2
            place2.routes['s'] = place1
        case 's':
            place1.routes['s'] = place2
            place2.routes['n'] = place1
        case 'e':
            place1.routes['e'] = place2
            place2.routes['w'] = place1
        case 'w':
            place1.routes['w'] = place2
            place2.routes['e'] = place1

def new_place(class_type, connection, direction):
    add_to_places(class_type)
    add_to_lookups(places[-1])
    add_route(connection, places[-1], direction)

def new_thing(class_type):
    add_to_things(class_type)
    add_to_lookups(things[-1])

# lookup

def lookup(object):
    return lookups.get(object)


# starting location
start = start()
places.append(start)

# other locations
new_place(forest(), start, 'n')


# thing classes inits


def food_init(self, name, heal):
    thing.__init__(self, name)
    self.heal = heal

def equipment_init(self, name, equip):
    thing.__init__(self, name)
    self.equip = equip

# thing classes

food = type('food',(thing,),{'__init__': food_init})
equipment = type('equipment',(thing,),{'__init__': equipment_init})

hat = type('hat',(equipment,),{})

# things

apple = food('apple', 50)
sword = equipment('super cool sword', 50)



# test


print(lookup('apple'))
lookup('green forest').visit()
print(start.lookup_inv('potato'))
print(start.lookup_exits('n'))
print(lookups)