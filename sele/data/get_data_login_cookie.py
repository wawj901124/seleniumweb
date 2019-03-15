# _*_ coding:utf-8 _*_

__author__ = 'bobby'
__date__ = '2018/7/13 17:48'

from util.operation_excel import OperationExcel   #导入OperationExcel
from data.data_config_login_cookie import *      #导入


class GetData:
    def __init__(self,file_name=None,sheet_id=None):
        self.file_name = file_name
        self.sheet_id = sheet_id
        self.opera_excel = OperationExcel(self.file_name,self.sheet_id)   #实例化
        self.global_var = GlobalVar()   #实例化

    #去获取excel行数，就是我们的case个数
    def get_case_lines(self):
        return self.opera_excel.get_lines()

    # 获取id单元格内的内容
    def get_id_content(self,row):
        col = int(self.global_var.id)  #获取id所在的列数
        id_content = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        if id_content == '':
            return None
        else:
            return id_content

    #获取title单元格内的内容
    def get_title_content(self,row):
        col = int(self.global_var.title)  #获取title所在的列数
        title_content = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        if title_content == '':
            return None
        else:
            return title_content

    #获取out_json_file单元格内的内容
    def get_out_json_file_content(self,row):
        col = int(self.global_var.out_json_file)  #获取out_json_file所在的列数
        out_json_file_content = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        if out_json_file_content == '':
            return None
        else:
            return out_json_file_content

    #获取out_login_url单元格内的内容
    def get_out_login_url_content(self,row):
        col = int(self.global_var.out_login_url)  #获取out_login_url所在的列数
        out_login_url_content = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        if out_login_url_content == '':
            return None
        else:
            return out_login_url_content

    #获取out_login_account_xpath单元格内的内容
    def get_out_login_account_xpath_content(self,row):
        col = int(self.global_var.out_login_account_xpath)  #获取out_login_account所在的列数
        out_login_account_xpath_content = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        if out_login_account_xpath_content == '':
            return None
        else:
            return out_login_account_xpath_content

    #获取out_login_account_text单元格内的内容
    def get_out_login_account_text_content(self,row):
        col = int(self.global_var.out_login_account_text)  #获取out_login_account_text所在的列数
        out_login_account_text_content = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        if out_login_account_text_content == '':
            return None
        else:
            return out_login_account_text_content

    #获取out_login_password_xpath单元格内的内容
    def get_out_login_password_xpath_content(self,row):
        col = int(self.global_var.out_login_password_xpath)  #获取out_login_password_xpath所在的列数
        out_login_password_xpath_content = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        if out_login_password_xpath_content == '':
            return None
        else:
            return out_login_password_xpath_content

    #获取out_login_password_text单元格内的内容
    def get_out_login_password_text_content(self,row):
        col = int(self.global_var.out_login_password_text)  #获取out_login_password_text所在的列数
        out_login_password_text_content = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        if out_login_password_text_content == '':
            return None
        else:
            return out_login_password_text_content

    #获取out_login_button_xpath单元格内的内容
    def get_out_login_button_xpath_content(self,row):
        col = int(self.global_var.out_login_button_xpath)  #获取out_login_button_xpath所在的列数
        out_login_button_xpath_content = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        if out_login_button_xpath_content == '':
            return None
        else:
            return out_login_button_xpath_content


    #写入test_result
    def write_test_result(self,row,value):
        col = int(self.global_var.test_result)  #获取test_result所在的列数
        self.opera_excel.write_value(row,col,value)   #向指定的单元格写入内容

    #写入test_description
    def write_test_description(self,row,value):
        col = int(self.global_var.test_description)  #获取test_description所在的列数
        self.opera_excel.write_value(row,col,value)   #向指定的单元格写入内容


if __name__ == '__main__':

    getdata = GetData()   #实例化
    print('---------------------------')
    rows_count = getdata.get_case_lines()
    for i in range(1, rows_count):  # 循环，但去掉第一个
        url = getdata.get_id_content(i)
        print(url)