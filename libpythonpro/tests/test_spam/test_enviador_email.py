import pytest

from libpythonpro.spam.enviador_email import Enviador, EmailInvalido


def criar_enviador_email():
    enviador = Enviador()
    assert enviador is not None

@pytest.mark.parametrize(
    'remetente',
    ['joaokadota@gmail.com', 'ildakadota@hotmail.com']
)
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente,
        'joaokadota@hotmail.com'
        'Cursos Python Pro',
        'Primeiro teste de envio de email .',
        'mandando email'
    )
    assert remetente in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'ildakadota']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'joaokadota@hotmail.com'
            'Cursos Python Pro',
            'Primeiro teste de envio de email .',
            'mandando email'
    )