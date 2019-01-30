# the import as such was necessary for pytest to run... but the directory NAME
# needs to be removed if you are to actually run the parser.py file
# I had my tests in test folder and my scripts in a folder called NAME both within a project folder.
from NAME.lexicon import lexicon



class ParserError(Exception):
    # wait where is this getting Exception from?
    # oh from the parser methods.
    pass

class Sentence(object):

    def __init__(self, subject, verb, obj):
        # we take tuples ('token', 'word') and convert them
        # here the 1 indicaets the actual word in the tuple
        # in the other parsers we extract the tuples
        # based upon their tokens
        self.subject = subject[1]
        self.verb = verb[1]
        self.object = obj[1]

# def __init__(word_list):
#
#     self.word_list = word_list

def peek(word_list):
    # alright so this just let's you look at the first word in the FIRST tuple
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
    # I Guess it pops off the entire ('token', 'word') tuple
        match(word_list, word_type)

def parse_verb(word_list):
    skip(word_list, 'stop')

    # here we check to see if the next word is a 'stop',
    # if it is we take it off of the list with match (method)
    # this peek if statement returns the 'verb' tuple!
    if peek(word_list) == 'verb':
        return match(word_list, 'verb')
    else:
        raise ParserError("Expected a verb next.")

def parse_object(word_list):
    skip(word_list, 'stop')
    next_word = peek(word_list)

    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'direction':
        return match(word_list, 'direction')
    else:
        raise ParserError("Expected a noun or direction next.")

def parse_subject(word_list):
    skip(word_list, 'stop')
    next_word = peek(word_list)

    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'verb':
        return ('noun', 'player')
    else:
        raise ParserError("Expected a verb next.")

def parse_sentence(word_list):
    # I think the order here is important and is what determines that
    # the parser knows what is an object and what is a subject
    # since the subject parser function is run first! yay!
    subj = parse_subject(word_list)
    verb = parse_verb(word_list)
    obj = parse_object(word_list)


    return Sentence(subj, verb, obj)
