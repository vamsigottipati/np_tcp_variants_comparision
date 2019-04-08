import socket
import time
from _thread import *

port = 8080
s = socket.socket()
host = "0.0.0.0"
s.bind((host, port))
s.listen(2)

print('Server listening....')


def clientThread(conn, addr):
    while True:
        addr_str = addr[0].replace('.', '')
        filename = 'incomming' + addr_str +'.txt'
        f = open(filename, 'wb')
        l = conn.recv(1024)
        clock_start = time.clock()
        time_start = time.time()
        while (l):
            f.write(l)
            l = conn.recv(1024)
        clock_end = time.clock()
        time_end = time.time()
        duration_clock = clock_end - clock_start
        print('clock:  start = ', clock_start, ' end = ', clock_end)
        print('clock:  duration_clock = ', duration_clock)

        duration_time = time_end - time_start
        print('time:  start = ', time_start, ' end = ', time_end)
        print('time:  duration_time = ', duration_time)
        f.close()

        print('Done receiving')
        final_message = 'Thank you for connecting'
        conn.send(final_message.encode())
        if not l:
            break
        okMsg = 'okay'
        conn.sendall(okMsg.encode())
    conn.close()

while True:
    conn, addr = s.accept()
    print(addr[0])
    conn_msg = 'Got connection from'
    print(conn_msg.encode(), addr)
    start_new_thread(clientThread, (conn, addr))

s.close()
