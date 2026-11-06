import socket
from des import ecb_decrypt

HOST = "127.0.0.1"
PORT = 5000
KEY = b"DEEBKEY1"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen(1)
print("Server listening on port", PORT)

while True:
    conn, addr = server.accept()
    print("\nConnected:", addr)

    data = conn.recv(4096)
    print("Received:", data.hex().upper())
    for i in range(0, len(data), 8):
        print("Block", i // 8 + 1, ":", data[i:i + 8].hex().upper())

    try:
        message = ecb_decrypt(data, KEY).decode()
        print("Decrypted:", message)
        conn.send(b"Transaction received")
    except Exception:
        print("Decryption failed")
        conn.send(b"Error")

    conn.close()
