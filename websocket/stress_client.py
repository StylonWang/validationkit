#!/usr/bin/python
# -*- coding: utf-8 -*-
from ws4py.client.threadedclient import WebSocketClient
import time
import sys

class EchoClient(WebSocketClient):
    def opened(self):
        for i in range(1, 10000):
            print("%d run" % (i))
            self.send("hello web socket server!")
            time.sleep(0.1)
        self.close(reason=None)

if len(sys.argv) < 3 :
    print "Usage:", sys.argv[0], "IP port"
    exit(1)

url="ws://"+sys.argv[1]+":"+sys.argv[2]

if __name__ == '__main__':
    try:
        ws = EchoClient(url, protocols=['http-only', 'chat'])
        ws.daemon = False
        ws.connect()
    except KeyboardInterrupt:
        ws.close()
