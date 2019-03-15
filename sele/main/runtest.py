# _*_ coding:utf-8 _*_

__author__ = 'bobby'
__date__ = '2018/8/7 10:16'

import traceback

from data.get_data import GetData   #导入GetData
from test.agent.fun.addmerchantfun import AddMerchantFun
from util.send_email import SendEmail


class RunTest:
    def __init__(self):
        # self.addmerchantfun = AddMerchantFun()   #实例化
        self.data = GetData()   #实例化
        self.send_mai = SendEmail() #实例化

    #程序执行
    def go_on_run(self):
        res = None
        pass_count = []
        fail_count = []
        global flag

        rows_count = self.data.get_case_lines()
        print("需要添加%d个商户"%(rows_count-1))
        for i in range(1,rows_count):   #循环，但去掉第一个

            try:
                print("添加第%d个商户"%i)
                self.writebrandname = self.data.get_brandname(i)
                self.writeremail = self.data.get_email(i)
                self.writercontactnumber = self.data.get_contactnumber(i)
                self.writermerchanttype = self.data.get_merchanttype(i)
                self.writercategory = self.data.get_category(i)
                self.writercriteria = self.data.get_criteria(i)
                self.writersiup = self.data.get_siup(i)
                self.writerprovince = self.data.get_province(i)
                self.writercity = self.data.get_city(i)
                self.writerdistrict = self.data.get_district(i)
                self.writervillage = self.data.get_village(i)
                self.writerpostcode = self.data.get_postcode(i)
                self.writeraddress = self.data.get_address(i)
                self.writercompany = self.data.get_company(i)
                self.writernpwptaxid = self.data.get_npwptaxid(i)
                self.writerofficialwebsite = self.data.get_officialwebsite(i)
                self.writerphotosiup = self.data.get_photosiup(i)
                self.writerphotonpwpcompany = self.data.get_photonpwpcompany(i)
                self.writerphototdp = self.data.get_phototdp(i)

                self.writername = self.data.get_name(i)
                self.writertypeid = self.data.get_typeid(i)
                self.writeridentitynumber = self.data.get_identitynumber(i)
                self.writernpwp = self.data.get_npwp(i)
                self.writeraddresstwo = self.data.get_addresstwo(i)
                self.writernationality = self.data.get_nationality(i)
                self.writerposition = self.data.get_position(i)
                self.writerphone = self.data.get_phone(i)
                self.writeremailtwo = self.data.get_emailtwo(i)
                self.writerphotofullfacebust = self.data.get_photofullfacebust(i)

                self.writerlocationphoto = self.data.get_locationphoto(i)
                self.writerphotoofthecashiersdesk = self.data.get_photoofthecashiersdesk(i)
                self.writerotherphoto = self.data.get_otherphoto(i)

                self.writerbank = self.data.get_bank(i)
                self.writeraccountname = self.data.get_accountname(i)
                self.writeraccountnumber = self.data.get_accountnumber(i)

                self.writerqrindoamount = self.data.get_qrindoamount(i)

                self.addmerchantfun = AddMerchantFun(self.writebrandname,self.writeremail ,self.writercontactnumber ,
                                                 self.writermerchanttype ,self.writercategory ,self.writercriteria ,
                                                 self.writersiup ,self.writerprovince ,self.writercity ,self.writerdistrict ,
                                                 self.writervillage,self.writerpostcode ,self.writeraddress ,self.writercompany ,
                                                 self.writernpwptaxid ,self.writerofficialwebsite ,self.writerphotosiup ,
                                                 self.writerphotonpwpcompany ,self.writerphototdp ,
                                                 self.writername,self.writertypeid ,self.writeridentitynumber ,self.writernpwp ,
                                                 self.writeraddresstwo ,self.writernationality ,self.writerposition ,self.writerphone ,
                                                 self.writeremailtwo ,self.writerphotofullfacebust ,self.writerlocationphoto ,
                                                 self.writerphotoofthecashiersdesk ,self.writerotherphoto ,
                                                 self.writerbank ,self.writeraccountname ,self.writeraccountnumber,
                                                 self.writerqrindoamount
                                                 )  # 实例化

                flag = False
                flagadd = self.addmerchantfun.addMerchant()
                # print("flagadd标志为",flagadd)
                if flagadd:
                    flag = True
            except Exception as e:
                self.addmerchantfun.activeweb.printredword()
                print('异常现象打印：',e)
                self.addmerchantfun.activeweb.printnormalword()
            finally:
                # print('第%d次循环执行完毕'%i)
                # print("flag标志：",flag)
                if flag:
                    pass_count.append(i+1)  # 通过的加到集合里
                else:
                    fail_count.append(i+1)  # 失败的加到集合里
                i = i + 1
        self.addmerchantfun.activeweb.printgreenword()
        print("添加成功的行数：",pass_count)
        self.addmerchantfun.activeweb.printredword()
        print("添加失败的行数：",fail_count)
        self.addmerchantfun.activeweb.printnormalword()
        self.send_mai.send_main(pass_count, fail_count)  # 调用发送邮件



if __name__ == '__main__':
    run = RunTest()   #实例化
    print('---------------------------')
    run.go_on_run()