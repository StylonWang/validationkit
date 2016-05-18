# -*- coding: utf-8 -*-
from ws4py.client.threadedclient import WebSocketClient

class EchoClient(WebSocketClient):
    def opened(self):
        self.send("hello web socket server!")
        #self.close(reason=None)

    #def closed(self, code, reason):
        #print(("Closed down", code, reason))

if __name__ == '__main__':
    try:
        ws = EchoClient('ws://10.1.9.109:9310', protocols=['http-only', 'chat'])
        ws.daemon = False
        ws.connect()
    except KeyboardInterrupt:
        ws.close()
