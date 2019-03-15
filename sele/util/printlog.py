import sys

from util.gettimestr import GetTimeStr

class PrintLog:

    def printLog(self):
        stdout_backup = sys.stdout
        gettime = GetTimeStr()
        timestr = gettime.getTimeStr()
        # define the log file that receives your log info
        log_file = open("%s_message.log" % timestr , "w")
        # redirect print output to log file
        sys.stdout = log_file
        print("Now all print info will be written to message.log")
        # any command line that you will execute
            #执行的内容
        log_file.close()
        # restore the output to initial pattern
        sys.stdout = stdout_backup
        print("Now this will be presented on screen")