import multiprocessing
from multiprocessing import Pool
import time


from main.run_all_test import RunAllTest
from util.getcookie import GetCookie

class GetCookieSleep:
    def getcookiesleep(self):
        while True:
            try:
                print("线程获取cookie启动")
                getcookie = GetCookie() #实例化
                getcookie.writerCookieToJson()
                print("线程获取cookie结束")
                time.sleep(30)
                print("等待30秒")
            except Exception as e:
                print("出现异常,异常原因：%s" % e)
            finally:
                True



runalltest = RunAllTest()
getcookie = GetCookie()
gcs = GetCookieSleep()

if __name__ == '__main__':
    starttime = time.time()
    print("开始时间：%s" % starttime)
    runalltest = RunAllTest()
    getcookie = GetCookie()
    gcs = GetCookieSleep()
    gcs.getcookiesleep()

    # p1 = multiprocessing.Process(target=runalltest.run())
    # p2 = multiprocessing.Process(target=gcs.getcookiesleep())
    #
    # p1.start()
    # p2.start()
    #
    # p1.join()
    # p2.join()

    pool = multiprocessing.Pool(2)
    pool.apply_async(runalltest.run())
    pool.apply_async(gcs.getcookiesleep())

    endtime = time.time()
    print("结束时间：%s" % endtime)
    print(str(round(endtime - starttime, 3)) + 's')



