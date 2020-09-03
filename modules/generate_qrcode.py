import qrcode,random,string,urllib,base64,time,os
from thread import *
data = """<html>
<body>

<p>Location "%s" Not found</p>

</body>
</html>
"""
def delete_img(path):
    time.sleep(20)
    os.remove(path)

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def generate_qrcode(data,path):
    try:
        qr = qrcode.QRCode(version=2,box_size=4,border=5)
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill='black',back_color='white')
        fname = get_random_string(5)+"-"+urllib.quote(data)
        fname = fname.encode("hex")+".jpeg"
        save_path = path+'images\\'+fname
        img.save(save_path)
        start_new_thread(delete_img,(save_path,))
        return fname
    except:
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
        self.return_data = {}
        pass

    def execute(self):
        global data
        if len(self.params) != 1:
            self.return_data["data"] = '<html>require /generate_qrcode?data=<your data here> </html>'
            return self.stt_code,self.return_data
        elif "data" in self.params and self.params["data"] != "":
            fname = generate_qrcode(self.params["data"],self.configs["web_root"])
            if fname:
                self.return_data["data"]  = '<html> <p>this qr image will be delete after 20 sec</p> <img src="/?l=images/%s" alt="%s"> </html>'%(fname,self.params["data"])
                return self.stt_code,self.return_data
            else:
                self.return_data["data"]  = '<html><p>error on generating the qrcode..</p></html>'
                return self.stt_code,self.return_data
        else:
            self.return_data["data"]  = '<html>require /generate_qrcode?data=<your data here> </html>'
            return self.stt_code,self.return_data
