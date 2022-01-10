import shutil
import urllib.request as request
from contextlib import closing
#from clint.textui import progress   
import time

"""
initial=time.time()
r=closing(request.urlopen('ftp://ftp-test.telkomadsl.co.za/1Meg-test.file'))
after=time.time()
diff=after-initial
print(str(diff))
with open('text.txt', 'wb') as f:
        shutil.copyfileobj(r, f)

"""
def speedTest():
    ini=time.time_ns()
    with closing(request.urlopen('ftp://ftp-test.telkomadsl.co.za/8Meg-test.file')) as r:
        af=time.time_ns()
        dif=af-ini
        dif=dif/(10**9)
        #print(dif)
        #print("speed= "+str(8/dif))
        return 8/dif

if __name__ == "__main__":
        mylist=[]
        for i in range(10):
                mylist.append(speedTest()) 
        avgTime=sum(mylist)/len(mylist)
        avgSpeed=8/avgTime
        print(mylist)
        print("avg speed= "+str(avgSpeed))
    