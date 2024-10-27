import threading
import urllib.request

def file_download(url,filename):
    urllib.request.urlretrieve(url,filename)

file_download('https://github.com/hanshu5252/Learning-C-Programming/blob/master/chapter%206%20pointers/1.c',"test.txt")

url_list =['https://github.com/hanshu5252/Learning-C-Programming/blob/master/chapter%206%20pointers/1.c','https://github.com/hanshu5252/Learning-C-Programming/blob/master/chapter%206%20pointers/1.c','https://github.com/hanshu5252/Learning-C-Programming/blob/master/chapter%206%20pointers/1.c']
file_name_list = ["data1.txt","data2.txt","data3.txt"]

ther = [threading.Thread(target=file_download, args=(url_list[i],file_name_list[i],)) for i in range (len(url_list)) ]
print(ther)
for t in ther:
    t.start()