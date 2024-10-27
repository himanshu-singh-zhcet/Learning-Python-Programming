def test_fib(n):  # generator function
    a,b=0,1
    for i in range(n):
        yield a      # when we used yield it is a generator function // data store nhi hota memory main 
        a,b = b,a+b

for i in test_fib(10):
    print(i)


def test_fib1():  # generator function
    a,b=0,1
    while True:
        yield a      # when we used yield it is a generator function 
        a,b = b,a+b

fib = test_fib1()

for i in range(10):
    print(next(fib))

s ="hima"
for i in s:  # for loop bhi pahle s ko iter ke andr bhejta hai s ki length ptta lagata hai
    print(i)

# print(next(s))  # it will show an error because string is not a iterator
print("now s becomes iterator")
s1  = iter(s)
print(next(s1))
print(next(s1))
print(next(s1))

# iterator waisa object ya waose data jisko hum next next krke data nikal ske iterable waisa object ya data jisko on=bject main convert kr skee