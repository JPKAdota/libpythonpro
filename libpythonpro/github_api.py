import request
import requests


def buscar_avatar (usuario):
    url = f'https://api.github.com/users/{usuario}'
    resp = requests.get (url)
    return resp.json()['avatar_url']

