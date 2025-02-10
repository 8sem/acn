import socket
import threading

HOST = '127.0.0.1'
PORT = 12345

def receive_messages(client_socket):
    """Receive and print messages from the server."""
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message:
                print(message)
        except:
            break

def start_client():
    """Start the client and connect to the server."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        username = input("Enter your username: ")
        client_socket.send(username.encode())

        threading.Thread(target=receive_messages, args=(client_socket,)).start()

        while message := input():
            if message.lower() == 'exit':
                break
            client_socket.send(message.encode())

if __name__ == "__main__":
    start_client()

