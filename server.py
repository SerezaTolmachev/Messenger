import socket
import threading

pswrd = '1234567890'

players = []

main_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
main_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
main_socket.bind(('localhost', 50))
main_socket.setblocking(False)
main_socket.listen(10)

def listen(player):
    while True:
        try:
            data = player.recv(1024).decode()

            if data != None:
                send_all(data, player)
        except:
            pass


def send_all(data, author):
    for player in players:
        if player != author:
            try:
                player.send(data.encode())
            except:
                pass


while True:
    try:
        conn, addr = main_socket.accept()
        dt = conn.recv(1024).decode()
        if dt == pswrd:
            a = 'Вам выдан доступ.'
            players.append(conn)
            conn.setblocking(False)
            conn.send(bytes(a.encode()))
            threading.Thread(target=listen, args=(conn,)).start()

        else:
            b = 'Доступ не разрешён.'
            conn.send(bytes(b.encode()))



    except BlockingIOError:
        pass




