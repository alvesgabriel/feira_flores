import pytest
from feira_flores.django_assertions import dj_assert_contains


def test_home_status_code(client):
    response = client.get('/')
    assert 200 == response.status_code


@pytest.mark.parametrize(
    'content', [
        'Feira de Flores',
        'contato@feiraflores.com.br',
        '+55 (88) 2101-5444',
        'href="/contato"',
    ]
)
def test_home(client, content):
    response = client.get('/')
    dj_assert_contains(response, content)


def test_contact_status_code(client):
    response = client.get('/contato/')
    assert 200 == response.status_code


@pytest.mark.parametrize(
    'content', [
        'contato@feiraflores.com.br',
        '(88) 2101-5444',
        'Av. Padre Cícero, 2555 - Triângulo',
        'Juazeiro do Norte - CE',
        '63041-145',
    ]
)
def test_contact_content(client, content):
    response = client.get('/contato/')
    dj_assert_contains(response, content)
