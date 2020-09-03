import subprocess,imp, threading, requests, json
from thread import start_new_thread

def gen_random(plugin_path,length):
    mods = imp.load_source('module.name', plugin_path+"gen_random_string.py")
    return mods.gen(length)

def check_url(whitelist,url):
    for i in whitelist:
        if i in url:
            return True
    return False


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
        self.return_data = {"data":"{}"}
        pass

    def execute(self):
        if self.req == "GET" and "c" in self.params:
            if self.params["c"] == "fetch_users":
                #authorized user only function
                if "Cookie" in self.headers and self.cookies_handler.check_cookies_by_id(self.headers["Cookie"]) and  self.cookies_handler.check_cookies_by_id(self.headers["Cookie"]) != "expired":
                    self.return_data["data"] = '{"username":"admin","password":"admin"}'
                else:
                    self.return_data["data"] = '{"error":"authorized user only"}'
                    return 403,self.return_data
            elif self.params["c"] == "fetch_info":
                self.return_data["data"] = '{"info":"this is just info for any Unauthorized or authorized users"}'


        return self.stt_code,self.return_data
        pass
