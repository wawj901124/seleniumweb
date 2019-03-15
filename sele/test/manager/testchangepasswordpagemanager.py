# _*_ coding:utf-8 _*_

__author__ = 'bobby'
__date__ = '2018/7/27 12:24'
import unittest

import HTMLTestRunner
from project.manager.changepasswordpagemanager import ChangePasswordPage
from test.manager.fun.loginfun import LoginManager
from base.activebase import ActiveWeb

class TestChangePasswordPage(unittest.TestCase):   #创建测试类
    # def __init__(self):
    #     self.changepasswordpage = LoginPage()  #实例化

    loginmanager = LoginManager()   #实例化
    global cookie
    global loginurl
    cookie = loginmanager.cookie
    loginurl = loginmanager.loginurl

    

    @classmethod   #类方法，只执行一次，但必须要加注解@classmethod,且名字固定为setUpClass
    def setUpClass(cls):
        pass

    @classmethod   #类方法，只执行一次，但必须要加注解@classmethod,且名字固定为tearDownClass
    def tearDownClass(cls):
        pass

    def setUp(self):   #每条用例执行测试之前都要执行此方法
        self.changepasswordpage = ChangePasswordPage()  # 实例化
        #登录
        self.activeweb = ActiveWeb()   #实例化
        url = "https://bjw.halodigit.com:9090/nereus/manager/index#/account/changePwd"   #管理后台修改密码页面
        self.activeweb.writerCookies(cookie,loginurl,url) #启动web
        
    def tearDown(self):   #每条用例执行测试之后都要执行此方法
        self.activeweb.closeBrowse()
        # pass

    @unittest.skip('test_01')   #跳过用例名字为‘test_01’的用例，跳过的用例的执行结果显示：是
    def test_01(self):   #修改密码页title检查
        """
        修改密码页title检查
        """
        changepasswordtitle = self.activeweb.findElementByXpathAndReturnText(0,self.changepasswordpage.changepaswordtitle)
        print('实际结果：',changepasswordtitle)
        prechangepasswordtitle = "Change password"
        self.assertEqual(changepasswordtitle,prechangepasswordtitle)

    @unittest.skip('test_02')  # 跳过用例名字为‘test_01’的用例，跳过的用例的执行结果显示：是
    def test_02(self):   #修改密码页原密码输入框默认文字显示检查
        """
        修改密码页原密码输入框默认文字显示检查
        """
        currentpassword = self.activeweb.findElementByXpathAndReturnValue(self.changepasswordpage.currentpasswordinput,"placeholder")
        print('实际结果：',currentpassword)
        precurrentpassword = "Please key in..."
        self.assertEqual(currentpassword,precurrentpassword)
        
    @unittest.skip('test_03')  # 跳过用例名字为‘test_01’的用例，跳过的用例的执行结果显示：是
    def test_03(self):   #修改密码页新密码输入框默认文字显示检查
        """
        修改密码页新密码输入框默认文字显示检查
        """
        newpassword = self.activeweb.findElementByXpathAndReturnValue(self.changepasswordpage.newpasswordinput,"placeholder")
        print('实际结果：',newpassword)
        prenewpassword  = "Please key in..."
        self.assertEqual(newpassword ,prenewpassword )

    @unittest.skip('test_04')  # 跳过用例名字为‘test_01’的用例，跳过的用例的执行结果显示：是
    def test_04(self):   #修改密码页确认密码输入框默认文字显示检查
        """
        修改密码页确认密码输入框默认文字显示检查
        """
        confirmpassword = self.activeweb.findElementByXpathAndReturnValue(self.changepasswordpage.confirmpasswordinput,"placeholder")
        print('实际结果：',confirmpassword)
        preconfirmpassword  = "Please key in..."
        self.assertEqual(confirmpassword ,preconfirmpassword)

    @unittest.skip('test_05')  # 跳过用例名字为‘test_01’的用例，跳过的用例的执行结果显示：是
    def test_05(self):   #修改密码页原密码输入为空时的文字提示
        """
        修改密码页原密码输入为空时的文字提示
        """
        self.activeweb.findElementByXpathAndClick(self.changepasswordpage.currentpasswordinput)
        self.activeweb.delayTime(3)
        self.activeweb.findElementByXpathAndClick(self.changepasswordpage.newpasswordinput)
        self.activeweb.delayTime(3)
        self.activeweb.findElementByXpathAndClick(self.changepasswordpage.currentpasswordinput)
        self.activeweb.delayTime(3)
        accounttip = self.activeweb.findElementByXpathAndReturnText(0,self.changepasswordpage.currentpasswordtip)
        print('实际结果：',accounttip)
        preaccounttip = "This option cannot be empty"
        self.assertEqual(accounttip,preaccounttip)

    @unittest.skip('test_06')  # 跳过用例名字为‘test_01’的用例，跳过的用例的执行结果显示：是
    def test_06(self):   #修改密码页新密码输入为空时的文字提示
        """
        修改密码页原密码输入为空时的文字提示
        """
        self.activeweb.findElementByXpathAndClick(self.changepasswordpage.currentpasswordinput)
        self.activeweb.delayTime(3)
        self.activeweb.findElementByXpathAndClick(self.changepasswordpage.newpasswordinput)
        self.activeweb.delayTime(3)
        self.activeweb.findElementByXpathAndClick(self.changepasswordpage.currentpasswordinput)
        self.activeweb.delayTime(3)
        accounttip = self.activeweb.findElementByXpathAndReturnText(0,self.changepasswordpage.newpasswordtip)
        print('实际结果：',accounttip)
        preaccounttip = "This option cannot be empty"
        self.assertEqual(accounttip,preaccounttip)

    @unittest.skip('test_07')  # 跳过用例名字为‘test_01’的用例，跳过的用例的执行结果显示：是
    def test_07(self):   #修改密码页确认密码输入为空时的文字提示
        """
        修改密码页确认密码输入为空时的文字提示
        """
        self.activeweb.findElementByXpathAndClick(self.changepasswordpage.confirmpasswordinput)
        self.activeweb.delayTime(3)
        self.activeweb.findElementByXpathAndClick(self.changepasswordpage.newpasswordinput)
        self.activeweb.delayTime(3)
        accounttip = self.activeweb.findElementByXpathAndReturnText(0,self.changepasswordpage.confirmpasswordtip)
        print('实际结果：',accounttip)
        preaccounttip = "This option cannot be empty"
        self.assertEqual(accounttip,preaccounttip)

    @unittest.skip('test_08')
    def test_08(self):   #修改密码页原密码输入少于6位提示
        """
        修改密码页原密码输入少于6位提示
        """
        self.activeweb.findElementByXpathAndInput(self.changepasswordpage.currentpasswordinput, "12345")
        self.activeweb.findElementByXpathAndClick(self.changepasswordpage.newpasswordinput)
        self.activeweb.delayTime(5)
        currentpasswordtip = self.activeweb.findElementByXpathAndReturnText(0,self.changepasswordpage.currentpasswordtip)
        print('实际结果：',currentpasswordtip)
        precurrentpasswordtip= "The length cannot be less than6"
        self.assertEqual(currentpasswordtip,precurrentpasswordtip)

    @unittest.skip('test_09')
    def test_09(self):   #修改密码页原密码输入大于16位提示
        """
        修改密码页原密码输入大于16位提示
        """
        self.activeweb.findElementByXpathAndInput(self.changepasswordpage.currentpasswordinput, "12345678901234567")
        self.activeweb.findElementByXpathAndClick(self.changepasswordpage.newpasswordinput)
        self.activeweb.delayTime(5)
        currentpasswordtip = self.activeweb.findElementByXpathAndReturnText(0,self.changepasswordpage.currentpasswordtip)
        print('实际结果：',currentpasswordtip)
        precurrentpasswordtip= "The length cannot be more than16"
        self.assertEqual(currentpasswordtip,precurrentpasswordtip)

    @unittest.skip('test_10')
    def test_10(self):   #修改密码页新密码输入少于6位提示
        """
        修改密码页新密码输入少于6位提示
        """
        self.activeweb.findElementByXpathAndInput(self.changepasswordpage.newpasswordinput, "12345")
        self.activeweb.findElementByXpathAndClick(self.changepasswordpage.confirmpasswordinput)
        self.activeweb.delayTime(5)
        newpasswordtip = self.activeweb.findElementByXpathAndReturnText(0,self.changepasswordpage.newpasswordtip)
        print('实际结果：',newpasswordtip)
        prenewpasswordtip= "The length cannot be less than6"
        self.assertEqual(newpasswordtip,prenewpasswordtip)

    @unittest.skip('test_11')
    def test_11(self):   #修改密码页新密码输入大于16位提示
        """
        修改密码页新密码输入大于16位提示
        """
        self.activeweb.findElementByXpathAndInput(self.changepasswordpage.newpasswordinput, "12345678901234567")
        self.activeweb.findElementByXpathAndClick(self.changepasswordpage.confirmpasswordinput)
        self.activeweb.delayTime(5)
        newpasswordtip = self.activeweb.findElementByXpathAndReturnText(0,self.changepasswordpage.newpasswordtip)
        print('实际结果：',newpasswordtip)
        prenewpasswordtip= "The length cannot be more than16"
        self.assertEqual(newpasswordtip,prenewpasswordtip)

    @unittest.skip('test_12')
    def test_12(self):   #修改密码页确认密码输入框提示
        """
        修改密码页确认密码输入框提示
        """
        self.activeweb.findElementByXpathAndInput(self.changepasswordpage.confirmpasswordinput, "1")
        self.activeweb.findElementByXpathAndClick(self.changepasswordpage.newpasswordinput)
        self.activeweb.delayTime(5)
        confirmpasswordtip = self.activeweb.findElementByXpathAndReturnText(0,self.changepasswordpage.confirmpasswordtip)
        print('实际结果：',confirmpasswordtip)
        preconfirmpasswordtip= "New password entered inconsistently"
        self.assertEqual(confirmpasswordtip,preconfirmpasswordtip)

    @unittest.skip('test_13')
    def test_13(self):   #修改密码成功
        """
        修改密码页修改密码成功
        """
        self.activeweb.findElementByXpathAndInput(self.changepasswordpage.currentpasswordinput, "123456")
        self.activeweb.findElementByXpathAndInput(self.changepasswordpage.newpasswordinput, "123456")
        self.activeweb.findElementByXpathAndInput(self.changepasswordpage.confirmpasswordinput, "123456")
        self.activeweb.findElementByXpathAndClick(self.changepasswordpage.submintbutton)
        self.activeweb.delayTime(5)
        currentpassword = self.activeweb.findElementByXpathAndReturnValue(self.changepasswordpage.currentpasswordinput,"placeholder")
        newpassword = self.activeweb.findElementByXpathAndReturnValue(self.changepasswordpage.newpasswordinput,"placeholder")
        confirmpassword = self.activeweb.findElementByXpathAndReturnValue(self.changepasswordpage.confirmpasswordinput,"placeholder")
        print('实际结果：', currentpassword)
        pre = "Please key in..."
        self.assertEqual(currentpassword,pre)
        self.assertEqual(newpassword, pre)
        self.assertEqual(confirmpassword, pre)



# if __name__ == '__main__':
#     # # unittest.main()
#     # #使用HTMLTestRunner跑
#     # filepath = "./report/htmlreport.html"   #放置报告的路径
#     # fp = open(filepath,'wb')   #资源流,以读写的方式打开 file用open替代即可
#     # suite = unittest.TestSuite()  #创建一个用例容器
#     # suite.addTest(TestLoginPage('test_05'))
#     # runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='this is a report',description='report description')   #设置报告的标题和描述
#     # runner.run(suite)  #执行用例集suite



