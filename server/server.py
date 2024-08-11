import socket

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
