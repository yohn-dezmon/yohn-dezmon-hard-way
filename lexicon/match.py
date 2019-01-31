

def match(word_list, expecting):
    # hmmm this is a weird line... why is it just if word_list... what does this accomplish?
    if word_list:
        # this is assigning the last item in the list to word !
        word = word_list.pop(0)
        #this part checks to see if the token is of the type we're expectingself.
        if word[0] == expecting:
            return word
        else:
            return None
    else:
        return None


word_list = [('noun','player'), ('verb', 'kill'), ('noun', 'cabinet')]


### OHHHH lol ..
# I was getting confused from the documentation b/c they didn't use an index
# and the default item to be removed from a list is the last oneself.
# in our example however, we use a 0 index (i.e. the first value in the list)
word = word_list.pop(0)

print(word)
print("""
------
 """)

print(word[0])



def peek(word_list):
    # alright so this just let's you look at the first word in the tuple (I think)
    if word_list:
        word = word_list[0]
        return word[0]
    else:
        return None

# to consume a word we use the match function, which confirms that the expected
# word is the right type, takes the tuple off of the list and returns the word.
def match(word_list, expecting):
    # hmmm this is a weird line... why is it just if word_list... what does this accomplish?
    if word_list:
        # this is assigning the first tuple in the list to word !
        word = word_list.pop(0)
        #this part checks to see if the token is of the type we're expecting
        if word[0] == expecting:
            return word
        else:
            return None
    else:
        return None

def skip(word_list, word_type):
    while peek(word_list) == word_type:
    # cool, this 'pops off' the word type we want to skip...
    # I Guess it pops off the entire ('token', 'word') tuple?
        match(word_list, word_type)

def parse_verb(word_list):
    skip(word_list, 'stop')
    # here we check to see if the next word is a 'stop',
    # if it is we take it off of the list with match (method)
    # this peek if statement returns the 'verb' tuple!
    if peek(word_list) == 'verb':
        return match(word_list, 'verb')

word_type = 'noun'

b = skip(word_list, word_type)

print(word_list)

word_list = [('noun','player'), ('verb', 'kill'), ('noun', 'cabinet')]

print("""           ROUND 2""")

b = parse_verb(word_list)
print(b)
