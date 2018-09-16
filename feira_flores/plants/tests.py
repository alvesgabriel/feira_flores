import pytest as pytest
from django.urls import reverse

from feira_flores.django_assertions import dj_assert_contains


def test_app_link_in_home(client):
    response = client.get('/')
    dj_assert_contains(response, reverse('plants:index'))


def test_status_code(resp):
    assert 200 == resp.status_code


@pytest.fixture
def resp(client):
    return client.get(reverse('plants:index'))


@pytest.mark.parametrize(
    'content', [
        '//imagens.ecid.com.br/imagem-curso-online/curso-basico-de-bonsai-curso-online.png',
        'Bonsai',
        'Aprenda esta arte milenar do cultivo de bonsais. Saiba mais sobre a escolha de plantas, os cuidados ' +
        'necessários, os diferentes estilos e as classificações de tamanho e espécie. A abordagem vai desde o preparo' +
        ' da terra até a poda e manutenção das pequenas árvores.'
    ]
)
def test_index_content(resp, content):
    dj_assert_contains(resp, content)
