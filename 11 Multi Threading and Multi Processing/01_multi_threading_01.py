# yhaa pr hum ek process ke andr multiple thread implement kr rhe  hai 
import threading
def test(id):
    print("program starts %d"% id)

thread = [threading.Thread(target=test,args=(i,)) for i in range (10)]
for t in thread:
    t.start()

print(thread)
print(id(thread))
