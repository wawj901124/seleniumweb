# _*_ coding:utf-8 _*_

__author__ = 'bobby'
__date__ = '2018/7/13 17:48'

from util.operation_excel import OperationExcel   #导入OperationExcel
from data.assertselectsearch_data_config import *      #导入


class GetData:
    def __init__(self,file_name=None,sheet_id=None):
        self.file_name = file_name
        self.sheet_id = sheet_id
        self.opera_excel = OperationExcel(self.file_name,self.sheet_id)   #实例化


    #去获取excel行数，就是我们的case个数
    def get_case_lines(self):
        return self.opera_excel.get_lines()

    # 获取id
    def get_id(self,row):
        col = int(get_id())  #获取id所在的列数
        id = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return id

    # 获取title
    def get_title(self,row):
        col = int(get_title())  #获取id所在的列数
        title = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return title

    #获取是否加入cookie
    def get_cookie(self,row):
        col = int(get_cookie())  #获取cookie所在的列数
        url = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return url

    # 获取url
    def get_url(self,row):
        col = int(get_url())  #获取url所在的列数
        url = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        print("获取到的url:%s"% url)
        return url

    #获取selectxpath
    def get_selectxpath(self,row):
        col = int(get_selectxpath())  #获取testxpath所在的列数
        selectxpath = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        if selectxpath == '':
            return None
        else:
            return selectxpath

    #获取selectoptiontext
    def get_selectoptiontext(self,row):
        col = int(get_selectoptiontext())  #获取testxpath所在的列数
        selectoptiontext = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        if selectoptiontext == '':
            return None
        else:
            return selectoptiontext

    #获取selectinputxpath
    def get_selectinputxpath(self,row):
        col = int(get_selectinputxpath())  #获取testxpath所在的列数
        selectinputxpath = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        if selectinputxpath == ' ':
            return None
        else:
            return selectinputxpath


    #获取selectinputtext
    def get_selectinputtext(self,row):
        col = int(get_selectinputtext())  #获取testxpath所在的列数
        selectinputtext = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        if selectinputtext == '':
            return None
        else:
            return selectinputtext

    #获取searchbuttonxpath
    def get_searchbuttonxpath(self,row):
        col = int(get_searchbuttonxpath())  #获取testxpath所在的列数
        searchbuttonxpath = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return searchbuttonxpath

    #获取searchtableresultxpath
    def get_searchtableresultxpath(self,row):
        col = int(get_searchtableresultxpath())  #获取testxpath所在的列数
        searchtableresultxpath = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return searchtableresultxpath

    #获取colnum
    def get_colnum(self,row):
        col = int(get_colnum())  #获取testxpath所在的列数
        colnum = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return colnum

    #获取checktext
    def get_checktext(self,row):
        col = int(get_checktext())  #获取testxpath所在的列数
        checktext = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return checktext

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



