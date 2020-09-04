#this module can be access from clihndlr to recive data from client
# this function is just to recive clients data
import socket,select

def get_data(conn):
    try:
        conn.setblocking(0)
        data = ""
        while True:
            ready = select.select([conn], [], [], 0.01)
            if ready[0]:
                data += conn.recv(1000000)
            else:
                break
        conn.setblocking(1)
        return data
    except socket.error:
        return False
