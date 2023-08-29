import socket

def start_server(port=8080):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', port))
    server_socket.listen(1)

    print(f"Server is running on port {port}...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Client connected from {addr}")
        
        request = client_socket.recv(1024).decode('utf-8')
        print(f"Received request:\n{request}")

        response = "HTTP/1.1 200 OK\nContent-Type: text/plain\n\nHello, World!"
        
        client_socket.sendall(response.encode('utf-8'))
        client_socket.close()

start_server()
