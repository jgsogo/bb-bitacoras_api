#!/usr/bin/env python
# encoding: utf-8

import requests
from exceptions import (BitacorasBadRequest, BitacorasNotAuthorized, BitacorasNotFound, BitacorasInternalServerError)
from ..models import Actividad, Anotacion, Mensaje, Tweet, Usuario

class Client(object):
    _key = None
    _endpoint = 'http://api.bitacoras.com'
    _format = 'json'

    def __init__(self, key, format='json'):
        self._key = key
        self._format = format

    def _get_url(self, method):
        return '/'.join((self._endpoint, method))

    def _get_params(self):
        return {'key' : self._key, 'format': self._format}

    def _handle_error(self, r):
        status_code = r.status_code
        if status_code == 400: # Bad request
            raise BitacorasBadRequest()
        elif status_code == 401: # Not Authorized
            raise BitacorasNotAuthorized()
        elif status_code == 404: # Not Found
            raise BitacorasNotFound()
        elif status_code == 500: # Internal Server Error
            raise BitacorasInternalServerError()

    def _make_request(self, url, params):
        r = requests.post(url, params)
        if r.status_code == 200:
            return r
        else:
            return self._handle_error(r)

    def _build_queryset(self, response, query_class):
        if self._format == 'json':
            queryset = []
            for item in response.json()['data']:
                queryset.append(query_class.from_json(item))
            return queryset
        else:
            raise Exception("Not implemented")

    # API methods
    def anotacion(self, anotacion_url):
        url = self._get_url('anotacion')
        params = self._get_params()
        params.update({'url':anotacion_url})
        r = self._make_request(url, params)
        return self._build_queryset(r, Anotacion)

    def portada(self):
        url = self._get_url('portada')
        params = self._get_params()
        r = self._make_request(url, params)
        return self._build_queryset(r, Anotacion)

    def hemeroteca(self):
        raise NotImplementedError()

    def canales(self, canal):
        url = self._get_url('canales')
        params = self._get_params()
        params.update({'etiqueta':canal})
        r = self._make_request(url, params)
        return self._build_queryset(r, Anotacion)

    def buscar(self, busqueda, ciudad=None):
        url = self._get_url('buscar')
        params = self._get_params()
        params.update({'busqueda':busqueda})
        if ciudad:
            params.update({'ciudad':ciudad})
        r = self._make_request(url, params)
        return self._build_queryset(r, Anotacion)

    def geo(self):
        raise NotImplementedError()

    def retweets(self, anotacion_url):
        url = self._get_url('retweets')
        params = self._get_params()
        params.update({'url':anotacion_url})
        r = self._make_request(url, params)
        return self._build_queryset(r, Anotacion)

    def canal_usuario(self):
        raise NotImplementedError()

    def recomendaciones(self):
        raise NotImplementedError()

    def descubrimientos(self):
        raise NotImplementedError()

    def comentadas(self):
        raise NotImplementedError()

    def sigue_a(self):
        raise NotImplementedError()

    def le_siguen(self):
        raise NotImplementedError()

    def comunidad(self):
        raise NotImplementedError()

    def comentarios(self):
        raise NotImplementedError()

    def usuario(self):
        raise NotImplementedError()

    def usuarios(self):
        raise NotImplementedError()

    def recibidos(self):
        raise NotImplementedError()

    def inbox(self):
        raise NotImplementedError()

    def top_bitacoras(self):
        raise NotImplementedError()

    def top_usuarios(self):
        raise NotImplementedError()

