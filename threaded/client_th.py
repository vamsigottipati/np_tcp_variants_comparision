import socket

s = socket.socket()
host = "0.0.0.0"
port = 8080

s.connect((host, port))

with open('test.txt', 'rb') as f:
    print('file opened')
    while True:
        print('sending data...')
        data = f.read(1024)
        s.send(data)
        if not data:
            break

f.close()
print('Successfully sent the file')
s.close()
print('connection closed')
