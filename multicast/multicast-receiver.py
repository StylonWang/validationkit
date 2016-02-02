#!/usr/bin/python

MCAST_GRP = '239.1.1.1'
MCAST_PORT = 1234
TIME_OUT = 2

# set up receiver socket
rsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
rsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#rsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
rsock.setblocking(0)
rsock.bind( (MCAST_GRP, MCAST_PORT) )

mreq = struct.pack("4sl", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)
rsock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

start_time = time.time()

# receive response
while True:

    ready = select.select([rsock], [], [], 1);
    if not ready[0] :
        continue

    # receive messages
    msg = rsock.recvfrom(1024)

    # TODO: save multicast raw data as file
