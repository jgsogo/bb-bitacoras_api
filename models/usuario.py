#!/usr/bin/env python
# encoding: utf-8


class Usuario(object):
    _alias = None       # alias en Bitacoras.com
    _avatar = None      # imagen del usuario (32x32px)
    _descripcion = None # pequeña descripción
    _nombre = None      # nombre completo
    _pais = None        # país, si se ha indicado
    _ciudad = None      # ciudad, si se ha indicado

    @classmethod
    def from_json(cls, data):
        instance = Usuario()
        instance._alias = data['alias']
        instance._avatar = data['avatar']
        instance._descripcion = data['descripcion']
        instance._nombre = data['nombre']
        instance._pais = data['pais']
        instance._ciudad = data['ciudad']
        return instance