import socket  # noqa: F401


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    with socket.create_server(("localhost", 6379), reuse_port=True) as server_socket:
        conn, addr = server_socket.accept()
        with conn:
            while True:
                print(f"Connected to {addr}")
                _ = conn.recv(1024).decode()
                conn.sendall(b"+PONG\r\n")
                


if __name__ == "__main__":
    main()
