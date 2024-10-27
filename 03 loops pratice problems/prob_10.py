a= int(input("enter the first no "))
b= int(input("enter the second no "))
c=a if a>b else b
while c<=a*b :
    if c%a==0 and c%b==0 :
        print("the lcm is",c)
        break
    c=c+1
