# _*_ coding:utf-8 _*_

__author__ = 'bobby'
__date__ = '2018/7/13 17:26'

class global_var:
    #测试数据
    cookie = '2'
    url = '3'
    testxpath = '4'
    preresult = '5'
    testresult = '6'
    testdescription = '7'

#获取cookie列数
def get_cookie():
    return global_var.cookie

#获取url列数
def get_url():
    return global_var.url

#获取testxpath列数
def get_testxpath():
    return global_var.testxpath

#获取preresult列数
def get_preresult():
    return global_var.preresult

#获取testresult列数
def get_testresult():
    return global_var.testresult

#获取testdescription列数
def get_testdescription():
    return global_var.testdescription
