#!/usr/bin/python

import requests
from jsonrpclib import jsonrpc

username = ''
password = ''
# site address
host = '

class Nzbget(object):
    def __init__(self, username, password, host):
        if username and password:
            authstring = '%s:%s@' % (username, password)
        else:
            authstring = ''

        self.url = 'https://%s%s/jsonrpc' % (authstring, host)
        self.action = jsonrpc.ServerProxy(self.url)

    def pause(self):
        print('Paused nzbget')
        return self.action.pause()

    def resume(self):
        print('Resumed nbzbget')
        return self.action.resume()

client = Nzbget(host=host, username=username, password=password)

client.resume()
