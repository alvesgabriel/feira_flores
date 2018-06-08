from unittest.mock import Mock

import pytest

from feira_flores.spam.main import EnviadorDeSpam
from feira_flores.spam.models import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Gabriel', email='gabriel.alves.monteiro1@gmail.com'),
            Usuario(nome='Ana Isa', email='aaisa.af91@gmail.com'),
        ],
        [
            Usuario(nome='Gabriel', email='gabriel.alves.monteiro1@gmail.com'),
        ]
    ]
)
def test_qtd_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'gabriel.alves.monteiro1@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Gabriel', email='gabriel.alves.monteiro1@gmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'aaisa.af91@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
    enviador.enviar.assert_called_once_with(
        'aaisa.af91@gmail.com',
        'gabriel.alves.monteiro1@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
