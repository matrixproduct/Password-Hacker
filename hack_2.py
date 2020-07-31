# write your code here
import sys, socket, string, itertools

args = sys.argv
# args = [' ', '127.0.0.1', '9090']
hostname = args[1]
port = int(args[2])


soc = socket.socket()
soc.connect((hostname, port))


letters = string.ascii_lowercase
digits = "0123456789"
all_symbols = letters + digits

resp = ""
i = 0

while resp != "Connection success!":
    i += 1
    for comb in itertools.product(all_symbols, repeat=i):
        pwd = "".join(comb)
        soc.send(pwd.encode())
        resp = soc.recv(1024).decode()
        if resp == "Connection success!":
            break

soc.close()
print(pwd)