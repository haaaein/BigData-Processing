from socket import *

BUFSIZE = 1024

s = socket(AF_INET, SOCK_STREAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

s.bind(("", 8082))
s.listen(5)
conn, addr = s.accept()
data = "tmp"

while data != "exit":
	data = conn.recv(BUFSIZE).decode("UTF-8")
	print(addr, ":", data)
	conn.send(data.encode("UTF-8"))

conn.close()
