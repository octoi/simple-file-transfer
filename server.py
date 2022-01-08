import socket

s = socket.socket()
host = socket.gethostname()
port = 8080

s.bind((host, port))
s.listen()

print(f"[+] SERVER STARTED {host}:{port}")

conn, addr = s.accept()
print(f"[+] {addr} CONNECTED")

filename = input(str("Please enter the filename of the file: "))
file = open(filename, 'rb')
file_data = file.read(1024)

conn.send(file_data)

print("[+] DATA TRANMITTED SUCCESSFULLY")
