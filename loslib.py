#Requirements
import requests
import sys
import time
import urllib.parse
from bs4 import BeautifulSoup
import inspect
import time
import binascii
#-------------


def _vname_(**kwargs):
    bound_args = inspect.signature(_vname_).bind(**kwargs)
    bound_args.apply_defaults()
    return dict(bound_args.arguments)["kwargs"]


class c:                    #for print colored text
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m' 
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class los():
    def __init__(self, id=False,pw=False):
        self.phead("""
                                                
            __    _____ _____    __    _ _     
            |  |  |     |   __|  |  |  |_| |_   
            |  |__|  |  |__   |  |  |__| | . |_ 
            |_____|_____|_____|  |_____|_|___|_|
                                                
        """)
        #~~~~~~~~USER INFO~~~~~~
        self.uid = id
        self.upw = pw
        self.nlevel = ""        #problem
        self.probs = dict()
        #~~~~~~~~~~~~~~~~~~~~~~~

        #~~~~~~~~~~URLs~~~~~~~~~~~
        self.url_login = "https://los.rubiya.kr?login"
        self.url_prob = "https://los.rubiya.kr/static/json.js"
        self.url_base = "https://los.rubiya.kr"
        self.url_prob = ""
        #~~~~~~~~~~~~~~~~~~~~~~~~~

        #~~~~~~~~for REEQUEST~~~~~~~~~~~~
        self.__session = requests.Session()           #init session()
        self.__response = ""
        self.__soup = ""
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        #~~~~~~~~~~~~~~OPTIONS~~~~~~~~~~~
        self.out = True         #print logs

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        #~~~~~~~~~RESPONSES~~~~~~~~~
        self.ans = ""
        self.runtime = 0

        self.login()
        return

    #~~~~~~~~~~~GETTER & SETTER~~~~~~~~~
    @property           #self.__response
    def res(self):
        return self.__response
    @res.setter         #self.__response
    def res(self,value):
        if(isinstance(value,requests.models.Response)):
            self.__response = value
            self.html = BeautifulSoup(self.__response.text,"html.parser")
        return

    @property           #self.__session
    def http(self):
        return self.__session
    @http.setter        #self.__session
    def http(self):
        return

    @property          #self.__soup
    def html(self):
        return str(self.__soup)
    @html.setter       #self.__soup
    def html(self,value):
        if isinstance(value,BeautifulSoup):
            self.__soup = value
        return
    @property          #self.__soup
    def shtml(self):
        return self.__soup
    #~~~~~~~~~~~~END~~~~~~~~~~~~~~~~~~~~


    #~~~~~~~~~~SET USER~~~~~~~~~~~~~~~~
    def login(self):
        if(not(self.uid and self.upw)):
            self.perror("pls set userID & userPW")
            return
        self.res = self.http.post("https://los.rubiya.kr?login", 
        data={
            "id":self.uid,
            "pw":self.upw
        })
        if "php" in self.html:
            self.psuccess("id:({id}) login success!".format(id=self.uid))
            self.get_probs()
            self.pwarning("your level : "+self.nlevel)
            self.setProb(self.nlevel)
        else:
            self.perror("LOGIN FAIL")
        return
    
    def get_probs(self):
        self.res = self.http.get("https://los.rubiya.kr/static/json.js")
        tprobs = self.res.json()["data"]
        self.probs = dict()
        for prob in tprobs:
            self.probs[prob["descrip"]] = {"status":prob["status"]=="completed" and True or False , "link":self.url_base+prob["link"].lstrip(".")}
        self.set_next()
        return
    
    def set_next(self):
        for prob in self.probs:
            if not self.probs[prob]["status"]:
                self.nlevel = prob
                break
        return

    #~~~~~~~~~~~~~~PROBLEM~~~~~~~~~~~~~~~
    def setProb(self,prob_name):
        self.url_prob = self.probs[prob_name.lower()]["link"]
        return
    
    def send(self,*args, **kwargs):
        vnames = _vname_(**kwargs)
        params = "&".join("%s=%s" % (k,v) for k,v in vnames.items())
        try:
            self.res = self.http.get(self.url_prob, params=params)
            self.Parse()
            if self.out :
                self.pblue("sended data : "+self.res.url)
                self.psuccess("ANSWER ↓\n"+self.ans)
                print(self.shtml.text)
        except:
            self.result = False
            self.perror("SEND ERROR")
        return
    
    def Parse(self):
        if len(self.res.text) < 20:
            self.ans = self.res.text
            return
        aa = self.shtml.find_all("h2")
        for a in aa:
            self.ans += a.get_text()+"\n"
        return
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    #~~~~~~~~~Time service for blind SQLI~~~~~~~
    def start(self):
        self.time = time.time()
        return

    def end(self):
        self.runtime = time.time() - self.time
        self.runtime *= 1000 #to ms
        return self.runtime
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    #~~~~~~~~~~~print functions~~~~~~~~~~~~
    def phead(self,msg):
        return print(c.HEADER+msg+c.ENDC)

    def perror(self,msg):
        return print(c.FAIL+msg+c.ENDC)
    
    def psuccess(self,msg):
        return print(c.OKGREEN+msg+c.ENDC)
    
    def pwarning(self,msg):
        return print(c.WARNING+msg+c.ENDC)
    
    def pblue(self,msg):
        return print(c.OKBLUE+msg+c.ENDC)
 
    def load(self,msg):
        return print("\r"+msg)
    
    def log(self,msg):
        return print("[+] "+msg)

    #Encoder
    def hex(self,string):
        return "0x"+string.encode("utf-8").hex()

    def unhex(self,_hex_):
        return binascii.unhexlify(_hex_)

    def urlencode(self,string):
        return "".join(["%"+x.encode("utf-8").hex() for x in string])


