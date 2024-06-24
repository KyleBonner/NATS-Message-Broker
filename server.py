import socket

def handle_connection(client_socket):
    data = client_socket.recv(1024).decode()
    if "subject" in data:
        client_socket.send(b"True")
    client_socket.close()

def start_server():
    host = "localhost"
    port = 57839

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, address = server_socket.accept()
        print(f"New connection from {address[0]}:{address[1]}")
        handle_connection(client_socket)

start_server()