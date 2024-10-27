class test:
    def test_meth(self):
        print("this is my first class ")

class child_class(test):  # calling test class 
    pass

child_class_obj = child_class()
child_class_obj.test_meth()

# multilevel_inheritance
class class1:
    def test_class1(self):
        print("this method is form calss1")

class class2(class1):
    def test_class2(self):
        print("this method is from class2")

class class3(class2):
    pass

obj = class3()
obj.test_class1()
obj.test_class2()




