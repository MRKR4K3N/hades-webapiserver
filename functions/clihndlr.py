# this class only can access from listhndlr to handle the clients
# responsible to handle the clients requests and the function modules

import socket,drecvhndlr,headhndlr,imp,sndtchndlr

class client_handler:
    def __init__(self,ip,conn,configs,cookies_handler):
        self.ip = ip
        self.conn = conn
        self.configs = configs
        self.params = {}
        self.post_data = {}
        self.return_data = {"data":"","add_head":{}}
        self.cookies_handler = cookies_handler

    def client_room(self):
        #print "[+] incoming connection from: "+self.ip
        data = drecvhndlr.get_data(self.conn)
        try:
            if data:
                head_data = headhndlr.Get_header(data)
                #headers,req,dest = headhndlr.Get_header(data) #header parser
                headers = head_data["headers"]
                req = head_data["req"]
                dest = head_data["dest"]
                if len(head_data["post_data"]) != 0:
                    self.post_data = head_data["post_data"]

                if "?" in dest:
                    if headhndlr.check_params(dest):
                        self.params = headhndlr.get_params(dest) #get the parameter from destination
                        dest = dest.split("?")[0] #split the parameter from destination, and get only destination
                    else:
                        dest = dest.split("?")[0]
                if dest == "/":
                    dest = "index"

                dest = dest.replace("/","").replace("..","")
                try:
                    mods = imp.load_source('module.name', self.configs["web_modules"]+dest+'.py')
                    start_= mods.start(headers,self.ip,self.params,req,self.post_data,self.configs,self.cookies_handler)
                    status_code , self.return_data = start_.execute()
                except IOError:
                    status_code = 404
                    self.return_data["data"] = "File Not Found"%(dest)
                    pass
                stc = sndtchndlr.send_to_client(status_code,self.return_data,self.conn)
                stc.start()
                if "User-Agent" in headers:
                    print "%s [] %s %s [stt_code: %s ] - %s"%(self.ip, req, dest, status_code, headers["User-Agent"])
                else:
                    print "%s [] %s %s [stt_code: %s ] -"%(self.ip, req, dest, status_code)
            else:
                self.conn.close()
        except Exception, e:
            status_code = 404
            self.return_data["data"] = "File Not Found"%(dest)
            stc = sndtchndlr.send_to_client(status_code,self.return_data,self.conn)
            stc.start()
            print e
            self.conn.close()
        self.conn.close()
