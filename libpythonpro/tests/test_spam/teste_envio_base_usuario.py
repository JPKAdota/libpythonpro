from unittest.mock import Mock

import pytest

from libpythonpro.spam.enviador_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Joao', email='joaokadota@gmail.com'),
            Usuario(nome='Kadota', email='joaokadota@gmail.com')
        ],
        [
            Usuario(nome='Joao', email='joaokadota@gmail.com')
        ]
    ]
)
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'Joaokadota@gmail.com',
        'Curso python',
        'confira os módulos'
    )
    assert len(usuarios) == enviador.enviar.call_count

def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Kadota', email='joaokadota@gmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'kadotata@gmail.com',
        'Curso python',
        'confira os módulos'
    )
    enviador.enviar.assert_called_once_with (
        'kadotata@gmail.com',
        'joaokadota@gmail.com',
        'Curso python',
        'confira os módulos'
    )
