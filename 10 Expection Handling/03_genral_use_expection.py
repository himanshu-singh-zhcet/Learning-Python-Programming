try:
    a = 10/0
except ZeroDivisionError as e:
    print(e)

try:
    int("sidh")
except (ValueError,TypeError) as e:  # multiple errors bhi likh skte hai 
    print(e)

try:
    int("sidh")
except:
    print("this will catch an error")

# import error
try:
    import sudh
except ImportError as e:
    print(e)

# key error
try:
    d = {"key":"sudh",1:[1,2,3,4]}
    print(d["key2"])
except KeyError as e :
    print(e)

#attribute error
try:
    "sudh".test()
except AttributeError as e:
    print(e)

#index error
try:
    l = [2,3,4,5]
    print(l[6])
except IndexError as e:
    print(e)

# type error
try:
    123+"sidh"
except TypeError as e:
    print(e)

#file not found error
try: 
    with open("test.txt",'r') as f:
        test = f.read()
except FileNotFoundError as e:
    print(e)

try: 
    with open("test.txt",'r') as f:
        test = f.read()
except Exception as e:   # expection ek super class hai ye hi isse handle kr lega neeche waale handler pr nhi jaane dega 
    print(e)             # or generic or expection (super class) kabhi bhi uper nhi likhna chahiye kyuki ye neeche waalo ko chlne hi nhi dega
except FileNotFoundError as e:
    print("hii ",e)

def test(file):    # try or expect ko  function or classes main bhi rkh skte hai 
    try:
        with open(file,'r') as f:
            test = f.read()
    except FileNotFoundError as e:
        print(e)

       
         
    