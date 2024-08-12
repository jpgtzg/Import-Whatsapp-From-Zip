import socket
""" 
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('0.0.0.0', 9999))

while True:
    data, addr = sock.recvfrom(1024)

    result = data.decode()

    print('received: {}'.format(result))

    if result == 'exit':
        break
    if result == 'data sent':
        # Now print your data
        

        sock.sendto(input("Enter text: ").encode(), addr)
    if result == 'data failed':
        print('Data failed')
        break
 """
class Server: 

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((self.host, self.port))

    def receive(self):
        data, addr = self.sock.recvfrom(1024)
        print('received: {}'.format(data.decode())) # TODO REMOVE
        return data.decode(), addr
        
    def send(self, data, addr):
        self.sock.sendto(data.encode(), addr)

    def close(self):
        self.sock.close()

server = Server('0.0.0.0', 9999)

while True:
    data, addr = server.receive()
    if data == 'exit':
        break
    
    server.send(input("Enter text: "), addr)