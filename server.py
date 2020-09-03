import socket,functions,sys,time
from thread import *

sock = ""
# -test-
# TODO
# create a server that support ssl to secure the conneection between the server and clients

if len(sys.argv) != 2:
    print """
    %s <config file>"""%(sys.argv[0])
    exit()

conf = sys.argv[1]
configs = {}
def read_config():
    f = open(conf,"r")
    for i in f:
        line = i.strip("\r\n").strip("\n")
        if '#' in line or line == "":
            pass
        else:
            c = line.split(" = ")
            configs[c[0]] = c[1]
    pass

def main():
    global sock
    read_config()
    print configs
    cs = functions.srvhndlr.create_server(configs["server_ip"],int(configs["server_port"]))
    sock = cs.start()
    if sock:
        print "[+] Server is up!"
        lstn = functions.listhndlr.start_listening(sock,configs)
        start_new_thread(lstn.listen,())
        print "[+] Server is listening for connection"
    else:
        print "[!] can't the start server"

main()
try:
    while True:
        time.sleep(10)
        pass
except KeyboardInterrupt:
    sock.close()
