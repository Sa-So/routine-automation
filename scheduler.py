import schedule
import time as t
import adb_oopsie as ao
from classes import * 

#time_s = ""
#time_s = input(" Enter time in hh:mm : ")
# def fun1():
#     a.unlock()
#     t.sleep(1)
#     a.google_()
## time table 
#schedule.every().thursday.at(time_s).do(fun1)

a = ao.android()
def funny(s):
    a.unlock()
    t.sleep(1)
    #fm cns da RTS
    a.google_(url=s)
    
#funny(DA);

#if(t.asctime().find('Tue')!=-1):
schedule.every().monday.at("10:07").do(funny,RTS)
schedule.every().monday.at("11:05").do(funny,CNS)
schedule.every().monday.at("12:05").do(funny,CC)

schedule.every().tuesday.at("09:05").do(funny,FM)
schedule.every().tuesday.at("10:05").do(funny,CNS)
schedule.every().tuesday.at("11:05").do(funny,DA)
schedule.every().tuesday.at("12:05").do(funny,RTS)

schedule.every().wednesday.at("09:05").do(funny,OB)
schedule.every().wednesday.at("10:05").do(funny,CNS)
schedule.every().wednesday.at("11:05").do(funny,CC)
schedule.every().wednesday.at("12:05").do(funny,FM)
#schedule.every().friday().at('4:06').do()

#FM DA CC from 10
schedule.every().thursday.at("10:05").do(funny,FM)
schedule.every().thursday.at("11:05").do(funny,DA)
schedule.every().thursday.at("12:05").do(funny,CC)


vary = ""
while vary != "12:05":
    schedule.run_pending()
    #print(t.gmtime(),t.asctime())
    var1 = t.asctime().split(':')
    var0 = var1[0][-2:]
    var2 = var1[1]
    #print(var0,var2)
    vary = var0 + ":"+var2
    print(vary)
    t.sleep(30)
