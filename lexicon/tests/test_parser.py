import pytest

import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, '/Users/HomeFolder/projects/lexicon/modules')

from parser import Parser


# I've engeineered each test such that it has a failure and a success.

word_list_SVO = [('noun','player'), ('verb', 'kill'), ('noun', 'cabinet')]
word_list_VO = [('verb', 'kill'), ('noun', 'cabinet')]
word_list_sVO = [('stop','it'), ('verb', 'kill'), ('noun', 'cabinet')]
word_list_noV = [('stop','it'), ('noun', 'cabinet')]
word_list_direc = [('verb', 'go'), ('direction', 'east')]


# it is not necessary to explicitly call the Sentence class
# (b/c Parser instantiates Sentence eventually)

parser_SVO = Parser(word_list_SVO)
parser_VO = Parser(word_list_VO)
parser_sVO = Parser(word_list_sVO)
parser_noV = Parser(word_list_noV)
parser_direc = Parser(word_list_direc)

@pytest.fixture
def fixtcha_():
    # I probably don't need these any more...
    global word_list_SVO
    global word_list_VO
    global word_list_sVO
    global word_list_noV
    global word_list_direc

    global parser_SVO
    global parser_VO
    global parser_sVO
    global parser_noV
    global parser_direc

def test_init(fixtcha_):

    assert parser_SVO.word_list == word_list_SVO
    assert parser_VO.word_list == word_list_VO
    assert parser_sVO.word_list == word_list_sVO
    assert parser_noV.word_list == word_list_noV
    assert parser_direc.word_list == word_list_direc


def test_peek(fixtcha_):
    result_SVO = parser_SVO.peek()
    result_VO = parser_VO.peek()

# pass:
    assert result_SVO == 'noun'
    # fail:
    assert result_VO == 'noun'
    # pass:
    assert result_VO == 'verb'

def test_match(fixtcha_):
    expecting = 'noun'
    result_SVO = parser_SVO.match(expecting)
    result_VO = parser_VO.match(expecting)

    # the reason the final outcome of this is the tuple and not the token
    # is because the end of the function is return word
    # not return word[0]

    assert result_SVO == ('noun', 'player')
    assert result_VO == ('verb', 'fool')

def test_skip(fixtcha_):
    word_type = 'stop'
    word_type_1 = 'noun'

    result = parser_sVO.skip(word_type)
    result_1 = parser_SVO.skip(word_type_1)

    assert word_list_sVO == [('verb', 'kill'), ('noun', 'cabinet')]
    assert word_list_SVO == [('noun','player'), ('verb', 'kill'), ('noun', 'cabinet')]

def test_verb(fixtcha_):
    # wait why does parse_verb(word_list_SVO) work and parse_verb(word_list_VO) not work...
    # b/c parse_test() doesn't have a next_word = peek(word_list)
    # so it won't recognize a verb if it is the first tuple, it only recognizes
    # verbs if it's the next one over from the first, or even second from the first! GOT IT!
    # Passing test:
    result_pass = parser_sVO.parse_verb(word_list_sVO)
    assert result_pass == ('verb', 'kill')

# once again here SVO doesn't raise an error but VO does
    with pytest.raises(ParserError, match='Expected a verb next.'):
         parser_VO.parse_verb(word_list_VO)

def test_object(fixtcha_):

# passes!
    result_obj = parser_sVO.parse_object(word_list_sVO)
# Fails! (as it should b/c there is a verb in the way, causing the error to raise.)
    result_direc = parser_direc.parse_object(word_list_direc)

    assert result_obj == ('noun', 'cabinet')
    assert result_direct == ('direction', 'east')

def test_subject(fixtcha_):

# passes!
    result_subj = parser_VO.parse_subject(word_list_VO)
    # passes!
    result_b_subj = parser_SVO.parse_subject(word_list_SVO)

    # raises an error!
    with pytest.raises(ParserError, match='Expected a verb next.'):
         parser_noV.parse_verb(word_list_noV)

def test_sentence(fixtcha_):
    subj = ('noun', 'bear')
    verb = ('verb', 'go')
    obj = ('noun', 'cabinet')

    sentence_result = Sentence(subj, verb, obj)

    assert sentence_result.subject == 'bear'
    assert sentence_result.verb == 'go'
    # should fail!
    assert sentence_result.subject == 'cabinet'
    assert sentence_result.object == 'cabinet'
