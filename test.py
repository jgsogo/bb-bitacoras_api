
from config import BITACORAS_API_KEY
from api import Client

from pprint import pprint

def run():
    bitacoras = Client(BITACORAS_API_KEY)

    portada = bitacoras.portada()
    for post in portada:
        print "[" + post._votos + "]" + post._titulo + " (" + post._url + ")"

run()
