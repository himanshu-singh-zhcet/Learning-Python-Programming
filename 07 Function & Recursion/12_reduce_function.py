from functools import reduce
l=[1,2,3,4,5,6]
a=reduce(lambda x,y:x+y,l)  # it always take two parameter eg a=reduce(lambda x,y,z:x+y+z,l) it will show an error 
print(a)
print(type(a))

b = reduce(lambda x,y: x if x>y else y,l)
print(b)