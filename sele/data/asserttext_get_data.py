# _*_ coding:utf-8 _*_

__author__ = 'bobby'
__date__ = '2018/7/13 17:48'

from util.operation_excel import OperationExcel   #导入OperationExcel
from data.asserttext_data_config import *      #导入


class GetData:
    def __init__(self,file_name=None,sheet_id=None):
        self.file_name = file_name
        self.sheet_id = sheet_id
        self.opera_excel = OperationExcel(self.file_name,self.sheet_id)   #实例化


    #去获取excel行数，就是我们的case个数
    def get_case_lines(self):
        return self.opera_excel.get_lines()

    #获取是否加入cookie
    def get_cookie(self,row):
        col = int(get_cookie())  #获取cookie所在的列数
        url = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return url

    # 获取url
    def get_url(self,row):
        col = int(get_url())  #获取url所在的列数
        url = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return url

    #获取testxpath
    def get_testxpath(self,row):
        col = int(get_testxpath())  #获取testxpath所在的列数
        testxpath = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return testxpath

    #获取preresult
    def get_preresult(self,row):
        col = int(get_preresult())  #获取preresult所在的列数
        preresult = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return preresult

    #写入testresult
    def write_testresult(self,row,value):
        col = int(get_testresult())  #获取testresult所在的列数
        self.opera_excel.write_value(row,col,value)   #向指定的单元格写入内容

    #写入testdescription
    def write_testdescription(self,row,value):
        col = int(get_testdescription())  #获取testdescription所在的列数
        self.opera_excel.write_value(row,col,value)   #向指定的单元格写入内容

    #判断是否加入cookie
    def is_cookie(self,row):
        cookie = self.get_cookie(row)
        if cookie == 'yes':
            return True
        else:
            return False


if __name__ == '__main__':

    getdata = GetData()   #实例化
    print('---------------------------')
    rows_count = getdata.get_case_lines()
    for i in range(1, rows_count):  # 循环，但去掉第一个
        url = getdata.get_url(i)
        print(url)



