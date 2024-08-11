import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    
    text = input("Enter text: ")
    if text == 'exit':
        break
    
    client.sendto(text.encode(), ('127.0.0.1', 9999))
    print(client.recv(1024).decode())
    

