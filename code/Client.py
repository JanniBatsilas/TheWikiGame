from threading import Thread
import socket
from g_window import GameWindow


def start_client():

    ClientSocket = socket.socket()
    host = '127.0.0.1'
    port = 1233

    print('Waiting for connection')
    try:
        ClientSocket.connect((host, port))
    except socket.error as e:
        print(str(e))

    Response = ClientSocket.recv(1024)

    while True:
        Input = input('Say Something: ')
        ClientSocket.send(str.encode(Input))
        Response = ClientSocket.recv(1024)
        print(Response.decode('utf-8'))

    ClientSocket.close()


class Client:

    def __init__(self):
        game = GameWindow()
        start_client()



