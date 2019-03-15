import traceback

# 在jenkins运行时经常提示找不到包，所以就需要手动添加PYTHONPATH，通过追加sys.path列表来实现
import os
import sys

rootpath = str(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
syspath = sys.path
sys.path = []
sys.path.append(rootpath)  # 将工程根目录加入到python搜索路径中
sys.path.extend([rootpath + i for i in os.listdir(rootpath) if i[0] != "."])  # 将工程目录下的一级目录添加到python搜索路径中
sys.path.extend(syspath)
# 追加完成


from data.asserttext_get_data import GetData   #导入GetData
from util.send_attach_email import SendEmail
from base.datailfunction import WebFunction
from util.gettimestr import GetTimeStr   #导入获取时间串函数




class RunTest:
    def __init__(self):
        # self.addmerchantfun = AddMerchantFun()   #实例化
        # self.webfunction = WebFunction()   #实例化
        self.file_name = "../dataconfig/asserttextmerchant.xls"
        self.sheet_id = 0
        self.data = GetData(self.file_name,self.sheet_id)   #实例化
        self.send_mai = SendEmail() #实例化
        self.loginurl = "https://bjw.halodigit.com:9090/nereus/merchant/index#/login"
        self.loginaccountxpath = "/html/body/div[1]/div[4]/form/div/div[2]/div[1]/input"
        self.loginaccount = "6281122336666"
        self.loginppasswordxpath = "/html/body/div[1]/div[4]/form/div/div[2]/div[2]/input"
        self.loginpassword = "abc123456"
        self.loginbuttonxpath = "/html/body/div[1]/div[4]/form/div/div[2]/a/span"

    def getcookie(self):
        self.webfunction = WebFunction()  # 实例化
        # 登录
        self.webfunction.activeweb.getUrl(self.loginurl)  # 打开网址
        self.webfunction.activeweb.findElementByXpathAndInput(self.loginaccountxpath,self.loginaccount)
        self.webfunction.activeweb.findElementByXpathAndInput(self.loginppasswordxpath,self.loginpassword)
        self.webfunction.activeweb.findElementByXpathAndClick(self.loginbuttonxpath)
        self.webfunction.activeweb.delayTime(3)

        self.webfunction.activeweb.findElementByXpathAndScriptClick("/html/body/div[1]/div[2]/div/form/div[5]/p[1]/span/input")
        self.webfunction.activeweb.delayTime(3)
        self.webfunction.activeweb.findElementByXpathAndClick("/html/body/div[1]/div[2]/div/form/div[29]/p/span[2]/button/span")
        self.webfunction.activeweb.delayTime(3)



        # 获取cookie
        cookie = self.webfunction.activeweb.getCookies()
        self.webfunction.activeweb.closeBrowse()
        return cookie

    #程序执行
    def go_on_run(self):
        global cookie
        cookie = self.getcookie()

        res = None
        pass_count = []
        fail_count = []
        # global assertresult
        assertresult = [0,0]
        rows_count = self.data.get_case_lines()


        print("需要执行%d个用例:"%(rows_count-1))
        for i in range(1,rows_count):   #循环，但去掉第一个
            if i % 10 == 0:
                cookie = self.getcookie()

            try:
                print("\n执行第%d个用例\n"%i)
                url = self.data.get_url(i)
                testxpath = self.data.get_testxpath(i)
                preresult = self.data.get_preresult(i)
                self.webfunction = WebFunction()  # 实例化

                if self.data.is_cookie(i):
                    self.webfunction.activeweb.writerCookies(cookie,self.loginurl,url)
                else:
                    self.webfunction.activeweb.getUrl(url)

                assertresult = self.webfunction.assertText(i,testxpath, preresult)

            except Exception as e:
                print('\n异常现象打印：\n',e)
            finally:
                # print('第%d次循环执行完毕'%i)
                if assertresult[0] == 'pass':
                    self.data.write_testresult(i, 'pass')
                    pass_count.append(i+1)  # 通过的加到集合里
                    self.data.write_testdescription(i, str(assertresult[1]))
                else:
                    self.data.write_testresult(i, 'fail')
                    fail_count.append(i+1)  # 失败的加到集合里
                    self.data.write_testdescription(i, str(assertresult[1]))
                self.webfunction.activeweb.closeBrowse()
                assertresult = [0, 0]
            i = i + 1
        print("\n成功的行数：",pass_count)
        print("\n失败的行数：",fail_count)
        self.send_mai.send_main(pass_count, fail_count,self.file_name)  # 调用发送邮件


if __name__ == '__main__':
    run = RunTest()   #实例化
    print('---------------------------')
    # stdout_backup = sys.stdout
    # gettime = GetTimeStr()
    # timestr = gettime.getTimeStr()
    # logpath = "../log/%s_message.txt" % timestr
    # print("Now all print info will be written to log文件：",logpath)
    # # define the log file that receives your log info
    # log_file = open(logpath, "w",encoding="utf-8")
    # # redirect print output to log file
    # sys.stdout = log_file
    # print('----------开始打印日志-----------------\n')
    run.go_on_run()
    # print('\n----------日志打印结束-----------------')
    # log_file.close()
    # # restore the output to initial pattern
    # sys.stdout = stdout_backup
    # print("Now this will be presented on screen")
    #
    # #发送log至邮箱
    # send_e = SendEmail()
    # send_e.send_main([1],[2],logpath)