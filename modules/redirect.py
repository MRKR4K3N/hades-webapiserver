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
        self.return_data["data"]  = "<script>window.location.href = '/index'</script>"
        return self.stt_code,self.return_data
        pass
