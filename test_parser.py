import pytest
from NAME.parser import *

# I've engeineered each test such that it has a failure and a success.

word_list_SVO = [('noun','player'), ('verb', 'kill'), ('noun', 'cabinet')]
word_list_VO = [('verb', 'kill'), ('noun', 'cabinet')]
word_list_sVO = [('stop','it'), ('verb', 'kill'), ('noun', 'cabinet')]
word_list_noV = [('stop','it'), ('noun', 'cabinet')]
word_list_direc = [('verb', 'go'), ('direction', 'east')]

@pytest.fixture
def fixtcha_():
    global word_list_SVO
    global word_list_VO
    global word_list_sVO

def test_peek():
    result_SVO = peek(word_list_SVO)
    result_VO = peek(word_list_VO)

    assert result_SVO == 'noun'
    assert result_VO == 'noun'
    assert result_VO == 'verb'

def test_match():
    expecting = 'noun'
    result_SVO = match(word_list_SVO, expecting)
    result_VO = match(word_list_VO, expecting)

    # the reason the final outcome of this is the tuple and not the token
    # is because the end of the function is return word
    # not return word[0]

    assert result_SVO == ('noun', 'player')
    assert result_VO == ('verb', 'fool')

def test_skip():
    word_type = 'stop'
    word_type_1 = 'noun'

    result = skip(word_list_sVO, word_type)
    result_1 = skip(word_list_SVO, word_type_1)

    # interesting, this is hard to test b/c it is just a while loop that gets
    # rid of stop token tuples...

    assert word_list_sVO == [('verb', 'kill'), ('noun', 'cabinet')]
    assert word_list_SVO == [('noun','player'), ('verb', 'kill'), ('noun', 'cabinet')]

def test_verb():
    # wait why does parse_verb(word_list_SVO) work and parse_verb(word_list_VO) not work...
    # b/c parse_test() doesn't have a next_word = peek(word_list)
    # so it won't recognize a verb if it is the first tuple, it only recognizes
    # verbs if it's the next one over from the first, or even second from the first! GOT IT!
    # Passing test:
    result_pass = parse_verb(word_list_sVO)
    assert result_pass == ('verb', 'kill')

# once again here SVO doesn't raise an error but VO does
    with pytest.raises(ParserError, match='Expected a verb next.'):
         parse_verb(word_list_VO)

def test_object():

# passes!
    result_obj = parse_object(word_list_sVO)
# Fails! (as it should b/c there is a verb in the way, causing the error to raise.)
    result_direc = parse_object(word_list_direc)

    assert result_obj == ('noun', 'cabinet')
    assert result_direct == ('direction', 'east')

def test_subject():

# passes!
    result_subj = parse_subject(word_list_VO)
    # passes!
    result_b_subj = parse_subject(word_list_SVO)

    # raises an error!
    with pytest.raises(ParserError, match='Expected a verb next.'):
         parse_verb(word_list_noV)

def test_sentence():
    subj = ('noun', 'bear')
    verb = ('verb', 'go')
    obj = ('noun', 'cabinet')

    sentence_result = Sentence(subj, verb, obj)

    assert sentence_result.subject == 'bear'
    assert sentence_result.verb == 'go'
    # should fail!
    assert sentence_result.subject == 'cabinet'
    assert sentence_result.object == 'cabinet'
