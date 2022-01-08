import socket

s = socket.socket()

host = input(str("Please enter the host address of the sender: "))
port = 8080

s.connect((host, port))
print(f"[+] CONNECTED TO {host}:{port}")

filename = input(str("Please enter filename for the incoming file: "))
file = open(filename, 'wb')

file_data = s.recv(1024)
file.write(file_data)
file.close()

print(f"[+] FILE SAVED SUCCESSFULLY {filename}")
