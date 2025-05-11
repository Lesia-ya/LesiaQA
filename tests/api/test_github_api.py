import pytest


@pytest.mark.api
def test_user_exists(github_api):
    user = get_user('defunkt')
    assert user['login'] == 'defunkt'

@pytest.mark.api
def test_user_not_exists(github_api):
    r = get_user('butenkosergii')
    assert r['message'] == 'Not Found'
