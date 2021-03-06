from dsa.challenges.repeated_word.repeated_word import repeated_word_return

def test_one():
    actual = repeated_word_return("i love soda and soda loves me")
    expected = 'soda'
    assert actual == expected

def test_two():
    actual = repeated_word_return("i love love")
    expected = 'love'
    assert actual == expected

def test_three():
    actual = repeated_word_return("cant stand this sun it is not the sun i like")
    expected = 'sun'
    assert actual == expected

def test_four():
    actual = repeated_word_return("is it taco tuesday or is it taco tuedsay?")
    expected = 'is'
    assert actual == expected
