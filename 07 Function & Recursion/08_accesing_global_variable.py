x =10  # global variabl 
def f1():
    global x  # if we put global x after x =5 then it will show an error 
    x=5   # global variable
    print(x)
    print(x)

print(x)
f1()
print(x)