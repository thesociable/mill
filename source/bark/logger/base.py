# :coding: utf-8
# :copyright: Copyright (c) 2013 Martin Pengelly-Phillips
# :license: See LICENSE.txt.

import copy

import bark
from .log import Log


class Logger(Log):
    '''Helper for emitting logs.

    A logger can be used to preset common information (such as a name) and then
    emit :py:class:`~bark.log.Log` records with that information already
    present.

    '''

    def __init__(self, _handle=bark.handle, **kw):
        '''Initialise logger.

        If you need to override the default handle then pass in a custom
        *_handle*

        '''
        super(Logger, self).__init__(**kw)
        self._handle = _handle

    def prepare(self, *args, **kw):
        '''Prepare and return a log for emission.

        *kw* arguments are automatically mixed in to a
        :py:class:`~bark.log.Log` record made by copying this current logger.

        '''
        log = copy.deepcopy(self)
        log.update(**kw)
        return log

    def log(self, *args, **kw):
        '''Emit a :py:class:`~bark.log.Log` record.'''
        log = self.prepare(*args, **kw)
        self._handle(log)
