# write a program to check wether a given no is prime or not
a = int(input("enter a no "))
i=2
while i<=a-1 :
    if a%i==0 :
        print("it is not a prime no")
        break
    i+=1
if i==a :
    print("no is prime")


