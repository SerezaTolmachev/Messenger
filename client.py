import socket
import threading

ip_address = str(input('Ведите IP-адрес.'))
port = int(input('Ведите порт.'))
password = str(input('Ведите пароль.'))
#ip_address = 'localhost'
#port = 50
#password = '1234567890'
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((ip_address, port))
client_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
client_socket.send(bytes(password.encode()))
dat = client_socket.recv(1024).decode()
if dat == 'Вам выдан доступ.':
    print('Вы успешно подключились!')

elif dat =='Доступ не разрешён.':
    exit()

def send_message():

    while True:
        msg = input()
        client_socket.send(bytes(msg.encode()))

def recv_message():
    while True:
        try:
            dat = client_socket.recv(1024).decode()
            print(dat)

        except:
            pass


threading.Thread(target=recv_message).start()
threading.Thread(target=send_message).start()















