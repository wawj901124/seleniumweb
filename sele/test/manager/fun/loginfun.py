# _*_ coding:utf-8 _*_

__author__ = 'bobby'
__date__ = '2018/9/3 11:05'
from base.activebase import ActiveWeb

class LoginManager:

    def __init__(self):
        self.activeweb = ActiveWeb()  # 实例化
        self.loginurl = "https://bjw.halodigit.com:9090/nereus/manager/index#/login"
        self.loginaccountxpath = "/html/body/div[1]/div[2]/form/div/div[1]/input"
        self.loginaccount = "admin@iapppay.com"
        self.loginppasswordxpath = "/html/body/div[1]/div[2]/form/div/div[2]/input"
        self.loginpassword = "123456"
        self.loginbuttonxpath = "/html/body/div[1]/div[2]/form/div/a[1]/span"
        self.cookie = self.getcookie()

    def getcookie(self):
        # 登录
        self.activeweb.getUrl(self.loginurl)  # 打开网址
        self.activeweb.findElementByXpathAndInput(self.loginaccountxpath,self.loginaccount)
        self.activeweb.findElementByXpathAndInput(self.loginppasswordxpath,self.loginpassword)
        self.activeweb.findElementByXpathAndClick(self.loginbuttonxpath)
        self.activeweb.delayTime(3)
        # 获取cookie
        cookie = self.activeweb.getCookies()
        self.activeweb.closeBrowse()
        return cookie

    def writercookie(self,url):
        self.activeweb.writerCookies(self.cookie, self.loginurl,url)
