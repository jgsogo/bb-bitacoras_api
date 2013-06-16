#!/usr/bin/env python
# encoding: utf-8

try: # python 3.x
    import html.parser as html_parser
except ImportError: # fallback for python 2.x
    import HTMLParser as html_parser

class Anotacion(object):

    _autor = None       # nombre completo del autor
    _alias = None       # alias en Bitacoras.com del autor
    _avatar = None      # imagen del usuario (32x32px)
    _fecha = None       # fecha de publicación
    _votos = None       # número de votos
    _url = None         # dirección completa de la anotación
    _bitacora = None    # dirección completa de la bitácora
    _nombre = None      # nombre completo de la bitácora
    _titulo = None      # título completo
    _contenido = None   # resumen del contenido sin etiquetas HTML

    @classmethod
    def from_json(cls, data):
        parser_html = html_parser.HTMLParser()
        instance = Anotacion()
        instance._alias = parser_html.unescape(data['alias'])
        instance._autor = parser_html.unescape(data['autor'])
        instance._bitacora = data['bitacora']
        instance._contenido = parser_html.unescape(data['contenido'])
        instance._fecha = data['fecha']
        instance._nombre = parser_html.unescape(data['nombre'])
        instance._titulo = parser_html.unescape(data['titulo'])
        instance._url = data['url']
        instance._votos = data['votos']
        return instance
