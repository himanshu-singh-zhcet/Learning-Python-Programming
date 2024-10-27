a,b=10,20
s1= "sum of {} and {} is {}"
s3= "sum of {2} and {1} is {0}"
print(s1)
s2=s1.format(a,b,a+b)
print(s2)
s4=s3.format(a,b,a+b)
print(s4)


