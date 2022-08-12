from libpythonpro.spam.enviador_email import Enviador


def criar_enviador_email():
    enviador = Enviador()
    assert enviador is not None

def tedt_remente():
    enviador = Enviador()
    enviador.enviar(
        'joaokadota@gmail.com',
        'Cursos Python Pro',
        'Primeiro teste de envio de email'
    )