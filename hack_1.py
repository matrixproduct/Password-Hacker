# write your code here
import sys, socket

args = sys.argv
hostname = args[1]
port = int(args[2])
message = args[3]


soc = socket.socket()
soc.connect((hostname, port))
soc.send(message.encode())
resp = soc.recv(1024).decode()
print(resp)
soc.close()