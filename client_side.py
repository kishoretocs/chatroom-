import sys,socket,time

client_side = socket.socket()
client_host = socket.gethostname()
ip = socket.gethostbyname(client_host)
sport = 8080

print('this is your id address :',ip)
server_host = input("enter your's ip address :")
name = input("enter your friends name: ")

client_side.connect((server_host,sport))

client_side.send(name.encode())
client_name = client_side.recv(1024)
client_name = client_name.decode()

print(client_name,'has joined ')

while True:
    massage = (client_side.recv(1024)).decode()
    print(client_name, ":", massage)
    massage = input("me :")
    client_side.send(massage.encode())
