import unittest
from data.assertselectsearch_get_data import GetData   #导入GetData
from util.send_attach_email import SendEmail
from base.datailfunction import WebFunction
from base.activebase import ActiveWeb

class TestSearch(unittest.TestCase):  # 创建测试类

    @classmethod  # 类方法，只执行一次，但必须要加注解@classmethod,且名字固定为setUpClass
    def setUpClass(cls):
        pass

    @classmethod  # 类方法，只执行一次，但必须要加注解@classmethod,且名字固定为tearDownClass
    def tearDownClass(cls):
        pass

    def setUp(self):  # 每条用例执行测试之前都要执行此方法
        self.cookie = self.getcookie()
        self.activeweb = ActiveWeb()  # 实例化
        self.loginurl = "https://bjw.halodigit.com:9090/nereus/manager/index#/login"
        # self.loginaccountxpath = "/html/body/div[1]/div[2]/form/div/div[1]/input"
        # self.loginaccount = "admin@iapppay.com"
        # self.loginppasswordxpath = "/html/body/div[1]/div[2]/form/div/div[2]/input"
        # self.loginpassword = "123456"
        # self.loginbuttonxpath = "/html/body/div[1]/div[2]/form/div/a[1]/span"


        #pass


    def tearDown(self):  # 每条用例执行测试之后都要执行此方法
        self.activeweb.closeBrowse()

        # pass

    #获取cookie
    def getcookie(self):
        # 登录
        self.activeweb = ActiveWeb()  # 实例化
        self.loginurl = "https://bjw.halodigit.com:9090/nereus/manager/index#/login"
        self.loginaccountxpath = "/html/body/div[1]/div[2]/form/div/div[1]/input"
        self.loginaccount = "admin@iapppay.com"
        self.loginppasswordxpath = "/html/body/div[1]/div[2]/form/div/div[2]/input"
        self.loginpassword = "123456"
        self.loginbuttonxpath = "/html/body/div[1]/div[2]/form/div/a[1]/span"

        self.activeweb.getUrl(self.loginurl)  # 打开网址
        self.activeweb.findElementByXpathAndInput(self.loginaccountxpath,self.loginaccount)
        self.activeweb.findElementByXpathAndInput(self.loginppasswordxpath,self.loginpassword)
        self.activeweb.findElementByXpathAndClick(self.loginbuttonxpath)
        self.activeweb.delayTime(3)
        # 获取cookie
        cookie = self.activeweb.getCookies()
        self.activeweb.closeBrowse()
        return cookie

    #定义搜索查找函数
    def definesearch(self,num,is_cookie,url,selectxpath,selectoptiontext,selectinputxpath,selectinputtext,searchbuttonxpath,searchtableresultxpath,colnum,checktext):

        if is_cookie:
            self.activeweb.writerCookies(self.cookie, self.loginurl,url)
        else:
            self.activeweb.getUrl(url)

        self.activeweb.findElementByXpathAndReturnOptions(selectxpath,str(selectoptiontext))
        if selectinputxpath ==None:
            print("不执行输入文本内容")
        else:
            self.activeweb.findElementByXpathAndInput(selectinputxpath,str(selectinputtext))
        self.activeweb.findElementByXpathAndClick(searchbuttonxpath)
        self.activeweb.delayTime(5)
        tabledic = self.activeweb.findElementByXpathAndReturnTableNum(num,searchtableresultxpath)
        for value in tabledic.values():
            if str(checktext).lower() in value[int(colnum)].lower():
                self.assertTrue(True)
            else:
                self.assertTrue(False)




    @staticmethod    #根据不同的参数生成测试用例
    def getTestFunc(num,is_cookie,url,selectxpath,selectoptiontext,selectinputxpath,selectinputtext,searchbuttonxpath,searchtableresultxpath,colnum,checktext):
        def func(self):
            self.definesearch(num,is_cookie,url,selectxpath,selectoptiontext,selectinputxpath,selectinputtext,searchbuttonxpath,searchtableresultxpath,colnum,checktext)
        return func


def __generateTestCases():
    file_name = "D:\\Users\\Administrator\\PycharmProjects\\seleniumweb\\sele\\dataconfig\\assertselectsearchmanager.xls"
    sheet_id = 0
    datasheet = GetData(file_name,sheet_id)   #实例化
    rows_count = datasheet.get_case_lines()   #获取表的行数
    for i in range(1, rows_count):  # 循环，但去掉第一
        args = []
        args.append(i)
        args.append(datasheet.is_cookie(i))
        args.append(datasheet.get_url(i))
        args.append(datasheet.get_selectxpath(i))
        args.append(datasheet.get_selectoptiontext(i))
        args.append(datasheet.get_selectinputxpath(i))
        args.append(datasheet.get_selectinputtext(i))
        args.append(datasheet.get_searchbuttonxpath(i))
        args.append(datasheet.get_searchtableresultxpath(i))
        args.append(datasheet.get_colnum(i))
        args.append(datasheet.get_checktext(i))


        setattr(TestSearch, 'test_func_%s_%s' % (datasheet.get_id(i),datasheet.get_title(i)),
                TestSearch.getTestFunc(*args))  # 通过setattr自动为TestCase类添加成员方法，方法以“test_func_”开头


__generateTestCases()

if __name__ == '__main__':
    print("hello world")
    unittest.main()










