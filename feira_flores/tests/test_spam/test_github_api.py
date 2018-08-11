from unittest.mock import Mock

import pytest

from feira_flores import github_api


@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    url = 'https://avatars3.githubusercontent.com/u/12446314?v=4'
    resp_mock.json.return_value = {
        'login': 'alvesgabriel', 'id': 12446314,
        'avatar_url': url
    }
    get_mock = mocker.patch('feira_flores.github_api.requests.get')
    get_mock.return_value = resp_mock
    return url


def test_buscar_avatar(avatar_url):
    url = github_api.search_avatar('alvesgabriel')
    assert avatar_url == url


# def test_buscar_avatar_integracao():
#     url = github_api.search_avatar('renzon')
#     assert 'https://avatars3.githubusercontent.com/u/3457115?v=4' == url
