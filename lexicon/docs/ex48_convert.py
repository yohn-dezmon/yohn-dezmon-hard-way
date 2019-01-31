def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None

# this catches an input that isn't a number and instead returns Noneself.

# use this test in your scanner to test whether something is a Number
# and also as the last thing you check before declaring a word an error .
