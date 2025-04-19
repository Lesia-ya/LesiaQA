import pytest


class User:

    def __init__(self) -> None:
        self.name = 'Sergii'
        self.second_name = 'Butenko'


@pytest.fixture
def user():
    yield user


def test_remove_name(user):
    user.name = ''
    assert user.name == ''


def test_name(user):
    assert user.name == 'Sergii'


def test_second_name(user):
    assert user.second_name == 'Butenko'
