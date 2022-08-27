import sys,socket,time
root = socket.socket()
host_name = socket.gethostname()
id_addres = socket.gethostbyname(host_name)
port = 1234
root.bind((host_name,port))
print('bind is complied')
print('your id address is ', id_addres)
name = input('enter name: ')
root.listen(1)
com , add = root.accept()#com is connet to the socket and add is assignted to the id address
print('connect resversed from :' ,add[0])
client = (com.recv(1024)).decode()
print(client +'has connected')
com.send(name.encode())
 
while True:
    msg = input('me:')
    com.send(msg.encode())
    msg = com.recv(1024)
    msg = msg.decode()
    print(client, ":", msg)