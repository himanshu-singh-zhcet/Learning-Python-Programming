n= int(input("enter a no "))
sum=0
while n>0 :
    a=n%10
    sum= a+sum
    n=n//10
print(sum)
