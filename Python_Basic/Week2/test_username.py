from username_exception import username


def test_username_test_1():
    assert (True == username('sakir123'))


def test_username_test_2():
    assert (False == username('abc'))


def test_username_test_3():
    assert (True == username('sakir1'))
