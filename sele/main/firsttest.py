# _*_ coding:utf-8 _*_

__author__ = 'bobby'
__date__ = '2018/7/26 14:59'
import time   #导入时间
import os
import sys

rootpath = str(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
syspath = sys.path
sys.path = []
sys.path.append(rootpath)  # 将工程根目录加入到python搜索路径中
sys.path.extend([rootpath + i for i in os.listdir(rootpath) if i[0] != "."])  # 将工程目录下的一级目录添加到python搜索路径中
sys.path.extend(syspath)
# 追加完成


from selenium import webdriver   #导入驱动
from selenium.webdriver import ActionChains

# #通过executable_path指明Fiirefox驱动文件所在路径
# # firefoxdriver = webdriver.Firefox(executable_path="D:\\Users\\Administrator\\PycharmProjects\\seleniumweb\\sele\\driver")
# # firefoxdriver = webdriver.Firefox(executable_path="D:\\Users\\Administrator\\PycharmProjects\\seleniumweb\\sele\\driver")
#
# firefoxdriver = webdriver.Firefox()   #需要把驱动所在路径配置到系统环境变量里
# #googledriver =webdriver.Firefox(executable_path="D:\\Users\\Administrator\\PycharmProjects\\seleniumweb\\sele\\driver")
# driver = firefoxdriver
# #打开搜狗首页
# driver.get("http://www.sogou.com")
# #清除搜索输入框默认内容
# driver.find_element_by_id("query").clear()
# #在输入框中输入“光荣之路自动化测试”
# driver.find_element_by_id("query").send_keys("光荣之路自动化测试")
# #单击“搜索”按钮
# driver.find_element_by_id("stb").click()
# #等待3秒
# time.sleep(3)
# #退出浏览器
# # driver.quit()

class  ActiveWeb:
    def __init__(self):
        self.driver = self.getFirefoxDriver()


    #使用火狐浏览器
    def getFirefoxDriver(self):
        firefoxdriver = webdriver.Firefox()  # 需要把驱动所在路径配置到系统环境变量里
        # firefoxdriver = webdriver.Chrome() # 需要把驱动所在路径配置到系统环境变量里
        return  firefoxdriver

    #使用谷歌浏览器
    def getChromeDriver(self):
        chromedriver = webdriver.Chrome()  # 需要把驱动所在路径配置到系统环境变量里
        return  chromedriver

    #使用IE浏览器
    def getIeDriver(self):
        iedriver = webdriver.Ie()  # 需要把驱动所在路径配置到系统环境变量里
        return  iedriver

    #使用Edge浏览器
    def getEdgeDriver(self):
        edgedriver = webdriver.Edge()  # 需要把驱动所在路径配置到系统环境变量里
        return  edgedriver

    #使用Opera浏览器
    def getOperaDriver(self):
        operadriver = webdriver.Opera  # 需要把驱动所在路径配置到系统环境变量里
        return  operadriver

    #打开网址
    def Activefunction(self,url):
        self.driver.get(url)

    #通过xpath查找元素
    def findElementByXpath(self,path):
        return self.driver.find_element_by_xpath(path)

    #通过xpath查找元素，然后输入内容
    def findElementByXpathAndInput(self,path,inputcontent):
        ele = self.findElementByXpath(path)
        ele.clear()   #清除输入框内容
        ele.send_keys(inputcontent)   #输入内容

    #通过xpath查找元素，然后点击
    def findElementByXpathAndClick(self,path):
        ele = self.findElementByXpath(path)
        ele.click()   #点击

    #通过xpath查找元素，然后点击
    def findElementByXpathAndScriptClick(self,path):
        ele = self.findElementByXpath(path)
        self.driver.execute_script("arguments[0].click();", ele)
        return ele

    def select(self):
        js = "$('.TimeAvailable').medate({\
                   beginyear: new Date().getFullYear()+7,\
                beginmonth: 2,\
                yearTxt: '',\
                monthTxt: '',\
                cancelBtn: 'cancel',\
                confirmBtn: 'confirm',\
                datetitle: ''\
                }, function (data) {\
                   var realData = data.substr(2, 2) + data.substr(5, 2);\
                    $('.TimeAvailable').val(data).attr('data-real', realData);\
                    isActiveBtn();\
                });"
        self.driver.execute_script(js)

    #延迟3秒
    def delaytime(self,dalaytime):
        time.sleep(int(dalaytime))   #延迟，秒数

    #关闭浏览器
    def closebrowse(self):
        self.driver.quit()


if __name__ == "__main__":
    for i in range(1,2):
        activeweb = ActiveWeb() #实例化
        url = "https://bjw.halodigit.com:9090/bbc/v/bcv?sk=cardno&ppt=EQs9kPmUry0HzqwbQHOmWK65AYBbj1Qr&bt=HFJS-tfWYfOWFa6nMYLF7VMAAAAAAAAehiQAQChkZjIyODM5MzIyZGZjZWIwNjIyYjVjNmJlNTg3OWVkODUyZDU5NGQ1#"
        activeweb.Activefunction(url)
        activeweb.delaytime(3)
        activeweb.findElementByXpathAndInput("/html/body/div[3]/div[2]/div[1]/input","abc")   #输入账号名
        activeweb.delaytime(3)
        activeweb.findElementByXpathAndInput("/html/body/div[3]/div[2]/div[2]/input","6064200000009999")   #输入密码
        activeweb.delaytime(3)
        activeweb.findElementByXpathAndClick("/html/body/div[3]/div[4]/a")   #点击登录
        activeweb.delaytime(3)
        activeweb.findElementByXpathAndInput("/html/body/div[4]/div[2]/div[1]/input", "123")  # 输入账号名
        activeweb.delaytime(3)

        activeweb.select()
        activeweb.findElementByXpathAndClick("/html/body/div[4]/div[2]/div[2]/input")  # 输入账号名
        activeweb.delaytime(3)

        activeweb.findElementByXpathAndClick("/html/body/div[7]/div[2]/footer/div/ul/li")   #点击登录
        activeweb.delaytime(3)
        activeweb.findElementByXpathAndClick("/html/body/div[4]/div[3]/a")   #点击登录
        activeweb.delaytime(3)
        activeweb.findElementByXpathAndInput("/html/body/div[5]/div[2]/div/div/input", "123456")  # 输入账号名
        activeweb.delaytime(3)
        activeweb.findElementByXpathAndClick("/html/body/div[5]/div[3]/a")   #点击登录
        activeweb.delaytime(3)
        activeweb.closebrowse()
















