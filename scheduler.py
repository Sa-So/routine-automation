import schedule
import time as t
import adb_oopsie as ao

#time_s = ""
time_s = input(" Enter time in hh:mm : ")

a = ao.android()
def fun1():
    a.unlock()
    t.sleep(1)
    a.google_()
schedule.every().friday.at(time_s).do(fun1)
#schedule.every().friday().at('4:06').do()

vary = ""
while vary != "09:05":
    schedule.run_pending()
    #print(t.gmtime(),t.asctime())
    var1 = t.asctime().split(':')
    var0 = var1[0][-2:]
    var2 = var1[1]
    #print(var0,var2)
    vary = var0 + ":"+var2
    print(vary)
    t.sleep(20)