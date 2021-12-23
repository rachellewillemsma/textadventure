vowels = ['a','e','i','o','u']

lookups = {} # leave empty
places = [] # leave empty
things = [] # leave empty

class player:
    def __init__(self, location):
        self.location = location
        self.inv = {}



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
        # if there is already an entry, append to it
        if word in lookups.keys():
            lookups[word].append(object)
        # if not, create one
        else:
            lookups[word] = [object]





# THINGS

def new_thing(class_type):
    add_to_things(class_type)
    add_to_lookups(things[-1])

def add_to_things(class_type):
    things.append([class_type][0])


class thing:
    def __init__(self, name):
        self.name = name
        new_thing(self)

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
sword = equipment('green apple', 50)





# PLACES

class place():
    def __init__(self):
        self.inv = {}
        self.routes = {}
          
    def visit(self):
        p.location = self
        print(f'\033[1m--- {self.name} ---\033[0m')
        print(self.desc, end='.\n')

    def lookup_inv(self, object):
        if object in self.inv.keys():
            return self.inv.get(object)
        else:
            return 'that is not here'

    def lookup_exits(self, direction):
        if direction in self.routes.keys():
            return self.routes.get(direction)
        else:
            return 'that is not here'

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







# lookup

def lookup(object):
    if len(lookups.get(object)) == 1:
        return lookups.get(object)[0]
    else:
        candidates = []
        exact_matches = []
        for obj in lookups.get(object):
            for item in p.location.inv:
                if obj == item:
                    candidates.append(obj)
            for item in p.inv:
                if obj == item:
                    candidates.append(obj)
        if len(candidates) == 1:
            return candidates[0]
        elif candidates:
            for cand in candidates:
                if len(cand) == len(object):
                    exact_matches.append(cand)

            if len(exact_matches) == 1:
                return exact_matches[0]
            elif exact_matches:
                pass
            else:
                for cand in candidates:
                    print(f'{cand} remains a candidate')
                    print(f'did you mean', end=' ')
                    print(f'{cand}', sep=', ', end='?')

        else:
            return "you don't see that here."

        # UNFINISHED right now it simply gets the first listed object under the term
        # EDGE CASE UNADRESSED!! what if one apple in inv and one on ground, and try to eat? must eat apple in inv!

        # instead the process should be a bit more complex...
        # EXAMPLE LOOKUP: "tree" | EXAMPLE LISTED OBJS: ["apple tree", "pear tree", "tree", "tree", "tree"]
        # Step 1: check which one of the listed objects is actually in the vicinity or in player inv
        # Result a: there is no tree in the vicinity
            ##### return message saying such
        # Result b: there is only one tree in the vicinity
            ##### return tree
        # Result c: there are multiple trees in the vicinity
            # Step 2: determine if any results share the same number of words as the input
                # Result a: only one object shares the same number of words
                ##### return tree
                # Result b: several objects share the same number of words
                ##### return all objects (action will be performed on all) #### EDGE CASES HERE ####
                # Result c: all objects have more words than the input
                    # Step 3: print(f'which {input} do you mean, the {result1} or the {result2}?')
                    # Case a: player types result1 or result2 in full
                        ##### Return result
                    # Case b: player types only the part of result1 or result2 which they did not type before
                        ##### Return result
                    # Case c: player types something else
                        ##### Pass (return to regular input)
                    



# starting location
start = start()
places.append(start)
p = player(start)

# other locations
new_place(forest(), start, 'n')






# test

hey = lookup('apple')
print(hey)
lookup('green forest').visit()
print(start.lookup_inv('potato'))
print(start.lookup_exits('n'))