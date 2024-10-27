class test:  # empty class
    pass

a = test()
print(type(a))

class pwskills:
    def welcome(self):
        print("welcome to pw skills")

rohan = pwskills()
rohan.welcome()

class pwskills:
    def __init__(self,phone_no,email_id,student_id):  # yhaa self ki jagah kuch bhilikh skte hai jo behave karewga as a pointer
        self.phone_no = phone_no
        self.email_id = email_id
        self.student_id = student_id
    def student_details(self):
        return self.phone_no,self.email_id,self.student_id

robin = pwskills(8171912220,"hanshu5252@gmail.com",101)
print(robin.student_details()) 