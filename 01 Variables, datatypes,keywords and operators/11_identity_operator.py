x=5
y=5
print(id(x))
print(id(y))
a= x is y
print(a)
y=6
print(id(y))
b= x is y
print(b)
b= x is not y
print(b)
