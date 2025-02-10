import socket
import threading

HOST = '127.0.0.1'
PORT = 12345
clients = {}

def broadcast(message, sender_socket=None):
    """Send a message to all connected clients."""
    for client in clients.keys():
        if client != sender_socket:
            client.send(message.encode())

def handle_client(client_socket):
    """Handle communication with a single client."""
    try:
        username = client_socket.recv(1024).decode().strip()
        clients[client_socket] = username
        broadcast(f"{username} joined the chat!")

        while message := client_socket.recv(1024).decode():
            broadcast(f"{username}: {message}", client_socket)
    except ConnectionResetError:
        pass
    finally:
        broadcast(f"{clients[client_socket]} left the chat.")
        del clients[client_socket]
        client_socket.close()

def start_server():
    """Start the server and accept connections."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print(f"Server running on {HOST}:{PORT}")

        while True:
            client_socket, _ = server_socket.accept()
            threading.Thread(target=handle_client, args=(client_socket,)).start()

if __name__ == "__main__":
    start_server()

