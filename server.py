import socket
import select
import string
import time
time_start=0
time_stop=0
clock_stop=0
duration_time=0
clock_start=0
count=0
def broadcast_data (sock, message):
    for socket in CONNECTION_LIST:
        if socket != server_socket and socket != sock:            
            socket.send(message)

if __name__ == "__main__":

    CONNECTION_LIST=[]
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    server_socket.bind(("0.0.0.0", 5000))
    server_socket.listen(2)
    CONNECTION_LIST.append(server_socket)
    print "TCP/IP Chat server process started."
    count = 0
    while 1:
        
        read_sockets,write_sockets,error_sockets = select.select(CONNECTION_LIST,[],[])

        for sock in read_sockets:

            if sock == server_socket:
                sockfd, addr = server_socket.accept()
                CONNECTION_LIST.append(sockfd)
                print "Client (%s, %s) connected" % addr
                broadcast_data(sockfd, "Client (%s, %s) connected" % addr)

            else:
                try:
                    data = sock.recv(1024)
                except:
                    broadcast_data(sock, "Client (%s, %s) is offline" % addr)
                    print "Client (%s, %s) is offline" % addr
                    sock.close()
                    CONNECTION_LIST.remove(sock)
                    continue

                if data:
                    if data == "q" or data == "Q":
                        broadcast_data(sock, "Client (%s, %s) quits" % addr)
                        print "Client (%s, %s) quits" % addr
                        sock.close()
                        CONNECTION_LIST.remove(sock)
                    else:
                        broadcast_data(sock, data)
			#print("sending...")
			#print("clock init")
			#if count == 0:
                        #	clock_start = time.clock()
		        #	time_start = time.time()
			#	print("clock started")
			 #       count = count + 1
	
		    
    		
		#clock_stop = time.clock()
		#time_stop = time.time()
		#print("clock stopped")
		#sock.close()
		#duration_time = time_stop - time_start
		#duration_clock = clock_stop - clock_start
		#print(duration_time) 
        #g=open('time.txt','wb')
	#g.write(str(duration_time))
	#g.close()
        #clock_start=0
	#time_start=0
	#clock_stop=0
	#time_stop=0  
    server_socket.close()	
