def f1(a,b):
    print("a=",a,"b=",b)
f1(2,4)  # positional arguments
f1(2,b=4)  #positional argumnet ke baad keyword argumnet aa skta hai but vice versa is not true
# f1(2,a=4)  this will show an type error 
# f1(b=4,2)  it will show an syntax error
f1(b=4,a=2)