# _*_ coding:utf-8 _*_

__author__ = 'bobby'
__date__ = '2018/8/10 15:55'
from base.activebase import ActiveWeb   #导入ActiveWeb
from project.agent.loginpageagent import LoginPage   #导入LoginPage页

class LoginPageAgentFun:
    def __init__(self):
        self.activeweb = ActiveWeb()   #实例化
        self.loginpage = LoginPage()   #实例化


    def checkResult(self,result,preresult):
        """
        实际结果与预期结果比较
        """
        if result == preresult:
            self.activeweb.printgreenword()
            print("测试通过")
            self.activeweb.printnormalword()
        else:
            self.activeweb.printredword()
            print("测试失败，失败描述：实际结果为%s,与预期结果%s不一致"% (result,preresult))
            self.activeweb.printnormalword()

    def checkTextEle(self,checkele,preresult):
        """
        页面text文本内容检查
        """
        result = self.activeweb.findElementByXpathAndReturnText(checkele)
        self.checkResult(result,preresult)

    def checkValueEle(self,checkele,checkvalue,preresult):
        """
        页面输入框默认内容检查
        """
        result = self.activeweb.findElementByXpathAndReturnValue(checkele,checkvalue)
        self.checkResult(result,preresult)
