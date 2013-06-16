#!/usr/bin/env python
# encoding: utf-8

class BitacorasException(Exception):
    pass

class BitacorasBadRequest(BitacorasException):
    pass

class BitacorasNotAuthorized(BitacorasException):
    pass

class BitacorasNotFound(BitacorasException):
    pass

class BitacorasInternalServerError(BitacorasException):
    pass
