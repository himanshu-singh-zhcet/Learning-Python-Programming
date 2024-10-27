class pwskills:
    def student_details(self,name,email_id,mobile_no):
        print(name,email_id,mobile_no)
        self.mentor_class(["himi","shivi"])  #calling static method in the object method 
    
    @staticmethod
    def mentor_email_id(email_id):
        print(email_id)
    @staticmethod     # static method class name se access hota hai 
    def mentor_class(list_mentor):
        print(list_mentor)
        pwskills.mentor_email_id(["hanshu","shivi"])    #calling static method in the static method
    
    @classmethod
    def class_name(cls):
        cls.mentor_class(["sugh","krish"])    #calling static method in the class method

    

pwskills.mentor_class(["himanshu","shivani"])
pwskills.class_name()

pw = pwskills()   # creating an object 
pw.student_details("himanshu","hanshu",8171912220)

