# _*_ coding:utf-8 _*_

__author__ = 'bobby'
__date__ = '2018/7/27 12:24'
import unittest

import HTMLTestRunner
from project.manager.forgetpasswordpagemanager import ForgetPasswordPage
from base.activebase import ActiveWeb

class TestForgetPasswordPage(unittest.TestCase):   #创建测试类
    # def __init__(self):
    #     self.forgetpasswordpage = LoginPage()  #实例化

    @classmethod   #类方法，只执行一次，但必须要加注解@classmethod,且名字固定为setUpClass
    def setUpClass(cls):
       pass

    @classmethod   #类方法，只执行一次，但必须要加注解@classmethod,且名字固定为tearDownClass
    def tearDownClass(cls):
        pass

    def setUp(self):   #每条用例执行测试之前都要执行此方法
        self.forgetpasswordpage = ForgetPasswordPage()  # 实例化
        self.activeweb = ActiveWeb()   #实例化
        url = "https://bjw.halodigit.com:9090/nereus/manager/retrive"   #管理后台
        # url = "https://bjw.halodigit.com:9090/nereus/agent/index#/login"
        self.activeweb.getUrl(url)   #启动web
        self.activeweb.delayTime(10)

    def tearDown(self):   #每条用例执行测试之后都要执行此方法
        self.activeweb.closeBrowse()
        # pass

    @unittest.skip('test_01')   #跳过用例名字为‘test_01’的用例，跳过的用例的执行结果显示：是
    def test_01(self):   #找回密码页找回密码框title检查
        """
        找回密码页找回密码框title检查
        """
        forgetpasswordtitle = self.activeweb.findElementByXpathAndReturnText(0,self.forgetpasswordpage.forgetpasswordtitle)
        print('实际结果：',forgetpasswordtitle)
        preforgetpasswordtitle = "Forget password"
        self.assertEqual(forgetpasswordtitle,preforgetpasswordtitle)

    @unittest.skip('test_02')  # 跳过用例名字为‘test_01’的用例，跳过的用例的执行结果显示：是
    def test_02(self):   #找回密码页账号输入框默认文字检查
        """
        找回密码页账号输入框默认文字检查
        """
        account = self.activeweb.findElementByXpathAndReturnValue(self.forgetpasswordpage.account,"placeholder")
        print('实际结果：',account)
        preaccount = "Your Email address"
        self.assertEqual(account,preaccount)

    @unittest.skip('test_03')  # 跳过用例名字为‘test_01’的用例，跳过的用例的执行结果显示：是
    def test_03(self):   #找回密码页账号输入为空时的文字提示
        """
        找回密码页账号输入为空时的文字提示
        """
        self.activeweb.findElementByXpathAndClick(self.forgetpasswordpage.account)
        self.activeweb.delayTime(3)
        self.activeweb.findElementByXpathAndClick(self.forgetpasswordpage.vercode)
        self.activeweb.delayTime(3)
        self.activeweb.findElementByXpathAndClick(self.forgetpasswordpage.account)
        self.activeweb.delayTime(3)
        accounttip = self.activeweb.findElementByXpathAndReturnText(0,self.forgetpasswordpage.accounttip)
        print('实际结果：',accounttip)
        preaccounttip = "This option cannot be empty"
        self.assertEqual(accounttip,preaccounttip)

    @unittest.skip('test_04')
    def test_04(self):   #找回密码页,验证码默认文字提示
        """
        找回密码页,验证码默认文字提示
        """
        vercodedisplay = self.activeweb.findElementByXpathAndReturnValue(self.forgetpasswordpage.vercode,"placeholder")
        print('实际结果：',vercodedisplay)
        prevercodedisplay = "Verification code"
        self.assertEqual(vercodedisplay,prevercodedisplay)

    @unittest.skip('test_05')
    def test_05(self):   #找回密码页，验证码输入内容为空时提示
        """
        找回密码页，验证码输入内容为空时提示
        """
        self.activeweb.findElementByXpathAndClick(self.forgetpasswordpage.vercode)
        self.activeweb.findElementByXpathAndClick(self.forgetpasswordpage.account)
        vercodetip = self.activeweb.findElementByXpathAndReturnText(0,self.forgetpasswordpage.accounttip)
        print('实际结果：',vercodetip)
        prevercodetip = "Please enter verification code"
        self.assertEqual(vercodetip,prevercodetip)

    @unittest.skip('test_06')
    def test_06(self):   #找回密码页,账号格式不是邮箱类型,不是类似1@1格式,123456,@,1@,@1,
        """
        找回密码页,账号格式不是邮箱类型,不是类似1@1格式,123456,@,1@,@1,
        """
        self.activeweb.findElementByXpathAndInput(self.forgetpasswordpage.account,"1")
        self.activeweb.findElementByXpathAndClick(self.forgetpasswordpage.vercode)
        self.activeweb.delayTime(3)
        accounttip = self.activeweb.findElementByXpathAndReturnText(0,self.forgetpasswordpage.accounttip)
        print('实际结果：',accounttip)
        preaccounttip = "Please enter the correct email address"
        self.assertEqual(accounttip,preaccounttip)

    @unittest.skip('test_07')
    def test_07(self):   #找回密码页，验证码输入长度小于4提示
        """
        找回密码页，验证码输入长度小于4提示
        """
        self.activeweb.findElementByXpathAndInput(self.forgetpasswordpage.vercode, "123")
        self.activeweb.findElementByXpathAndClick(self.forgetpasswordpage.account)
        self.activeweb.delayTime(5)
        codetip = self.activeweb.findElementByXpathAndReturnText(0,self.forgetpasswordpage.accounttip)
        print('实际结果：',codetip)
        precodetip= "The length cannot be less than4"
        self.assertEqual(codetip,precodetip)

    @unittest.skip('test_08')
    def test_08(self):   #找回密码页，验证码输入长度大于4提示
        """
        找回密码页，验证码输入长度大于4提示
        """
        self.activeweb.findElementByXpathAndInput(self.forgetpasswordpage.vercode, "12345")
        self.activeweb.findElementByXpathAndClick(self.forgetpasswordpage.account)
        self.activeweb.delayTime(5)
        codetip = self.activeweb.findElementByXpathAndReturnText(0,self.forgetpasswordpage.accounttip)
        print('实际结果：',codetip)
        precodetip= "The length cannot be more than4"
        self.assertEqual(codetip,precodetip)

    @unittest.skip('test_09')
    def test_09(self):   #找回密码页，验证码输入错误提示
        """
        找回密码页，验证码输入错误提示
        """
        self.activeweb.findElementByXpathAndInput(self.forgetpasswordpage.account,"1@1")
        self.activeweb.findElementByXpathAndInput(self.forgetpasswordpage.vercode, "1234")
        self.activeweb.findElementByXpathAndClick(self.forgetpasswordpage.resetpasswordbutton)
        self.activeweb.delayTime(5)
        resetpasswordbuttontip = self.activeweb.findElementByXpathAndReturnText(0,self.forgetpasswordpage.resetpasswordbuttontip)
        print('实际结果：',resetpasswordbuttontip)
        preresetpasswordbuttontip= "Incorrect validation code"
        self.assertEqual(resetpasswordbuttontip,preresetpasswordbuttontip)


    # @unittest.skip('test_10')
    def test_10(self):   #点击验证码判断验证码是否更新
        """
        点击验证码判断验证码是否更新
        """
        self.activeweb.delayTime(3)
        codetext = self.activeweb.getcodetext(self.forgetpasswordpage.code)

        print("验证码1：",codetext)
        self.activeweb.findElementByXpathAndClick(self.forgetpasswordpage.code)
        self.activeweb.delayTime(3)
        codetext2 = self.activeweb.getcodetext(self.forgetpasswordpage.code)
        print("验证码2：",codetext2)
        self.assertNotEqual(codetext,codetext2)

    @unittest.skip('test_11')
    def test_11(self):   #点击返回登录跳转到返回登录页
        """
        点击返回登录查看是否跳转到登录页
        """
        self.activeweb.findElementByXpathAndClick(self.forgetpasswordpage.backtologin)
        self.activeweb.delayTime(5)
        url  = self.activeweb.driver.current_url
        print("当前页面实际url：",url)
        preurl = "https://bjw.halodigit.com:9090/nereus/manager/index#/login"
        self.assertEqual(url,preurl)






# if __name__ == '__main__':
#     # # unittest.main()
#     # #使用HTMLTestRunner跑
#     # filepath = "./report/htmlreport.html"   #放置报告的路径
#     # fp = open(filepath,'wb')   #资源流,以读写的方式打开 file用open替代即可
#     # suite = unittest.TestSuite()  #创建一个用例容器
#     # suite.addTest(TestLoginPage('test_05'))
#     # runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='this is a report',description='report description')   #设置报告的标题和描述
#     # runner.run(suite)  #执行用例集suite



