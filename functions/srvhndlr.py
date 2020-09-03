# class for creating server
import socket

class create_server:
    def __init__(self,ip,port):
        self.ip = ip
        try:
            self.port = int(port)
            self.can_run = True
        except:
            self.can_run = False

    def start(self):
        if self.can_run:
            try:
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.bind((self.ip,self.port))
                s.listen(5)
                return s
            except socket.error:
                return False
