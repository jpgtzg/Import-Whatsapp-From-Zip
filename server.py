import socket

sock = socket.socket()
sock.bind( ('localhost', 8001))

sock.listen(10)

while True:
    conn, addr = sock.accept()
    print('connected: ', addr)

    conn.send(input('Enter message: ').encode())
    
    response = conn.recv(1024)
    print(response.decode())
    conn.close()