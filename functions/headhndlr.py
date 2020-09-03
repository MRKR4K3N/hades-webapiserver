# this is for client header parsing
import urllib

def Get_header(data):
    head_data = {"headers":{},
                 "req":"",
                 "dest":"",
                 "post_data":{}}
    if "GET /" in data or "POST /" in data and "HTTP/1.1" in data or "HTTP/1.0" in data:
        headers = {}
        req = ""
        dest = ""
        count = 0
        data0 = data.split("\r\n\r\n")[0].split("\r\n")
        header_dest = data[0].split(" ")
        b = data0[0].split(" ")
        if len(b) == 3:
            req = b[0]
            dest = b[1]

        for i in data0:
            if count != 0:
                a = i.split(": ")
                if len(a) == 2:
                    headers[a[0]] = a[1]
            count += 1
        if "POST /" in data:
            data0 = data.split("\r\n\r\n")[1].split("&")
            for i in data0:
                if i != "":
                    b = i.split("=")
                    key = urllib.unquote(b[0])
                    key = key.replace(" ","")
                    if len(b) == 2 and key != "":
                        head_data["post_data"][key] = urllib.unquote(b[1])
        head_data["headers"] = headers
        head_data["req"] = req
        head_data["dest"] = dest
        return head_data
        #return headers,req,dest

# this is parameter functions, their job is to check if there is parameter and parse it. access from clihndlr
def check_params(data):
    if len(data.split("?")) == 2 and data.split("?") != "" :
        return True
    else:
        return False

def get_params(data):
    a = data.split("?")[1].split("&")
    params = {}
    for i in a:
        b = i.split("=")
        key = urllib.unquote(b[0])
        key = key.replace(" ","")
        if len(b) == 2 and key != "":
            params[key] = urllib.unquote(b[1])
    return params
