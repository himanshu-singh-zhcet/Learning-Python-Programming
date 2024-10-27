import threading
import time
shared_var =0
lock_var = threading.Lock()

def test2(id):
    global shared_var    # mtlb ek core ke andr jitne bhi thread chl rhe hai wo sb access kr paaye
    with lock_var:
        shared_var =shared_var+1
        print("test 2 id is %d has increased the shared variable by %d" %(id,shared_var))
        # time.sleep(1)
        

thread = [threading.Thread(target=test2,args=(i,)) for i in range (3)]
print(thread)
for t in thread:
    t.start()