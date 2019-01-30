class lexicon(object):

    def scan(self, stuff):
        # stuff = input('> ')
        words = stuff.split()
        directions = ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back']
        verbs = ['go', 'stop', 'kill', 'eat']
        stop_words = ['the', 'in', 'of', 'from', 'at', 'it']
        nouns = ['door', 'player', 'bear', 'princess', 'cabinet']
        tuple_sent = []
        # the test is looking for a tuple ( which .split produces) within a list...
        for w in words:
            if w.lower() in directions:
                word = ('direction', w.lower())
                tuple_sent.append(word)
            elif w.lower() in verbs:
                word = ('verb', w.lower())
                tuple_sent.append(word)
            elif w.lower() in stop_words:
                word = ('stop', w.lower())
                tuple_sent.append(word)
            elif w.lower() in nouns:
                word = ('noun', w.lower())
                tuple_sent.append(word)
            elif w.isdigit():
                number = ('number', int(w))
                tuple_sent.append(number)
            else:
                err = ('error', w)
                tuple_sent.append(err)
        # If you don't have RETURN here, the nosetests will return
        # AssertionError: None != [('direction', 'north')]
        return tuple_sent


#
 # .isdigit() this method returns true if all characters in teh string are
 # digits and there is at least one character, false otherwise.
# b = scan("go north please")
# print(b)
#
# print("""
#
#
# """)
#
# c = "go north please"
# d = c.split()
# print(d)
