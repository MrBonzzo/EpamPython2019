#!/usr/bin/env python3


import select
import socket
import sys


if __name__ == "__main__":
    host, port = '127.0.0.1', 9999
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server_socket.connect((host, port))
    except ConnectionError:
        print('\nUnable to connect')
        sys.exit()
    print('\nConnected to TCP chat server')
    try:
        while True:
            socket_list = [sys.stdin, server_socket]
            read_sockets, _, _ = select.select(socket_list, [], [])
            for sock in read_sockets:
                if sock == server_socket:
                    data = sock.recv(2048).decode('utf-8').rstrip()
                    if not data:
                        server_socket.close()
                        print('\nDisconnected from chat server')
                        sys.exit()
                    else:
                        print(data)
                else:
                    msg = sys.stdin.readline()
                    server_socket.send(bytes(msg, 'utf-8'))
    except KeyboardInterrupt:
        pass
    finally:
        server_socket.close()
        print('\nClient stoped')
