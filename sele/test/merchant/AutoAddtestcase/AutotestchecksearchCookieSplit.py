import unittest

from data.assertselectsearch_get_data import GetData   #导入GetData
from base.activebase import ActiveWeb
from util.operation_json import OperationJson
from util.getcookie import GetCookie


class TestSearch(unittest.TestCase):  # 创建测试类


    @classmethod  # 类方法，只执行一次，但必须要加注解@classmethod,且名字固定为setUpClass
    def setUpClass(cls):
        pass

    @classmethod  # 类方法，只执行一次，但必须要加注解@classmethod,且名字固定为tearDownClass
    def tearDownClass(cls):
        pass

    def setUp(self):  # 每条用例执行测试之前都要执行此方法
        self.jsonfile = '../dataconfig/cookiemerchant.json'
        self.operationjson = OperationJson(file_path=self.jsonfile)   #实例化
        self.cookie = self.operationjson.get_all_data()
        print("self.cookie:%s" % self.cookie)
        self.activeweb = ActiveWeb()  # 实例化
        self.loginurl = "https://bjw.halodigit.com:9090/nereus/merchant/index"
        #pass


    def tearDown(self):  # 每条用例执行测试之后都要执行此方法
        self.activeweb.closeBrowse()
        # pass

    #定义搜索查找函数
    def definesearch(self,num,is_cookie,url,selectxpath,selectoptiontext,selectinputxpath,selectinputtext,searchbuttonxpath,searchtableresultxpath,colnum,checktext):

        if is_cookie:
            self.activeweb.writerCookies(self.cookie, self.loginurl,url)
        else:
            self.activeweb.getUrl(url)

        self.activeweb.findElementByXpathAndReturnOptions(selectxpath,str(selectoptiontext))
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
    gc = GetCookie()
    gc.writerCookieToJson()
    for i in range(1, rows_count):  # 循环，
        # if i % 2 == 0:
        #     gc = GetCookie()
        #     gc.writerCookieToJson()
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










