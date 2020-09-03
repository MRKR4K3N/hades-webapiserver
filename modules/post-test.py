import subprocess,imp, threading
from thread import start_new_thread

def gen_random(plugin_path,length):
    mods = imp.load_source('module.name', plugin_path+"gen_random_string.py")
    return mods.gen(length)


class start:
    def __init__(self,headers,ip,params,req,post_data,configs,cookies_handler):
        self.headers = headers
        self.req = req
        self.ip = ip
        self.params = params
        self.post_data = post_data
        self.configs = configs
        self.cookies_handler = cookies_handler
        self.stt_code = 200
        self.return_data = {"data":"<html></html>"}
        pass

    def execute(self):
        print self.post_data,self.params
        if len(self.post_data) != 0 and self.req == "POST":
            if "username" in self.post_data and "password" in self.post_data:
                if self.post_data["username"] == "admin" and self.post_data["password"] == "admin":
                    self.return_data["data"] = "Access Granted!"
                    id = gen_random(self.configs["plugins_path"],20)
                    self.return_data["add_head"] = {"Set-Cookie":id}
                    if self.cookies_handler.add_cookies(self.ip,id):
                        t = threading.Thread(target=self.cookies_handler.cookies_timer,args=(id,))
                        t.start()

                else:
                    self.return_data["data"] = "Access Denined"
            else:
                self.return_data["data"] = "Unknown data post"
        elif len(self.params) != 0:
            if "c" in self.params:
                if self.params["c"] == "get_cookies":
                    print self.cookies_handler.get_cookies()
                elif self.params["c"] == "check_cookies":
                    print self.cookies_handler.check_cookies_by_id(self.headers["Cookie"])
                elif self.params["c"] == "delete_cookies":
                    print self.cookies_handler.delete_cookies(self.headers["Cookie"])
            elif "username" in self.params:
                if self.params["username"] == "admin":
                    self.return_data["data"] = "Access Granted!"
                    id = gen_random(self.configs["plugins_path"],20)
                    self.return_data["add_head"] = {"Set-Cookie":id}
                    if self.cookies_handler.add_cookies(self.ip,id):
                        t = threading.Thread(target=self.cookies_handler.cookies_timer,args=(id,))
                        t.start()

        else:
            self.return_data["data"] = "hello this is post requests test"
        return self.stt_code,self.return_data
        pass
