import socket

def tcp_client():
    host = '127.0.0.1'  
    port = 65432  

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        message = "Hello, TCP Server!"
        client_socket.sendall(message.encode())
        data = client_socket.recv(1024)
        print(f"Received from server: {data.decode()}")

if __name__ == "__main__":
    tcp_client()

