def add(a,b):
    return a+b
s=add(3,4)
print(s)

x = add
print(id(add))
print(id(x))
print(x)
print(x(2,3))
