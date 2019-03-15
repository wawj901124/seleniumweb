# _*_ coding:utf-8 _*_

__author__ = 'bobby'
__date__ = '2018/7/27 12:24'
import unittest

import HTMLTestRunner
from base.activebase import ActiveWeb   #导入ActiveWeb
from project.agent.loginpageagent import LoginPage   #导入LoginPage页
from project.agent.addmerchantpage import AddMerchantPage   #导入AddMerchantPage页
from project.agent.addmerchantpage import AddMerchantPageCompany   #导入AddMerchantPageCompany页
from project.agent.addmeichantpagedonepage import AddMerchantDonePage   #导入AddMerchantDonePage页

class TestAddMerchantPage(unittest.TestCase):   #创建测试类

    @classmethod   #类方法，只执行一次，但必须要加注解@classmethod,且名字固定为setUpClass
    def setUpClass(cls):
       pass

    @classmethod   #类方法，只执行一次，但必须要加注解@classmethod,且名字固定为tearDownClass
    def tearDownClass(cls):
        pass

    def setUp(self):   #每条用例执行测试之前都要执行此方法
        self.activeweb = ActiveWeb()   #实例化
        self.loginpage = LoginPage()   #实例化
        self.addmerchantpage = AddMerchantPage() # 实例化
        self.addmerchantdonepage = AddMerchantDonePage()   #实例化
        self.addmerchantpagecompany = AddMerchantPageCompany()   #实例化

        url = "https://bjw.halodigit.com:9090/nereus/agent/index"   #代理商后台
        # url = "https://m-mbmpay.ahdipay.com/nereus/agent/index"   #现网
        self.activeweb.getUrl(url)   #打开网址
        self.activeweb.findElementByXpathAndInput(self.loginpage.account,"6281122336666")
        self.activeweb.findElementByXpathAndInput(self.loginpage.password, "abc123456")
        # self.activeweb.findElementByXpathAndInput(self.loginpage.account,"6281285610481")    #现网
        # self.activeweb.findElementByXpathAndInput(self.loginpage.password, "abc123456")   #现网
        self.activeweb.findElementByXpathAndClick(self.loginpage.loginbutton)
        self.activeweb.delayTime(3)
        self.activeweb.findElementByXpathAndClick("/html/body/div[3]/div[1]/div/ul/li/ul/li/a[2]")   #点击"Add merchant"
        self.activeweb.delayTime(3)

    def tearDown(self):   #每条用例执行测试之后都要执行此方法
        # self.addmerchantpage.activebase.closeBrowse()
        pass

    @unittest.skip('test_01')   #跳过用例名字为‘test_01’的用例，跳过的用例的执行结果显示：是
    def test_01(self):   #添加个人商户
        """
        添加页面元素
        :return:
        """
        writebrandname  = "123456"
        writeremail = "xiangkaizheng@iapppay.com"
        writercontactnumber = "abc123456"
        writermerchanttype = "Individu"
        writercategory = "TAXICABS & LIMOUSINES"
        writercriteria = "Medium"
        writersiup = "abc123456"
        writerprovince = "JAMBI"
        writercity = "Kab. Bungo"
        writerdistrict = "abc123456"
        writervillage = "abc123456"
        writerpostcode = "abc123456"
        writeraddress = "abc123456"
        writerphotosiup = "D:\\pic\\1.png"
        writerphotonpwpcompany = "D:\\pic\\1.png"
        writerphototdp = "D:\\pic\\1.png"

        writername = "abc123456"
        writertypeid = "KTP"
        writeridentitynumber = "abc123456"
        writernpwp = "abc123456"
        writeraddresstwo = "abc123456"
        writernationality = "Indonesian"
        writerphone = "abc123456"
        writeremailtwo = "xiangkaizheng@iapppay.com"
        writerphotofullfacebust = "D:\\pic\\1.png"

        writerlocationphoto = "D:\\pic\\1.png"
        writerphotoofthecashiersdesk = "D:\\pic\\1.png"
        writerotherphoto = "D:\\pic\\1.png"

        writerbank = "BCA"
        writeraccountname = "abc123456"
        writeraccountnumber = "abc123456"

        self.writerqrindoamount = "6281122336666"



        self.activeweb.findElementByXpathAndInput(self.addmerchantpage.brandnameinput, writebrandname)
        self.activeweb.findElementByXpathAndInput(self.addmerchantpage.emailinput, writeremail)
        self.activeweb.findElementByXpathAndInput(self.addmerchantpage.contactnumberinput, writercontactnumber)
        self.activeweb.findElementByXpathAndReturnOptions(self.addmerchantpage.merchanttypeselect,writermerchanttype)
        self.activeweb.findElementByXpathAndReturnOptions(self.addmerchantpage.categoryselect, writercategory)
        self.activeweb.findElementByXpathAndReturnOptions(self.addmerchantpage.criteriaselect, writercriteria)
        self.activeweb.findElementByXpathAndInput(self.addmerchantpage.siupinput, writersiup)
        self.activeweb.findElementByXpathAndReturnOptions(self.addmerchantpage.provinceselect, writerprovince)
        self.activeweb.findElementByXpathAndReturnOptions(self.addmerchantpage.cityselect, writercity)
        self.activeweb.findElementByXpathAndInput(self.addmerchantpage.districtinput, writerdistrict)
        self.activeweb.findElementByXpathAndInput(self.addmerchantpage.villageinput, writervillage)
        self.activeweb.findElementByXpathAndInput(self.addmerchantpage.postcodeinput, writerpostcode)
        self.activeweb.findElementByXpathAndInput(self.addmerchantpage.addressinput, writeraddress)
        self.activeweb.findElementByXpathAndAndFile(self.addmerchantpage.photosiupimage, writerphotosiup)
        self.activeweb.findElementByXpathAndAndFile(self.addmerchantpage.photonpwpcompanyimage, writerphotonpwpcompany)
        self.activeweb.findElementByXpathAndAndFile(self.addmerchantpage.phototdpimage, writerphototdp)

        self.activeweb.findElementByXpathAndInput(self.addmerchantpage.nameinput, writername)
        self.activeweb.findElementByXpathAndReturnOptions(self.addmerchantpage.typeidselect, writertypeid)
        self.activeweb.findElementByXpathAndInput(self.addmerchantpage.identitynumberinput, writeridentitynumber)
        self.activeweb.findElementByXpathAndInput(self.addmerchantpage.npwpinput, writernpwp)
        self.activeweb.findElementByXpathAndInput(self.addmerchantpage.addresstwoinput, writeraddresstwo)
        self.activeweb.findElementByXpathAndReturnOptions(self.addmerchantpage.nationalityselect, writernationality)
        self.activeweb.findElementByXpathAndInput(self.addmerchantpage.phoneinput, writerphone)
        self.activeweb.findElementByXpathAndInput(self.addmerchantpage.emailtwoinput, writeremailtwo)
        self.activeweb.findElementByXpathAndAndFile(self.addmerchantpage.photofullfacebustimage, writerphotofullfacebust)

        self.activeweb.findElementByXpathAndAndFile(self.addmerchantpage.locationphotoimage, writerlocationphoto)
        self.activeweb.findElementByXpathAndAndFile(self.addmerchantpage.photoofthecashiersdeskimage, writerphotoofthecashiersdesk)
        self.activeweb.findElementByXpathAndAndFile(self.addmerchantpage.otherphotoimage, writerotherphoto)

        self.activeweb.findElementByXpathAndReturnOptions(self.addmerchantpage.bankselect, writerbank)
        self.activeweb.findElementByXpathAndInput(self.addmerchantpage.accountnameinput, writeraccountname)
        self.activeweb.findElementByXpathAndInput(self.addmerchantpage.accountnumberinput, writeraccountnumber)

        self.activeweb.findElementByXpathAndInput(self.addmerchantpage.qrindoamountinput, self.writerqrindoamount)
        self.activeweb.findElementByXpathAndClick(self.addmerchantpage.checkbutton)
        self.activeweb.delayTime(3)

        self.activeweb.findElementByXpathAndClick(self.addmerchantpage.submitbutton)
        self.activeweb.delayTime(3)
        self.activeweb.findElementByXpathAndClick(self.addmerchantdonepage.merchantlistbutton)

    # @unittest.skip('test_02')   #跳过用例名字为‘test_01’的用例，跳过的用例的执行结果显示：是
    def test_02(self):   #添加公司商户
        """
        添加页面元素
        :return:
        """
        self.addmerchantpage = self.addmerchantpagecompany
        writebrandname  = "123456"
        writeremail = "xiangkaizheng@iapppay.com"
        writercontactnumber = "abc123456"
        writermerchanttype = "Company"
        writercategory = "TAXICABS & LIMOUSINES"
        writercriteria = "Medium"
        writersiup = "abc123456"
        writerprovince = "JAMBI"
        writercity = "Kab. Bungo"
        writerdistrict = "abc123456"
        writervillage = "abc123456"
        writerpostcode = "abc123456"
        writeraddress = "abc123456"
        writercompany = "abc123456"
        writernpwptaxid = "abc123456"
        writerofficialwebsite = "abc123456"
        writerphotosiup = "D:\\pic\\1.png"
        writerphotonpwpcompany = "D:\\pic\\1.png"
        writerphototdp = "D:\\pic\\1.png"

        writername = "abc123456"
        writerposition = "abc123456"
        writerphone = "abc123456"
        writeremailtwo = "xiangkaizheng@iapppay.com"
        writerphotofullfacebust = "D:\\pic\\1.png"

        writerlocationphoto = "D:\\pic\\1.png"
        writerphotoofthecashiersdesk = "D:\\pic\\1.png"
        writerotherphoto = "D:\\pic\\1.png"

        writerbank = "BCA"
        writeraccountname = "abc123456"
        writeraccountnumber = "abc123456"


        self.activeweb.findElementByXpathAndInput(self.addmerchantpage.brandnameinput, writebrandname)
        self.activeweb.findElementByXpathAndInput(self.addmerchantpage.emailinput, writeremail)
        self.activeweb.findElementByXpathAndInput(self.addmerchantpage.contactnumberinput, writercontactnumber)
        self.activeweb.findElementByXpathAndReturnOptions(self.addmerchantpage.merchanttypeselect,writermerchanttype)
        self.activeweb.findElementByXpathAndReturnOptions(self.addmerchantpage.categoryselect, writercategory)
        self.activeweb.findElementByXpathAndReturnOptions(self.addmerchantpage.criteriaselect, writercriteria)
        self.activeweb.findElementByXpathAndInput(self.addmerchantpage.siupinput, writersiup)
        self.activeweb.findElementByXpathAndReturnOptions(self.addmerchantpage.provinceselect, writerprovince)
        self.activeweb.findElementByXpathAndReturnOptions(self.addmerchantpage.cityselect, writercity)
        self.activeweb.findElementByXpathAndInput(self.addmerchantpage.districtinput, writerdistrict)
        self.activeweb.findElementByXpathAndInput(self.addmerchantpage.villageinput, writervillage)
        self.activeweb.findElementByXpathAndInput(self.addmerchantpage.postcodeinput, writerpostcode)
        self.activeweb.findElementByXpathAndInput(self.addmerchantpage.addressinput, writeraddress)

        self.activeweb.findElementByXpathAndInput(self.addmerchantpage.companyinput, writercompany)
        self.activeweb.findElementByXpathAndInput(self.addmerchantpage.officialwebsiteinput, writerofficialwebsite)
        self.activeweb.findElementByXpathAndInput(self.addmerchantpage.npwptaxidinput, writernpwptaxid)

        self.activeweb.findElementByXpathAndAndFile(self.addmerchantpage.photosiupimage, writerphotosiup)
        self.activeweb.findElementByXpathAndAndFile(self.addmerchantpage.photonpwpcompanyimage, writerphotonpwpcompany)
        self.activeweb.findElementByXpathAndAndFile(self.addmerchantpage.phototdpimage, writerphototdp)

        self.activeweb.findElementByXpathAndInput(self.addmerchantpage.nameinput, writername)
        self.activeweb.findElementByXpathAndInput(self.addmerchantpage.positioninput, writerposition)
        self.activeweb.findElementByXpathAndInput(self.addmerchantpage.phoneinput, writerphone)
        self.activeweb.findElementByXpathAndInput(self.addmerchantpage.emailtwoinput, writeremailtwo)
        self.activeweb.findElementByXpathAndAndFile(self.addmerchantpage.photofullfacebustimage, writerphotofullfacebust)

        self.activeweb.findElementByXpathAndAndFile(self.addmerchantpage.locationphotoimage, writerlocationphoto)
        self.activeweb.findElementByXpathAndAndFile(self.addmerchantpage.photoofthecashiersdeskimage, writerphotoofthecashiersdesk)
        self.activeweb.findElementByXpathAndAndFile(self.addmerchantpage.otherphotoimage, writerotherphoto)

        self.activeweb.findElementByXpathAndReturnOptions(self.addmerchantpage.bankselect, writerbank)
        self.activeweb.findElementByXpathAndInput(self.addmerchantpage.accountnameinput, writeraccountname)
        self.activeweb.findElementByXpathAndInput(self.addmerchantpage.accountnumberinput, writeraccountnumber)

        self.activeweb.findElementByXpathAndClick(self.addmerchantpage.submitbutton)
        self.activeweb.delayTime(3)
        self.activeweb.findElementByXpathAndClick(self.addmerchantdonepage.merchantlistbutton)









# if __name__ == '__main__':
#     # # unittest.main()
#     # #使用HTMLTestRunner跑
#     # filepath = "./report/htmlreport.html"   #放置报告的路径
#     # fp = open(filepath,'wb')   #资源流,以读写的方式打开 file用open替代即可
#     # suite = unittest.TestSuite()  #创建一个用例容器
#     # suite.addTest(TestLoginPage('test_05'))
#     # runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='this is a report',description='report description')   #设置报告的标题和描述
#     # runner.run(suite)  #执行用例集suite



