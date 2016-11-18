# -*- coding: utf-8 -*-
#
# @author: Daemon Wang
# Created on 2016-03-02
#

from tornado.options import options

import sys

class StatusModel(object):
    _key = None
    _value = None
    _desc = None

    def __init__(self,status):
        self._key = status[0]
        self._value = status[1]
        self._desc = status[2]

    def get(self):
        return ({("%s"%self._key).lower():self._value},{("%s_desc"%self._key).lower():self._desc})

class Status(object):
    class ConstError(TypeError): pass

    def __setattr__(self, key, value):
        if self.__dict__.has_key(key):
            raise self.StatusError, "Changing Status.%s" % key
        else:
            self.__dict__[key] = value
            for v in value:
                self.__dict__["%s_%s"%(key,v[0].upper())] = {"value":v[1],"desc":v[2]}

    def __getattr__(self, key):
        if self.__dict__.has_key(key):
            return self.key
        else:
            return None

    def desc(self,key,value):
        result = None
        if key in self.__dict__:
            for v in self.__dict__[key]:
                if v[1] == value:
                    result = StatusModel(v)
        return result

sys.modules[__name__] = Status()


