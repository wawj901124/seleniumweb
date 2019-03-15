from base.activebase import ActiveWeb
from util.operation_json import OperationJson


class GetCookie():
    def __init__(self,outjsonfile=None,outloginurl=None,outloginaccountxpath=None,
                 outloginaccounttext=None,outloginppasswordxpath=None,outloginpasswordtext=None,
                 outloginbuttonxpath=None):

        if outjsonfile==None:
            self.jsonfile = '../dataconfig/cookie.json'
        else:
            self.jsonfile = outjsonfile

        if outloginurl==None:
            self.loginurl ="https://bjw.halodigit.com:9090/nereus/manager/index#/login"
        else:
            self.loginurl = outloginurl

        if outloginaccountxpath==None:
            self.loginaccountxpath = "/html/body/div[1]/div[2]/form/div/div[1]/input"
        else:
            self.loginaccountxpath = outloginaccountxpath

        if outloginaccounttext==None:
            self.loginaccount = "xiangkaizheng@iapppay.com"
        else:
            self.loginaccount = outloginaccounttext

        if outloginppasswordxpath==None:
            self.loginppasswordxpath = "/html/body/div[1]/div[2]/form/div/div[2]/input"
        else:
            self.loginppasswordxpath = outloginppasswordxpath

        if outloginpasswordtext==None:
            self.loginpassword = "123456"
        else:
            self.loginpassword = outloginpasswordtext

        if outloginbuttonxpath==None:
            self.loginbuttonxpath = "/html/body/div[1]/div[2]/form/div/a[1]/span"
        else:
            self.loginbuttonxpath = outloginbuttonxpath

        self.operationjson = OperationJson(file_path=self.jsonfile)   #实例化
        self.activeweb = ActiveWeb()  # 实例化


    def getCookie(self):
        # 登录
        self.activeweb.getUrl(self.loginurl)  # 打开网址
        self.activeweb.findElementByXpathAndInput(self.loginaccountxpath,self.loginaccount)
        self.activeweb.findElementByXpathAndInput(self.loginppasswordxpath,self.loginpassword)
        self.activeweb.findElementByXpathAndClick(self.loginbuttonxpath)
        self.activeweb.delayTime(3)
        if 'merchant' in self.jsonfile :
            print("outjsonfile为：%s"% self.jsonfile)
            self.selectMerchant()
        else:
            print("开始获取cookie---")
        # 获取cookie
        cookie = self.activeweb.getCookies()
        self.activeweb.closeBrowse()
        return cookie

    def writerCookieToJson(self):
        self.cookie = self.getCookie()
        self.operationjson.write_data(self.cookie)
        print("\ncookie信息‘%s’已经写入‘%s’文件里。\n" % (self.cookie,self.jsonfile))

    #选商户时的操作
    def selectMerchant(self):
        self.merchantxpath = '/html/body/div[1]/div[2]/div/form/div[5]/p[1]/span/input'
        self.confirmbuttonxpath = '/html/body/div[1]/div[2]/div/form/div[43]/p/span[2]/button'

        self.activeweb.findElementByXpathAndScriptClick(self.merchantxpath)
        self.activeweb.findElementByXpathAndClick(self.confirmbuttonxpath)
        self.activeweb.delayTime(3)










