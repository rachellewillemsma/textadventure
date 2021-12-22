# synonyms list
synonyms = {
# directions
'n': ['n', 'north', 'northward'],
's': ['s', 'south', 'southward'],
'e': ['e', 'east', 'eastward'],
'w': ['w', 'west', 'westward'],
'up': ['up', 'ascend', 'get up'],
'down': ['down', 'descend', 'get down'],
# verbs
'go': ['go', 'walk', 'travel', 'move', 'wander', 'set off', 'voyage', 'explore', 'stroll', 'get to', 'enter', 'into'],
'exit': ['exit', 'leave', 'outta', 'get out'],
'look': ['x', 'look', 'examine', 'check', 'inspect'],
'consume': ['eat', 'drink', 'consume', 'munch', 'monch', 'chow down', 'slurp'],
'talk': ['talk', 'chat', 'speak', 'ask', 'address', 'inquire', 'tell', 'notify', 'say', 'explain', 'describe', 'shout', 'yell', 'scream'],
'equip': ['equip', 'put on', 'wear', 'don'],
'unequip': ['unequip', 'take off', 'remove', 'doff'],
'hit': ['hit', 'punch', 'stab', 'attack', 'cut'],
'shoot': ['shoot', 'open fire', 'fire at', 'let loose on'],
'buy': ['buy', 'purchase'],
'sell': ['sell', 'peddle'],
'take': ['take', 'pick up', 'gather', 'obtain', 'carry', 'hold', 'get', 'grab', 'nab', 'collect'],
'drop': ['drop', 'put down', 'discard', 'release', 'get rid of', 'let go of'],
'inventory': ['i', 'inventory'],
'quit': ['q', 'quit', 'quit game', 'end game', 'exit game']
}


# type lists

yeses = ['y', 'yes', 'ye', 'yep', 'yea', 'okay', 'ok', 'affirmative', 'confirm']
nos = ['no', 'nah', 'nope', 'nay', 'nae', 'negative']

directions = []
for term in ({k: synonyms[k] for k in list(synonyms)[:6]}):
    for word in synonyms[term]:
        directions.append(word)

verbs = []
for term in ({k: synonyms[k] for k in list(synonyms)[6:]}):
    for word in synonyms[term]:
        verbs.append(word)