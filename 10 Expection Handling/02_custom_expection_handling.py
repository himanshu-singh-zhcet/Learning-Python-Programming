class validage(Exception):
    def __init__(self,msg):
        self.msg = msg

def validage1(age):
    if age<=0:
        raise validage("entered age is negative")
    elif age>200:
        raise validage("entered age is very high")
    else:
        print("entered age is negative")

try:
    age= int(input("enter your age "))
    validage1(age)
except validage as e:
    print(e)
