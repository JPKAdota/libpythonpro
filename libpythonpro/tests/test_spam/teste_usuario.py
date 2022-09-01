from libpythonpro.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Joao', email='joaokadota@gmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)

def test_listar_usuario(sessao):
    usuarios = [Usuario(nome='Joao', email='joaokadota@gmail.com'),
                Usuario(nome='Kadota', email='joaokadota@gmail.com')
                ]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()

