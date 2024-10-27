def f1(a,b,c=0):   #vf1(a,b=0,c) it will show an error because non default argument can not come after default argument
    d=a+b+c
    print(d)
f1(1,2,3)
f1(2,4)