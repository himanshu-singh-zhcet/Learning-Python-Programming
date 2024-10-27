# def test():
#     print("this is the start of my function")
#     print("this is my test function")
#     print("this is the end of my function")
# test()

def deco(func):
    def inner_dec():
        print("this is start of my func")
        func()
        print("this is end of my func")
    return inner_dec
@deco
def test():
    print(6+7)

test()

import time
def timer_test(func):
    def timer_test_inner():
        start = time.time()
        func()
        end = time.time()
        print(end-start)
    return timer_test_inner

@timer_test
def test2():
    print("himanshu")


test2()