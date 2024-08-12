import socket

""" client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    
    text = input("Enter text: ")
    if text == 'exit':
        break
    
    client.sendto(text.encode(), ('127.0.0.1', 9999))
    print(client.recv(1024).decode())
     """
class Client :

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send(self, data):
        self.client.sendto(data.encode(), (self.host, self.port))

    def receive(self):
        data, addr = self.client.recvfrom(1024)
        print('received: {}'.format(data.decode()))
        return data.decode()

    def close(self):
        self.client.close()

client = Client('127.0.0.1', 9999)

while True: 
    text = input("Enter text: ")
    if text == 'exit':
        break

    client.send(text)
    print(client.receive())

