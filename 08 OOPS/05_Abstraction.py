import abc
class pwskills:
    @abc.abstractmethod
    def student_details(self):
        pass
    @abc.abstractmethod
    def student_assignment(self):
        pass
    @abc.abstractmethod
    def student_marks(self):
        pass

class web_develoment(pwskills):
    def student_details(self):
        print("this is a method for taking student dertails of erb development : ")
    def student_assignment(self):
        print("this is method for assigning the assignment: ")
    
class data_science(pwskills):
    def student_details(self):
        print("this will retrun student details for data science masters ")
    def student_assignment(self):
        print("this will give you student assignment details for data science masters  ")

dsm = data_science()
dsm.student_details()

wd = web_develoment()
wd.student_details()