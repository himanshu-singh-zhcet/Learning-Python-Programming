x =10      #global variable
def f1():   
    x =5   # local variable
    g=globals()
    print("local x = ",x)
    print("global x",g['x'])

print("global x = ",x)
f1()

