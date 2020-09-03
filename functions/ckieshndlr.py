# responsible for store,add,fetch,delete and verify the client cookies
# the client will store the cookies for a while in the memory for 5 mins
import time
from thread import start_new_thread

class cookies_handler(object):
    def __init__(self,):
        self.cookies = {} #{cookie:{"cookies_ip":<ip>,"cookies_time":<time>}}
        self.cookies_status = {} #{cookies:{"cookies_status":<active/expired>}}
        self.cookies_timeout =  300 #300 #5min in sec

    def cookies_timer(self,cookie):
        while True:
            if cookie in self.cookies:
                if (time.time()-self.cookies[cookie]["cookies_time"]) >= self.cookies_timeout:
                    del self.cookies[cookie]
                    self.cookies_status[cookie]["cookies_status"] = "expired"
                    break
            else:
                break
            time.sleep(2)

    def add_cookies(self,ip,cookie):
        self.cookies[cookie] = {}
        self.cookies[cookie]["cookies_ip"] = ip
        self.cookies[cookie]["cookies_time"] = time.time()
        self.cookies_status[cookie] = {}
        self.cookies_status[cookie]["cookies_status"] = "active"
        #start_new_thread(cookies_timer,(cookie,))
        return True

    def update_cookies(self,cookie):
        self.cookies[cookie]["cookies_time"] = time.time()
        return True

    def delete_cookies(self,cookie):
        if cookie in self.cookies:
            del self.cookies[cookie]

        if cookie in self.cookies_status:
            del self.cookies_status[cookie]
            return True
        else:
            return False

    def get_cookies(self):
        return self.cookies

    def check_cookies_by_id(self,cookie):
        if cookie in self.cookies_status:
            return self.cookies_status[cookie]["cookies_status"]
        else:
            return False
