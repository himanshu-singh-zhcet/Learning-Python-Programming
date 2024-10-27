# print(dir(int))  for printing the list of function applicable on int
a =100
print(a.__add__(5))
print(a)

class pwskills:
    def __new__(cls):
        print("this is my new")
    def __init__(self):
        print("this is my init")
        self.mobilenumber = 8171

pw = pwskills()

class pwskills1:
    
    def __init__(self):
        self.mobilenumber = 8171
    
    def __str__(self):    # hm chahte hai jb hum object ko print karaye to hexadecimal code na aaye usji jgh wo aaye jo hun chahte hai 
        return ("thi is my magic call of str ")
pw1 = pwskills1()
print(pw1)
