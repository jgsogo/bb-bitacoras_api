#!/usr/bin/env python
# encoding: utf-8

class Actividad(object):
    _url = None     # URL de la actividad: anotación, usuario,...
    _tipo = None    # tipo de actividad (anotación, voto, comentario,...)
    _alias = None   # alias en Bitacoras.com del autor
    _avatar = None  # imagen del usuario (32x32px)
    _fecha = None   # fecha de publicación
    _texto = None   # texto descriptivo, con etiquetas HTML