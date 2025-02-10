import socket

def udp_server():
    host = '127.0.0.1'  
    port = 65433  

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
        server_socket.bind((host, port))
        print(f"UDP Server is listening on {host}:{port}")

        while True:
            data, addr = server_socket.recvfrom(1024)
            print(f"Received from {addr}: {data.decode()}")
            server_socket.sendto(data, addr)  # Echo back the data

if __name__ == "__main__":
    udp_server()

