import threading
from time import ctime, sleep


from main.run_all_test import RunAllTest
from util.getcookie import GetCookie

class GetCookieSleep:
    def getcookiesleep(self):
        self.getcookie = GetCookie
        getcookie.writerCookieToJson()
        print("线程获取cookie启动")


runalltest = RunAllTest()
getcookie = GetCookie()
gcs = GetCookieSleep()

threads = []

t1 = threading.Thread(target=gcs.getcookiesleep())
threads.append(t1)

t2 = threading.Thread(target=runalltest.run())
threads.append(t2)





if __name__ == '__main__':
    for t in threads:
        t.start()
    # for t in threads:
    #     t.join()

    print("all over %s" %ctime())


