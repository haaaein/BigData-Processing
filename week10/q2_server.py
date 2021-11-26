from socket import *
import time

def main():
	listen_sock = socket(AF_INET, SOCK_STREAM)
	listen_sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
	listen_sock.bind(('', 8082))
	listen_sock.listen(1)

	while 1:
		conn, addr = listen_sock.accept()
		data = conn.recv(1024)
		print(data.decode("UTF-8"))
		msg = "HTTP/1.1 200 OK\n\n<html><body>This time is {}</body></html>".format(time.ctime())
		conn.sendall(msg.encode("UTF-8"))
		conn.close()

if __name__ == "__main__":
	main()