from feira_flores.spam.models import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Gabriel', email='gabriel.alves.monteiro1@gmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [
        Usuario(nome='Gabriel', email='gabriel.alves.monteiro1@gmail.com'),
        Usuario(nome='Ana Isa', email='aaisa.af91@gmail.com'),
    ]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
