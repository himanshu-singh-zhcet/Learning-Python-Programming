f = open("test.txt",'w')  # w mode mai n pahle wala data udd jayega
f.write("this is my first file to write")
f.close()

f = open("test.txt",'a')  # a mode maim pahle waale data ko truncate na kare 
f.write("this is second time i m writng ")
f.close()

f = open("test.txt",'r')
print(f.read())
f.close()

data1 = open("test.txt",'r')
for i in data1:
    print(i)

import os
a=os.path.getsize("test.txt")   # ye file ka size return krta hai
print(a)

import shutil
shutil.copy("test.txt","test_copy.txt")   # ye file ki copy kr dega 

with open("test.txt","r") as f:
    print(f.read())