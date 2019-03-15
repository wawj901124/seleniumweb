# _*_ coding:utf-8 _*_

__author__ = 'bobby'
__date__ = '2018/7/27 12:24'
import unittest

import HTMLTestRunner
from base.activebase import ActiveWeb   #导入ActiveWeb
from project.merchant.loginpagemerchant import LoginPage  #导入LoginPage页

class Test(unittest.TestCase):   #创建测试类

    @classmethod   #类方法，只执行一次，但必须要加注解@classmethod,且名字固定为setUpClass
    def setUpClass(cls):
       pass

    @classmethod   #类方法，只执行一次，但必须要加注解@classmethod,且名字固定为tearDownClass
    def tearDownClass(cls):
        pass

    def setUp(self):   #每条用例执行测试之前都要执行此方法
        self.activeweb = ActiveWeb()   #实例化
        self.loginpage = LoginPage()   #实例化

        url = "https://bjw.halodigit.com:9090/nereus/merchant/index#/login"   #商户后台
        # url = "https://m-mbmpay.ahdipay.com/nereus/agent/index"   #现网
        self.activeweb.getUrl(url)   #打开网址
        # self.activeweb.findElementByXpathAndInput(self.loginpage.account,"6281122336666")
        # self.activeweb.findElementByXpathAndInput(self.loginpage.password, "abc123456")
        # # self.activeweb.findElementByXpathAndInput(self.loginpage.account,"6281285610481")    #现网
        # # self.activeweb.findElementByXpathAndInput(self.loginpage.password, "abc123456")   #现网
        # self.activeweb.findElementByXpathAndClick(self.loginpage.loginbutton)
        # self.activeweb.delayTime(3)

    def tearDown(self):   #每条用例执行测试之后都要执行此方法
        self.activeweb.closeBrowse()
        # pass


    #@unittest.skip('test_02')  # 跳过用例名字为‘test_01’的用例，跳过的用例的执行结果显示：是
    def test_02(self):   #登录页账号输入框默认文字检查
        """
        登录页账号输入框默认文字检查
        """
        account = self.activeweb.findElementByXpathAndReturnValue(self.loginpage.account,"placeholder")
        print('实际结果：',account)
        preaccount = "QR Account number"
        self.assertEqual(account,preaccount)

    #@unittest.skip('test_03')  # 跳过用例名字为‘test_01’的用例，跳过的用例的执行结果显示：是
    def test_03(self):   #登录页密码输入框默认文字检查
        """
        登录页密码输入框默认文字检查
        """
        password = self.activeweb.findElementByXpathAndReturnValue(self.loginpage.password,"placeholder")
        print('实际结果：',password)
        prepassword = "Password"
        self.assertEqual(password,prepassword)

    #@unittest.skip('test_04')  # 跳过用例名字为‘test_01’的用例，跳过的用例的执行结果显示：是
    def test_04(self):   #登录页登录账号输入为空时的文字提示
        """
        登录页登录账号输入为空时的文字提示
        """
        self.activeweb.findElementByXpathAndClick(self.loginpage.account)
        self.activeweb.delayTime(3)
        self.activeweb.findElementByXpathAndClick(self.loginpage.password)
        self.activeweb.delayTime(3)
        self.activeweb.findElementByXpathAndClick(self.loginpage.account)
        self.activeweb.delayTime(3)
        accounttip = self.activeweb.findElementByXpathAndReturnText(0,self.loginpage.accounttip)
        print('实际结果：',accounttip)
        preaccounttip = "This option cannot be empty"
        self.assertEqual(accounttip,preaccounttip)

    #@unittest.skip('test_05')  # 跳过用例名字为‘test_01’的用例，跳过的用例的执行结果显示：是
    def test_05(self):   #登录页登录密码输入为空时的文字提示
        """
        登录页登录密码输入为空时的文字提示
        """
        self.activeweb.findElementByXpathAndClick(self.loginpage.account)
        self.activeweb.delayTime(3)
        self.activeweb.findElementByXpathAndClick(self.loginpage.password)
        self.activeweb.delayTime(3)
        self.activeweb.findElementByXpathAndClick(self.loginpage.account)
        self.activeweb.delayTime(3)
        passwordtip = self.activeweb.findElementByXpathAndReturnText(0,self.loginpage.passwordtip)
        print('实际结果：',passwordtip)
        prepasswordtip = "This option cannot be empty"
        self.assertEqual(passwordtip,prepasswordtip)

    #@unittest.skip('test_07')
    def test_07(self):   #登录页,账号长度小于10位提示
        """
        登录页,账号长度小于10位提示
        """
        self.activeweb.findElementByXpathAndInput(self.loginpage.account,"123456789")
        self.activeweb.findElementByXpathAndClick(self.loginpage.password)
        self.activeweb.delayTime(3)
        passwordtip = self.activeweb.findElementByXpathAndReturnText(0,self.loginpage.accounttip)
        print('实际结果：',passwordtip)
        prepasswordtip = "The length cannot be less than10"
        self.assertEqual(passwordtip,prepasswordtip)

    #@unittest.skip('test_07')
    def test_08(self):   #登录页,账号长度大于15位提示
        """
        登录页,账号长度大于15位提示
        """
        self.activeweb.findElementByXpathAndInput(self.loginpage.account,"1234567890123456")
        self.activeweb.findElementByXpathAndClick(self.loginpage.password)
        self.activeweb.delayTime(3)
        passwordtip = self.activeweb.findElementByXpathAndReturnText(0,self.loginpage.accounttip)
        print('实际结果：',passwordtip)
        prepasswordtip = "The length cannot be more than15"
        self.assertEqual(passwordtip,prepasswordtip)

    #@unittest.skip('test_09')
    def test_09(self):   #登录页,密码长度小于6位提示
        """
        登录页,密码长度小于6位提示
        :return:
        """
        self.activeweb.findElementByXpathAndInput(self.loginpage.password,"12345")
        self.activeweb.findElementByXpathAndClick(self.loginpage.account)
        self.activeweb.delayTime(3)
        passwordtip = self.activeweb.findElementByXpathAndReturnText(0,self.loginpage.accounttip)
        print('实际结果：',passwordtip)
        prepasswordtip = "The length cannot be less than6"
        self.assertEqual(passwordtip,prepasswordtip)

    #@unittest.skip('test_10')
    def test_10(self):   #登录页,密码长度大于24位提示
        """
        登录页,密码长度大于16位提示
        """
        self.activeweb.findElementByXpathAndInput(self.loginpage.password,"1234567890123456789012345")
        self.activeweb.findElementByXpathAndClick(self.loginpage.account)
        self.activeweb.delayTime(3)
        passwordtip = self.activeweb.findElementByXpathAndReturnText(0,self.loginpage.accounttip)
        print('实际结果：',passwordtip)
        prepasswordtip = "The length cannot be more than24"
        self.assertEqual(passwordtip,prepasswordtip)

    #@unittest.skip('test_11')
    def test_11(self):   #登录页,账号与密码错误时，点击登录，账号密码错误提示
        """
        登录页,账号与密码错误时，点击登录，账号密码错误提示
        """
        self.activeweb.findElementByXpathAndInput(self.loginpage.account,"12345678901")
        self.activeweb.findElementByXpathAndInput(self.loginpage.password, "123456")
        self.activeweb.findElementByXpathAndClick(self.loginpage.loginbutton)
        self.activeweb.delayTime(5)
        logintip = self.activeweb.findElementByXpathAndReturnText(0,self.loginpage.logintip)
        print('实际结果：',logintip)
        prelogintip = "Incorrect account or password"
        self.assertEqual(logintip,prelogintip)

    #@unittest.skip('test_12')
    def test_12(self):   #登录页,账号与密码错误时，点击登录，出现验证码提示
        """
        登录页,账号与密码错误时，点击登录，出现验证码提示
        """
        self.activeweb.findElementByXpathAndInput(self.loginpage.account,"12345678901")
        self.activeweb.findElementByXpathAndInput(self.loginpage.password, "123456")
        self.activeweb.findElementByXpathAndClick(self.loginpage.loginbutton)
        self.activeweb.delayTime(5)
        logintip = self.activeweb.findElementByXpathAndReturnValue(self.loginpage.vercode,"placeholder")
        print('实际结果：',logintip)
        prelogintip = "Verification code"
        self.assertEqual(logintip,prelogintip)

    #@unittest.skip('test_13')
    def test_13(self):   #登录页,账号与密码错误时，点击登录，验证码输入内容为空时提示
        """
        登录页,账号与密码错误时，点击登录，验证码输入内容为空时提示
        """
        self.activeweb.findElementByXpathAndInput(self.loginpage.account,"12345678901")
        self.activeweb.findElementByXpathAndInput(self.loginpage.password, "123456")
        self.activeweb.findElementByXpathAndClick(self.loginpage.loginbutton)
        self.activeweb.delayTime(5)
        self.activeweb.findElementByXpathAndClick(self.loginpage.vercode)
        self.activeweb.findElementByXpathAndClick(self.loginpage.account)
        vercodetip = self.activeweb.findElementByXpathAndReturnText(0,self.loginpage.accounttip)
        print('实际结果：',vercodetip)
        prevercodetip = "This option cannot be empty"
        self.assertEqual(vercodetip,prevercodetip)

    #@unittest.skip('test_14')
    def test_14(self):   #登录页,账号与密码输入，输入错误的验证码，点击登录，验证码输入错误提示
        """
        登录页,账号与密码输入，输入错误的验证码，点击登录，验证码输入错误提示
        """
        self.activeweb.findElementByXpathAndInput(self.loginpage.account,"12345678901")
        self.activeweb.findElementByXpathAndInput(self.loginpage.password, "123456")
        self.activeweb.findElementByXpathAndClick(self.loginpage.loginbutton)
        self.activeweb.delayTime(5)
        self.activeweb.findElementByXpathAndInput(self.loginpage.password, "123456")
        self.activeweb.findElementByXpathAndInput(self.loginpage.vercode, "1234")
        self.activeweb.findElementByXpathAndClick(self.loginpage.loginbutton)
        self.activeweb.delayTime(5)
        vercodetip = self.activeweb.findElementByXpathAndReturnText(0,self.loginpage.logintip)
        print('实际结果：',vercodetip)
        prevercodetip = "Incorrect validation code"
        self.assertEqual(vercodetip,prevercodetip)

    #@unittest.skip('test_15')
    def test_15(self):   #点击验证码判断验证码是否更新
        """
        点击验证码判断验证码是否更新
        """
        self.activeweb.findElementByXpathAndInput(self.loginpage.account,"12345678901")
        self.activeweb.findElementByXpathAndInput(self.loginpage.password, "123456")
        self.activeweb.findElementByXpathAndClick(self.loginpage.loginbutton)
        self.activeweb.delayTime(5)
        codetext = self.activeweb.getcodetext(self.loginpage.code)
        print("验证码1：",codetext)
        self.activeweb.findElementByXpathAndClick(self.loginpage.code)
        self.activeweb.delayTime(3)
        codetext2 = self.activeweb.getcodetext(self.loginpage.code)
        print("验证码2：",codetext2)
        self.assertNotEqual(codetext,codetext2)
        
    #@unittest.skip('test_16')
    def test_16(self):   #非代理商的正确的钱包账号登录提示
        """
        点击验证码判断验证码是否更新
        """
        self.activeweb.findElementByXpathAndInput(self.loginpage.account,"6281122337788")
        self.activeweb.findElementByXpathAndInput(self.loginpage.password, "a123456")
        self.activeweb.findElementByXpathAndClick(self.loginpage.loginbutton)
        self.activeweb.delayTime(5)
        logintip = self.activeweb.findElementByXpathAndReturnText(0,self.loginpage.logintip)
        prelogintip = "You are not AHDI merchant yet"
        self.assertEqual(logintip,prelogintip)









# if __name__ == '__main__':
#     # # unittest.main()
#     # #使用HTMLTestRunner跑
#     # filepath = "./report/htmlreport.html"   #放置报告的路径
#     # fp = open(filepath,'wb')   #资源流,以读写的方式打开 file用open替代即可
#     # suite = unittest.TestSuite()  #创建一个用例容器
#     # suite.addTest(TestLoginPage('test_05'))
#     # runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='this is a report',description='report description')   #设置报告的标题和描述
#     # runner.run(suite)  #执行用例集suite



