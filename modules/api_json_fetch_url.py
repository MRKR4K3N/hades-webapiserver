import subprocess,imp, threading, requests, json
from thread import start_new_thread

def gen_random(plugin_path,length):
    mods = imp.load_source('module.name', plugin_path+"gen_random_string.py")
    return mods.gen(length)

def check_url(whitelist,url):
    for i in whitelist:
        if i == url:
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
        self.return_data = {"data":"<html></html>"}
        self.whitelist = ["https://www.w3schools.com"]
        pass

    def execute(self):
        if self.req == "GET" and "url" in self.params and "path" in self.params:
            url = self.params["url"]
            path = self.params["path"]
            if check_url(self.whitelist,url): #check the url for whitelist
                try:
                    data = requests.get(url+path)
                    try:
                        json.loads(data.text[3:]) #[3:] remove the weird characters
                        self.return_data["data"] = data.text[3:].encode("utf-8")
                    except ValueError:
                        self.return_data["data"] = "{}"
                except:
                    self.return_data["data"] = "{}"
            else:
                self.return_data["data"] = "{}"
        return self.stt_code,self.return_data
        pass
