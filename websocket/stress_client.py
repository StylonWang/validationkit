# -*- coding: utf-8 -*-
from ws4py.client.threadedclient import WebSocketClient
import time

class EchoClient(WebSocketClient):
    def opened(self):
        for i in range(1, 10000):
            print("%d run" % (i))
            self.send("hello web socket server!")
            time.sleep(0.1)
        self.close(reason=None)

    #def closed(self, code, reason):
        #print(("Closed down", code, reason))

if __name__ == '__main__':
    try:
        ws = EchoClient('ws://10.1.9.109:9310', protocols=['http-only', 'chat'])
        ws.daemon = False
        ws.connect()
    except KeyboardInterrupt:
        ws.close()
