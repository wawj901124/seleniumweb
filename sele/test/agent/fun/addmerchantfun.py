# _*_ coding:utf-8 _*_

__author__ = 'bobby'
__date__ = '2018/7/27 12:24'

from base.activebase import ActiveWeb   #导入ActiveWeb
from project.agent.loginpageagent import LoginPage   #导入LoginPage页
from project.agent.addmerchantpage import AddMerchantPage   #导入AddMerchantPage页
from project.agent.addmerchantpage import AddMerchantPageCompany   #导入AddMerchantPageCompany页
from project.agent.addmeichantpagedonepage import AddMerchantDonePage   #导入AddMerchantDonePage页

class AddMerchantFun:   #创建测试类
    def __init__(self,writebrandname=None,writeremail=None,writercontactnumber =None,writermerchanttype=None,
                 writercategory=None,writercriteria =None,writersiup=None,writerprovince=None,writercity=None,
                 writerdistrict=None,writervillage=None,writerpostcode =None,writeraddress =None,writercompany=None,
                 writernpwptaxid =None,writerofficialwebsite=None,writerphotosiup=None,writerphotonpwpcompany =None,
                 writerphototdp =None,writername =None,writertypeid =None,writeridentitynumber=None,writernpwp=None,
                 writeraddresstwo =None,writernationality =None,writerposition =None,writerphone =None,writeremailtwo=None,
                 writerphotofullfacebust=None,writerlocationphoto=None,writerphotoofthecashiersdesk=None,writerotherphoto=None,
                 writerbank=None,writeraccountname =None,writeraccountnumber=None,writerqrindoamount = None
                 ):
        self.activeweb = ActiveWeb()   #实例化
        self.loginpage = LoginPage()   #实例化
        self.addmerchantpage = AddMerchantPage() # 实例化
        self.addmerchantdonepage = AddMerchantDonePage()   #实例化
        self.addmerchantpagecompany = AddMerchantPageCompany()   #实例化

        #登录
        self.url = "https://bjw.halodigit.com:9090/nereus/agent/index"   #代理商后台
        self.account = "6281122336666"
        self.password = "abc123456"
        # self.url = "https://m-mbmpay.ahdipay.com/nereus/agent/index"  # 代理商后台
        # self.account = "6281285610481"   #现网
        # self.password = "abc123456"   #现网

        self.addmer = "/html/body/div[3]/div[1]/div/ul/li/ul/li/a[2]"

        #输入内容：
        if writebrandname == None:
            self.writebrandname  = ""
        else:
            self.writebrandname = writebrandname

        if writeremail == None:
            self.writeremail = ""
        else:
            self.writeremail = writeremail

        if writercontactnumber == None:
            self.writercontactnumber = ""
        else:
            self.writercontactnumber = writercontactnumber

        if writermerchanttype == None:
            self.writermerchanttype = ""
        else:
            self.writermerchanttype = writermerchanttype

        if writercategory == None:
            self.writercategory = ""
        else:
            self.writercategory = writercategory

        if writercriteria == None:
            self.writercriteria = ""
        else:
            self.writercriteria = writercriteria

        if writersiup == None:
            self.writersiup = ""
        else:
            self.writersiup = writersiup

        if writerprovince == None:
            self.writerprovince = ""
        else:
            self.writerprovince = writerprovince

        if writercity == None:
            self.writercity = ""
        else:
            self.writercity = writercity

        if writerdistrict == None:
            self.writerdistrict = ""
        else:
            self.writerdistrict = writerdistrict

        if writervillage == None:
            self.writervillage = ""
        else:
            self.writervillage = writervillage

        if writerpostcode == None:
            self.writerpostcode = ""
        else:
            self.writerpostcode = writerpostcode

        if writeraddress == None:
            self.writeraddress = ""
        else:
            self.writeraddress = writeraddress

        if writercompany == None:
            self.writercompany = ""
        else:
            self.writercompany = writercompany

        if writernpwptaxid == None:
            self.writernpwptaxid = ""
        else:
            self.writernpwptaxid = writernpwptaxid

        if writerofficialwebsite == None:
            self.writerofficialwebsite = ""
        else:
            self.writerofficialwebsite = writerofficialwebsite

        if writerphotosiup == None:
            self.writerphotosiup = ""
        else:
            self.writerphotosiup = writerphotosiup

        if writerphotonpwpcompany == None:
            self.writerphotonpwpcompany = ""
        else:
            self.writerphotonpwpcompany = writerphotonpwpcompany

        if writerphototdp == None:
            self.writerphototdp = ""
        else:
            self.writerphototdp = writerphototdp


        if writername == None:
            self.writername = ""
        else:
            self.writername = writername

        if writertypeid == None:
            self.writertypeid = ""
        else:
            self.writertypeid = writertypeid

        if writeridentitynumber == None:
            self.writeridentitynumber = ""
        else:
            self.writeridentitynumber = writeridentitynumber

        if writernpwp == None:
            self.writernpwp = ""
        else:
            self.writernpwp = writernpwp

        if writeraddresstwo == None:
            self.writeraddresstwo = ""
        else:
            self.writeraddresstwo = writeraddresstwo

        if writernationality == None:
            self.writernationality = ""
        else:
            self.writernationality = writernationality

        if writerposition == None:
            self.writerposition = ""
        else:
            self.writerposition = writerposition

        if writerphone == None:
            self.writerphone = ""
        else:
            self.writerphone = writerphone

        if writeremailtwo == None:
            self.writeremailtwo = ""
        else:
            self.writeremailtwo = writeremailtwo

        if writerphotofullfacebust == None:
            self.writerphotofullfacebust = ""
        else:
            self.writerphotofullfacebust = writerphotofullfacebust


        if writerlocationphoto == None:
            self.writerlocationphoto = ""
        else:
            self.writerlocationphoto = writerlocationphoto

        if writerphotoofthecashiersdesk == None:
            self.writerphotoofthecashiersdesk = ""
        else:
            self.writerphotoofthecashiersdesk = writerphotoofthecashiersdesk

        if writerotherphoto == None:
            self.writerotherphoto = ""
        else:
            self.writerotherphoto = writerotherphoto


        if writerbank == None:
            self.writerbank = ""
        else:
            self.writerbank = writerbank

        if writeraccountname == None:
            self.writeraccountname = ""
        else:
            self.writeraccountname = writeraccountname

        if writeraccountnumber == None:
            self.writeraccountnumber = ""
        else:
            self.writeraccountnumber = writeraccountnumber

        if writerqrindoamount == None:
            self.writerqrindoamount = ""
        else:
            self.writerqrindoamount = writerqrindoamount


    def closeweb(self):
        """
        关闭浏览器
        """
        self.activeweb.closeBrowse()

    def  loginweb(self):
        """
        登录
        """
        self.activeweb.getUrl(self.url)   #打开网址
        self.activeweb.findElementByXpathAndInput(self.loginpage.account, self.account)
        self.activeweb.findElementByXpathAndInput(self.loginpage.password, self.password)
        self.activeweb.findElementByXpathAndClick(self.loginpage.loginbutton)
        self.activeweb.delayTime(3)

    def clickAddMerchant(self):
        """
        点击“Add merchant”
        """
        self.activeweb.findElementByXpathAndClick(self.addmer)   #点击"Add merchant"
        self.activeweb.delayTime(3)

    def addIndividuMerchant(self):
        """
        添加个人商户
        """
        global flaggere

        self.activeweb.findElementByXpathAndReturnOptions(self.addmerchantpage.merchanttypeselect,self.writermerchanttype)
        self.activeweb.findElementByXpathAndInput(self.addmerchantpage.brandnameinput, self.writebrandname)
        self.activeweb.findElementByXpathAndInput(self.addmerchantpage.emailinput, self.writeremail)
        self.activeweb.findElementByXpathAndInput(self.addmerchantpage.contactnumberinput, self.writercontactnumber)
        self.activeweb.findElementByXpathAndReturnOptions(self.addmerchantpage.categoryselect, self.writercategory)
        self.activeweb.findElementByXpathAndReturnOptions(self.addmerchantpage.criteriaselect, self.writercriteria)
        self.activeweb.findElementByXpathAndInput(self.addmerchantpage.siupinput, self.writersiup)
        self.activeweb.findElementByXpathAndReturnOptions(self.addmerchantpage.provinceselect, self.writerprovince)
        self.activeweb.findElementByXpathAndReturnOptions(self.addmerchantpage.cityselect, self.writercity)
        self.activeweb.findElementByXpathAndInput(self.addmerchantpage.districtinput, self.writerdistrict)
        self.activeweb.findElementByXpathAndInput(self.addmerchantpage.villageinput, self.writervillage)
        self.activeweb.findElementByXpathAndInput(self.addmerchantpage.postcodeinput, self.writerpostcode)
        self.activeweb.findElementByXpathAndInput(self.addmerchantpage.addressinput, self.writeraddress)
        self.activeweb.findElementByXpathAndAndFile(self.addmerchantpage.photosiupimage, self.writerphotosiup)
        self.activeweb.findElementByXpathAndAndFile(self.addmerchantpage.photonpwpcompanyimage, self.writerphotonpwpcompany)
        self.activeweb.findElementByXpathAndAndFile(self.addmerchantpage.phototdpimage, self.writerphototdp)

        self.activeweb.findElementByXpathAndInput(self.addmerchantpage.nameinput, self.writername)
        self.activeweb.findElementByXpathAndReturnOptions(self.addmerchantpage.typeidselect, self.writertypeid)
        self.activeweb.findElementByXpathAndInput(self.addmerchantpage.identitynumberinput, self.writeridentitynumber)
        self.activeweb.findElementByXpathAndInput(self.addmerchantpage.npwpinput, self.writernpwp)
        self.activeweb.findElementByXpathAndInput(self.addmerchantpage.addresstwoinput, self.writeraddresstwo)
        self.activeweb.findElementByXpathAndReturnOptions(self.addmerchantpage.nationalityselect, self.writernationality)
        self.activeweb.findElementByXpathAndInput(self.addmerchantpage.phoneinput, self.writerphone)
        self.activeweb.findElementByXpathAndInput(self.addmerchantpage.emailtwoinput, self.writeremailtwo)
        self.activeweb.findElementByXpathAndAndFile(self.addmerchantpage.photofullfacebustimage, self.writerphotofullfacebust)

        self.activeweb.findElementByXpathAndAndFile(self.addmerchantpage.locationphotoimage, self.writerlocationphoto)
        self.activeweb.findElementByXpathAndAndFile(self.addmerchantpage.photoofthecashiersdeskimage, self.writerphotoofthecashiersdesk)
        self.activeweb.findElementByXpathAndAndFile(self.addmerchantpage.otherphotoimage, self.writerotherphoto)

        self.activeweb.findElementByXpathAndReturnOptions(self.addmerchantpage.bankselect, self.writerbank)
        self.activeweb.findElementByXpathAndInput(self.addmerchantpage.accountnameinput, self.writeraccountname)
        self.activeweb.findElementByXpathAndInput(self.addmerchantpage.accountnumberinput, self.writeraccountnumber)

        self.activeweb.findElementByXpathAndInput(self.addmerchantpage.qrindoamountinput, self.writerqrindoamount)
        self.activeweb.findElementByXpathAndClick(self.addmerchantpage.checkbutton)
        self.activeweb.delayTime(3)

        self.activeweb.findElementByXpathAndClick(self.addmerchantpage.submitbutton)
        self.activeweb.delayTime(3)

        if self.activeweb.findElementByXpathAndReturnText(self.addmerchantdonepage.merchantnamecontent) == self.writebrandname :
            flaggere = True
            self.activeweb.printgreenword()
            print("添加个人商户%s成功" % self.writebrandname)
            self.activeweb.printnormalword()
        else:
            flaggere= False
            self.activeweb.printredword()
            print("添加个人商户%s失败" % self.writebrandname)
            self.activeweb.printnormalword()
        self.activeweb.findElementByXpathAndClick(self.addmerchantdonepage.merchantlistbutton)
        return flaggere

    def addCompanyMerchant(self):
        """
        添加公司商户
        """
        global flagcom
        self.addmerchantpage = self.addmerchantpagecompany


        self.activeweb.findElementByXpathAndReturnOptions(self.addmerchantpage.merchanttypeselect,self.writermerchanttype)
        self.activeweb.findElementByXpathAndInput(self.addmerchantpage.brandnameinput, self.writebrandname)
        self.activeweb.findElementByXpathAndInput(self.addmerchantpage.emailinput, self.writeremail)
        self.activeweb.findElementByXpathAndInput(self.addmerchantpage.contactnumberinput, self.writercontactnumber)
        self.activeweb.findElementByXpathAndReturnOptions(self.addmerchantpage.categoryselect, self.writercategory)
        self.activeweb.findElementByXpathAndReturnOptions(self.addmerchantpage.criteriaselect, self.writercriteria)
        self.activeweb.findElementByXpathAndInput(self.addmerchantpage.siupinput, self.writersiup)
        self.activeweb.findElementByXpathAndReturnOptions(self.addmerchantpage.provinceselect, self.writerprovince)
        self.activeweb.findElementByXpathAndReturnOptions(self.addmerchantpage.cityselect, self.writercity)
        self.activeweb.findElementByXpathAndInput(self.addmerchantpage.districtinput, self.writerdistrict)
        self.activeweb.findElementByXpathAndInput(self.addmerchantpage.villageinput, self.writervillage)
        self.activeweb.findElementByXpathAndInput(self.addmerchantpage.postcodeinput, self.writerpostcode)
        self.activeweb.findElementByXpathAndInput(self.addmerchantpage.addressinput, self.writeraddress)

        self.activeweb.findElementByXpathAndInput(self.addmerchantpage.companyinput, self.writercompany)
        self.activeweb.findElementByXpathAndInput(self.addmerchantpage.officialwebsiteinput, self.writerofficialwebsite)
        self.activeweb.findElementByXpathAndInput(self.addmerchantpage.npwptaxidinput, self.writernpwptaxid)

        self.activeweb.findElementByXpathAndAndFile(self.addmerchantpage.photosiupimage, self.writerphotosiup)
        self.activeweb.findElementByXpathAndAndFile(self.addmerchantpage.photonpwpcompanyimage, self.writerphotonpwpcompany)
        self.activeweb.findElementByXpathAndAndFile(self.addmerchantpage.phototdpimage, self.writerphototdp)

        self.activeweb.findElementByXpathAndInput(self.addmerchantpage.nameinput, self.writername)
        self.activeweb.findElementByXpathAndInput(self.addmerchantpage.positioninput, self.writerposition)
        self.activeweb.findElementByXpathAndInput(self.addmerchantpage.phoneinput, self.writerphone)
        self.activeweb.findElementByXpathAndInput(self.addmerchantpage.emailtwoinput, self.writeremailtwo)
        self.activeweb.findElementByXpathAndAndFile(self.addmerchantpage.photofullfacebustimage, self.writerphotofullfacebust)

        self.activeweb.findElementByXpathAndAndFile(self.addmerchantpage.locationphotoimage, self.writerlocationphoto)
        self.activeweb.findElementByXpathAndAndFile(self.addmerchantpage.photoofthecashiersdeskimage, self.writerphotoofthecashiersdesk)
        self.activeweb.findElementByXpathAndAndFile(self.addmerchantpage.otherphotoimage, self.writerotherphoto)

        self.activeweb.findElementByXpathAndReturnOptions(self.addmerchantpage.bankselect, self.writerbank)
        self.activeweb.findElementByXpathAndInput(self.addmerchantpage.accountnameinput, self.writeraccountname)
        self.activeweb.findElementByXpathAndInput(self.addmerchantpage.accountnumberinput, self.writeraccountnumber)

        self.activeweb.findElementByXpathAndInput(self.addmerchantpage.qrindoamountinput, self.writerqrindoamount)
        self.activeweb.findElementByXpathAndClick(self.addmerchantpage.checkbutton)
        self.activeweb.delayTime(3)

        self.activeweb.findElementByXpathAndClick(self.addmerchantpage.submitbutton)
        self.activeweb.delayTime(3)

        if self.activeweb.findElementByXpathAndReturnText(self.addmerchantdonepage.merchantnamecontent) == self.writebrandname :
            flagcom = True
            self.activeweb.printgreenword()
            print("添加公司商户%s成功"% self.writebrandname)
            self.activeweb.printnormalword()
        else:
            flagcom = False
            self.activeweb.printredword()
            print("添加公司商户%s失败" % self.writebrandname)
            self.activeweb.printnormalword()
        self.activeweb.findElementByXpathAndClick(self.addmerchantdonepage.merchantlistbutton)
        return flagcom


    def addMerchant(self):
        """
        添加商户
        """
        global flagadd
        if self.writermerchanttype == "Individu":
            self.loginweb()
            self.clickAddMerchant()
            flagadd = self.addIndividuMerchant()
        elif self.writermerchanttype == "Company":
            self.loginweb()
            self.clickAddMerchant()
            flagadd = self.addCompanyMerchant()
        else:
            print('商户类型不正确，商户类型只有：Individu和Company两种，你输入的商户类型为:%s' % self.writermerchanttype)
            flagadd = False
        self.closeweb()
        return flagadd




if __name__ == '__main__':
    addmerchant = AddMerchantFun()   #实例化
    addmerchant.addMerchant()



