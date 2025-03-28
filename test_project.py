from project import word_generator, accuracy, time_difference

def test_word_generator():
    assert len(word_generator(10)) == 10
    assert len(word_generator(100)) == 100

def test_accuracy():
    a = "The quick brown fox jumps over the lazy dog"
    b = "The quik brown fix jumps over teh lazi dog"
    assert accuracy(a,b) == "82.86"

def test_time_difference():
    a = '12:30:00'
    b = '12:31:30'
    c = '12:31:45'
    assert time_difference(a,b) == 1.5
    assert time_difference(a,c) == 1.75


test_accuracy()


