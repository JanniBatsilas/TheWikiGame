import socket
import os
from _thread import *


client_list = []


def start_server():

    ServerSocket = socket.socket()
    host = '127.0.0.1'
    port = 1233
    ThreadCount = 0

    try:
        ServerSocket.bind((host, port))
    except socket.error as e:
        print(str(e))

    print('Waitiing for a Connection..')
    ServerSocket.listen(5)

    def threaded_client(connection):
        connection.send(str.encode('Welcome to the Servern'))
        while True:
            data = connection.recv(2048)
            reply = 'Server Says: ' + data.decode('utf-8')
            if not data:
                break
            connection.sendall(str.encode(reply))
        connection.close()

    while True:
        Client, address = ServerSocket.accept()
        client_list.append()
        print('Connected to: ' + address[0] + ':' + str(address[1]))
        start_new_thread(threaded_client, (Client,))
        ThreadCount += 1
        print('Thread Number: ' + str(ThreadCount))

    ServerSocket.close()


class Server:

    def __init__(self):
        start_server()


