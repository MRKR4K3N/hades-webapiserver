#using imp for importing the plugin
import imp

def gen_random(plugin_path,length): #create function out of the class
    mods = imp.load_source('module.name', plugin_path+"gen_random_string.py") #add this line
    return mods.gen(length) # if add this if needed since we need the output then we add this

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
        self.return_data = {}
        pass

    def execute(self):
        #so this code is an example how to use the random_string generator
        #here we add the parameters the plugin path and the length of the random string
        #we going to add into return_data["data"] for the program send it to the client
        self.return_data["data"] = gen_random(self.configs["plugins_path"],20)
        return self.stt_code,self.return_data
        pass
