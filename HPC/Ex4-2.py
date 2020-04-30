import random
import socket

def barrier():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 6999))
    while True:
        data = client.recv(1024)
        if data == b'GOON':
            break
    client.send('quit'.encode())
    client.close()

def MaxMin():
    a = []
    for i in range(10):
        a.append(random.random() * 10)
    barrier()
    print(max(a), min(a))

if __name__ == "__main__":
    MaxMin()
