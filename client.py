import socket

sock = socket.socket()

sock.connect(('localhost', 8001))

while True:
    response = sock.recv(1024)
    print(response.decode())

    input_message = input('Enter message: ')
    if input_message == 'exit':
        break
    sock.send(input_message.encode())

sock.close()