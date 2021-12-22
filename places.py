vowels = ['a','e','i','o','u']


class player:
    def __init__(self):
        pass

p = player()

# making sure routes between places should be reciprocal
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

class place():
    def __init__(self):
        self.content = {}
        self.routes = {}
          
    def visit(self):
        p.location = self
        print(f'\033[1m--- {self.name} ---\033[0m')
        print(self.desc, end='.')

# classes – will manually add

start = type('start',(place,),{
    'name': 'start', 
    'desc': 'a really nice start'})
forest = type('forest',(place,),{
    'name': 'green forest', 
    'desc': 'a really nice forest', 'direction': 'unknown'})
plains = type('meadow',(place,),{
    'name': 'meadow', 
    'desc': 'a really nice meadow'})

# instances
objs = []
lookups = {}

start = start()
objs.append(start)



def add_to_objs(class_type):
    objs.append([class_type][0])

def add_to_data(object):
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
        lookups[word] = objs[-1]

def new_place(class_type, connection, direction):
    add_to_objs(class_type)
    add_to_data(objs[-1])
    add_route(connection, objs[-1], direction)


new_place(forest(), start, 'n')

# test

print(objs)
print(lookups)