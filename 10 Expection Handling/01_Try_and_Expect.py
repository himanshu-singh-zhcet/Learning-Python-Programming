try:
    f = open("test.txt",'r')   #try and expect se ye hoga ki agr ye code crash ho gya to is as aage baala code bhi crash nhi karega wo shi chalega
except Exception as e:
    print("this is my expect block",e)



try:
    f = open("test1.txt",'w')
    f.write("i m writing in thos file")
    f.close()
except Exception as e:
    print("this is my expect block",e)
else:
    print("this will execute once when your try will execute without error")

try:
    f = open("test.txt",'r')
finally:
    print("finally will executed in any situation")
