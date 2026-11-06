import socket
import sys
from des import ecb_encrypt

HOST = "127.0.0.1"
PORT = 5000
KEY = b"DEEBKEY1"

message = "TRANSFER EGP 1000 FROM ACC 1234 TO ACC 5678"
if len(sys.argv) > 1:
    message = sys.argv[1]

ciphertext = ecb_encrypt(message.encode(), KEY)

print("Message:", message)
print("Ciphertext:", ciphertext.hex().upper())
for i in range(0, len(ciphertext), 8):
    print("Block", i // 8 + 1, ":", ciphertext[i:i + 8].hex().upper())

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
client.send(ciphertext)

print("Server:", client.recv(1024).decode())
client.close()
