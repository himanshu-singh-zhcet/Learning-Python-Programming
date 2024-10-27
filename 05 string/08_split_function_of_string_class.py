s1='mysirg education service private limited'
l1=s1.split(' ')    #string function returns a list of strings
print(l1)
s2=input("enter no seprated by comas ")
print(s2)
l2=s2.split(',')
print(l2)
l3=[int(x) for x in l2]
print(l3)
l4=[int(x) for x in input("enter the no seprated by commas").split(',')]
print(l4)
