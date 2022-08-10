import request
import requests


def buscar_avatar (usuario):
    url = f'https://api.github.com/users/JPKAdota'
    resp = requests.get (url)
    return resp.json()['avatar_url']

if __name__ == '__main__':
    print(buscar_avatar('JPKAdota'))
