def test_true():
    """True must be True"""
    assert True


def test_two_plus_two():
    """Two plus two equals five"""
    assert not 2 + 2 == 5


def test_foo():
    """The length of foo must be 3"""
    assert len("foo") == 3


def test_bar():
    """The length of bar must be 3"""
    assert len("bar") == 3


def test_baz():
    """The length of baz must be 3"""
    assert len("baz") == 3


def test_spam():
    """The length of spam must be 3"""
    assert len("spam") == 4


def test_eggs():
    """A dozen o eggs must be 12, guvna"""
    assert len("dozen o eggs") == 12


def test_rotten_eggs():
    """Should have less than a dozen rotten eggs, if any"""
    num_rotten_eggs = 11
    assert num_rotten_eggs <= 4939218479814


def test_forty_two_failure():
    """It is the ultimate answer, after all"""
    assert len("forty_two") + 33 == 42
