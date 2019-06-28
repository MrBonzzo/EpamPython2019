#!/usr/bin/env python3


import select
import socket


def send_to_all(message, client_socket=None):
    for dest_socket in clients:
        if dest_socket != main_socket and dest_socket != client_socket:
            try:
                dest_socket.send(message)
            except ConnectionError:
                continue


if __name__ == "__main__":
    host, port = '', 9999
    clients = {}
    main_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    main_socket.bind((host, port))
    main_socket.listen(10)
    clients[main_socket] = f"('{host}', {port})"

    print(f'TCP chat server started on {port} port')
    try:
        while True:
            read_sockets, _, _ = select.select(clients, [], [])
            for sock in read_sockets:
                if sock == main_socket:
                    client_socket, client_addr = main_socket.accept()
                    print(f'{client_addr} connected')
                    clients[client_socket] = f'{client_addr}'
                else:
                    try:
                        data = sock.recv(2048)
                    except OSError:
                        continue
                    if not data:
                        print(f'{clients[sock]} disconnected')
                        sock.close()
                        del clients[sock]
                    else:
                        client_addr = f'{clients[sock]}: '.encode('utf-8')
                        data = client_addr + data
                        send_to_all(data, sock)
    except KeyboardInterrupt:
        pass
    finally:
        for sock in clients:
            sock.close()
        print('\nTCP chat server stoped')
