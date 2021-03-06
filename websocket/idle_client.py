#!/usr/bin/python
# -*- coding: utf-8 -*-
from ws4py.client.threadedclient import WebSocketClient
import sys

class EchoClient(WebSocketClient):
    def opened(self):
        self.send("hello web socket server!")

    def received_message(self, m):
        print("=> %d %s" % (len(m), str(m)))

if len(sys.argv) < 3 :
    print "Usage:", sys.argv[0], "IP port"
    exit(1)

url="ws://"+sys.argv[1]+":"+sys.argv[2]
print url

if __name__ == '__main__':
    try:
        ws = EchoClient(url, protocols=['http-only', 'chat'])
        ws.daemon = False
        ws.connect()
    except KeyboardInterrupt:
        ws.close()


