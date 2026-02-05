import socket
from common.config import PORT, BUFFER_SIZE, ENCODING

SERVER_IP = "192.168.1.198"  # <-- set Windows server LAN IP here


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((SERVER_IP, PORT))
        print(f"[*] Connected to {SERVER_IP}:{PORT}")

        while True:
            msg = input("You: ")
            if msg.lower() in {"exit", "quit"}:
                break

            client.sendall(msg.encode(ENCODING))

            data = client.recv(BUFFER_SIZE)
            if not data:
                print("[!] Server disconnected.")
                break
            print("Server:", data.decode(ENCODING, errors="replace"))


if __name__ == "__main__":
    main()
