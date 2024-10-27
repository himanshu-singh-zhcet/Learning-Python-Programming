import time
import threading
def test1(id):
    for i in range(10):
        print("test %d is printing %d %s"%(id,i,time.ctime()))
        time.sleep(1)

thread = [threading.Thread(target=test1,args=(i,)) for i in range (3)]
for t in thread:
    t.start()