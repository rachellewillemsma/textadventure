from classes_and_functions import *
from synonyms import * 

test_game = False


print(welcome_message)
p.location.visit()

def play():
    while True:
        # get input including up to three word phrases
        input_single = input().lower().split(' ')
        input_double = []
        input_triple = []

        for x in range(len(input_single)-1):
            input_double.append(f'{input_single[x]} {input_single[x+1]}')
        for x in range(len(input_single)-2):
            input_triple.append(f'{input_single[x]} {input_single[x+1]} {input_single[x+2]}')

        inputs = input_triple + input_double + input_single

        # reset variables
        input_verbs = []
        input_things = []
        input_npcs = []
        input_places = []
        input_directions = []
        verb = []
        direct = []
        indirect = []
        direction = []

        # reduce synonyms to main term
        for x in range(len(inputs)):
            for term in synonyms:
                for word in synonyms[term]:
                    if inputs[x] == word:
                        inputs[x] = term

        # categorize input words
        for word in inputs:
            if word in verbs:
                input_verbs.append(word)
            elif word in things:
                input_things.append(word)
            elif word in places:
                input_places.append(word)
            elif word in npcs:
                input_npcs.append(word)
            elif word in directions:
                input_directions.append(word)

        # continue to categorize
        # check if valid
        if input_verbs != []:
            verb = input_verbs[0]
            if input_directions != []:
                direction = input_directions[0]
            if input_things != []:
                direct = input_things[0]
                if input_npcs != []:
                    indirect = input_npcs[0]
                elif input_places != []:
                    indirect = input_places[0]
            elif input_npcs != []:
                direct = input_npcs[0]
                if input_places != []:
                    indirect = input_places[0]
            elif input_places != []:
                direct = input_places[0]
        elif input_directions != []:
            direction = input_directions[0]
        else:
            print('you must include an action.')

        # connect input to function
        if verb == 'take':
            take(direct)

        elif verb == 'drop':
            drop(direct)

        elif verb == 'inventory':
            inventory()
        
        elif verb == 'look':
            look(direct)
        
        elif verb == 'go':
            if direction:
                go(direction)
            else:
                go(direct)

        # less common / semantically abiguous terms should be toward the bottom of this list
    
        elif verb == 'rest':
            rest()

        elif verb == 'quit':
            print('are you sure? (yes/no)')
            confirm = input().lower().split()
            for word in confirm:
                if word in yeses:
                    print('goodbye, adventurer')
                    quit()
                elif word in nos:
                    pass
                else:
                    pass
        
        # only exception to verb needed rule

        elif direction:
            go(direction)
        
        else:
            pass # this should not be possible – raise error

        # testing stuff goes here

        if test_game:
            print(f'\n--- INFO ---')
            print(f'your input was: {inputs}')
            print(f'verb: {verb}')
            print(f'direct: {direct}')
            print(f'indirect: {indirect}')
            print(f'direction: {direction}')

play()