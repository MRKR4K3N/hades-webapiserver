
data = """<html>
<body>

<p>file Not found</p>

</body>
</html>
"""

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
        global data
        if len(self.params) != 1:
            self.return_data["data"] = '<html><script>window.location.href="/?l=index.html"</script></html>'
            return self.stt_code,self.return_data
        else:
            self.params["l"] = self.params["l"].replace("../","") #solve the path traversal vuln
            location = self.configs["web_root"]+self.params["l"]
            #print location
            try:
                f = open(location,"rb")
                self.return_data["data"]  = f.read()
                f.close()
                return self.stt_code,self.return_data
            except:
                self.return_data["data"] = data%(self.params["l"])
                return self.stt_code,self.return_data
                pass
