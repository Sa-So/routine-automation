import schedule
import time as t
import adb_oopsie as ao

a = ao.android()
def fun1():
    a.unlock()
    a.google_()
schedule.every().friday.at("04:05").do(fun1)
#schedule.every().friday().at('4:06').do()

while True:
    schedule.run_pending()
    t.sleep(1)