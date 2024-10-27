# write a python script to remove duplicate element from the list
l1=[10,34,55,66,88,10,30,90,45,10,44,55,66,77,]
print(l1)
s1= set(l1)
print(s1)
l2=list(s1)
print(l2)
l3=list(set([int(x) for x in input("enter no seperate by commas ").split(',')]))
print(l3)