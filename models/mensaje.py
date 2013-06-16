#!/usr/bin/env python
# encoding: utf-8

class Mensaje(object):
    _autor = None   # nombre completo del autor
    _alias = None   # alias en Bitacoras.com del autor
    _avatar = None  # imagen del usuario (32x32px)
    _fecha = None   # fecha de publicación
    _texto = None   # contenido filtrado, con etiquetas HTML