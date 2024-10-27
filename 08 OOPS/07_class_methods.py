# class pwskills:
#     def __init__(self,name,email):
#         self.name = name
#         self.email = email
#     @classmethod
#     def details(cls,name,email):
#         return cls(name,email)
#     def student_details(self):
#         print(self.name,self.email)

# pw = pwskills.details("himanshu","hanshu@gmail.com") # bina object create kiye  name or email id pass kr paa rha hu 
# print(pw.name)
# pw.student_details()

class pwskills:

    mibile_num = 8171912220        # class variable
    def __init__(self,name,email):
        self.name = name
        self.email = email
    
    @classmethod
    def change_no(cls,mobile):
        pwskills.mibile_num = mobile

    @classmethod
    def details(cls,name,email):
        return cls(name,email)
    def student_details(self):
        print(self.name,self.email,pwskills.mibile_num)


pw = pwskills.details("himanshu","hanshu@gmail.com") # bina object create kiye  name or email id pass kr paa rha hu 
print(pw.name)
pw.student_details()
print(pw.mibile_num)
pw.change_no(96234567)
print(pw.mibile_num)
pw.student_details()   # class method ke jariye kisi dusre method ko bhi access kr skte hai



class pwskills2:
    mibile_num = 8171912220        # class variable
    def __init__(self,name,email):
        self.name = name
        self.email = email
    
    @classmethod
    def change_no(cls,mobile):
        pwskills2.mibile_num = mobile

    @classmethod
    def details(cls,name,email):
        return cls(name,email)
    def student_details(self):
        print(self.name,self.email,pwskills2.mibile_num)

def course_details(cls,course_name):  #external function 
    print("cousse name is : ",course_name)

pwskills2.course_details = classmethod(course_details)   # making external function a class method 
pwskills2.course_details("data_science")

class pwskills3:
    mibile_num = 8171912220        # class variable
    def __init__(self,name,email):
        self.name = name
        self.email = email
    
    @classmethod
    def change_no(cls,mobile):
        pwskills3.mibile_num = mobile

    @classmethod
    def details(cls,name,email):
        return cls(name,email)
    def student_details(self):
        print(self.name,self.email,pwskills3.mibile_num)
    
del pwskills3.change_no  # or delattr(pwskills3,"change_no") # deleting a method from class pwskills3
#  delattr(pwskills3,"mobile_num") this will work for deleting class variable 

