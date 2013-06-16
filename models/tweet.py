#!/usr/bin/env python
# encoding: utf-8


class Tweet(object):
    _id = None          # identificador (status)
    _alias = None       # alias en Twitter.com del autor
    _avatar = None      # imagen del usuario
    _fecha = None       # fecha de publicación
    _url = None         # dirección completa del tweet
    _contenido = None   # texto del tweet

    @classmethod
    def from_json(cls, data):
        instance = Tweet()
        instance._id = data['id']
        instance._alias = data['alias']
        instance._avatar = data['avatar']
        instance._fecha = data['fecha']
        instance._url = data['url']
        instance._contenido = data['contenido']
        return instance