import pytest
from feira_flores.django_assertions import dj_assert_contains


def test_status_code(client):
    response = client.get('/')
    assert 200 == response.status_code


@pytest.mark.parametrize(
    'content', [
        'Feira de Flores',
        'contato@feiraflores.com.br',
        '+55 88 98765-4321',
    ]
)
def test_home(client, content):
    response = client.get('/')
    dj_assert_contains(response, content)
