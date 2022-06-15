import socket

client = socket.socket()
client.bind(('127.0.0.1',8888))

res = client.recv(2048).decode()
print(res)

res = client.recv(2048).decode()
inp = input(res)
client.send(inp.encode())

res = client.recv(2048).decode()
print (res)

while True:
    msg = client.recv(2048).decode()
    if msg == 'ok':
        break
    inp = input(msg)
    client.send(inp.encode())
res = client.recv(2048).decode()
print(res)


client.close()
