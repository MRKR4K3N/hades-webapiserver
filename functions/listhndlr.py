# this class is to listen and accept the incoming connection

import socket,clihndlr,ckieshndlr,imp
from thread import start_new_thread

class start_listening:
    """docstring for ."""

    def __init__(self, sock, configs):
        self.sock = sock
        self.configs = configs
        self.cookies_handler = ckieshndlr.cookies_handler()

    def listen(self):
        while True:
            conn,addr = self.sock.accept()
            ip = str(addr[0])+":"+str(addr[1])
            mods = imp.load_source('module.name', self.configs["functions_paths"]+'clihndlr'+'.py')
            start_= mods.client_handler(ip,conn,self.configs,self.cookies_handler)
            start_new_thread(start_.client_room,())
