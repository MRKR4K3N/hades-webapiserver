# this is script is responsible for creating a server header and send data to clients
#

import socket,magic
#HTTP/1.1 200 OK
headers_code = {200:"OK",
           404:"Not Found",
           401:"Unauthorized",
           403:"Forbidden"}

def build_header(status_code,Length,type,add_head = {}):
    header = {
              "Server":"hades-WebApiServer/1.0",
              "Content-Type":type,
              "Content-Length":Length,
              "Access-Control-Allow-Origin": "*"
              }
    if len(add_head) != 0:
        for i in add_head:
            header[i] = add_head[i]
        pass

    headers = ["HTTP/1.1 %s %s"%(status_code,headers_code[status_code])]
    for i in header:
        headers.append("%s: %s"%(i,header[i]))
    return "\r\n".join(headers)

class send_to_client:
    def __init__(self, status_code,data,conn):
        self.status_code = status_code
        self.data = data
        self.conn = conn

    def start(self):
        if "add_head" in self.data:
            head = build_header(self.status_code,str(len(self.data["data"])),magic.from_buffer(self.data["data"],mime=True),add_head = self.data["add_head"])
        else:
            head = build_header(self.status_code,str(len(self.data["data"])),magic.from_buffer(self.data["data"],mime=True),add_head = {})
        compile = head +"\r\n\r\n"+ self.data["data"]
        self.conn.send(compile)
        pass
