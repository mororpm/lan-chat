import socket
import threading
from common.config import PORT, BUFFER_SIZE, ENCODING

HOST = "0.0.0.0"  # Listen on all interfaces


def handle_client(conn: socket.socket, addr):
    print(f"[+] Client connected: {addr}")
    try:
        while True:
            data = conn.recv(BUFFER_SIZE)
            if not data:
                break

            msg = data.decode(ENCODING, errors="replace")
            print(f"\nClient: {msg}")
            reply = input("You: ")

            conn.sendall(reply.encode(ENCODING))
    finally:
        conn.close()
        print(f"[-] Client disconnected: {addr}")


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, PORT))
        server.listen()

        print(f"[*] Server started on {HOST}:{PORT}")
        print("[*] Waiting for clients...")

        while True:
            conn, addr = server.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr), daemon=True)
            thread.start()


if __name__ == "__main__":
    main()
