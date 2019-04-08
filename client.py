import socket
from _thread import *
import threading
import sys
import time

global sender_time_start
global recv_time_start

global sender_time_stop
global recv_time_stop

#global diff_sender
#global diff_recv



def recv_data():
    while 1:
        global_counter_recv = 0
        try:
            recv_data = client_socket.recv(1024)
            if global_counter_recv != 0:
                recv_time_stop = time.time()
                print(recv_time_stop - recv_time_start)
            if not recv_data:
                print("Server closed connection, thread exiting.")
                interrupt_main()
                break
            else:
                filename = 'out.txt'
                recv_time_start = time.time()
                f = open(filename, 'wb')
                while (recv_data):
                    f.write(recv_data)
                    recv_data = client_socket.recv(1024)
                    global_counter_recv = global_counter_recv + 1
        except:
            print("Server closed connection, thread exiting.")
            interrupt_main()
            break


def send_data():
    global_counter_send = 0
    while 1:
        print(global_counter_send)
        if global_counter_send != 0:
            sender_time_stop = time.time()
            print(sender_time_stop - sender_time_start)
        send_data = input("Enter file name to send (q or Q to quit):")
        if send_data == "q" or send_data == "Q":
            client_socket.send(send_data)
            interrupt_main()
            break
        else:
            with open('in.txt', 'rb') as f:
                sender_time_start = time.time()
                print("file opened")
                l = f.read(1024)
                while (l):
                    client_socket.send(l)
                    if global_counter_send == 0:
                        sender_time_start = time.time()
                    print("sent")
                    l = f.read(1024)
                    global_counter_send = global_counter_send + 1


if __name__ == "__main__":

    print("******   TCP/IP File Transfer program   *******")
    print("Connecting to server")

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("192.168.0.14", 5000))

    print("Connected to server")

    start_new_thread(recv_data, ())
    start_new_thread(send_data, ())

    try:
        while True:
            continue
    except:
        print("Client program quits....")
        client_socket.close()
