def test(a,b):
    return a+b

print(test(4,5))    
print(test("hello","world"))

class data_science:
    def slybuss(self):
        print("this is my slybusss for data science master: ")
class web_dev:
    def slybuss(self):
        print("this is slybuss for web development")

def class_parcer(class_object):
    for i in class_object:
        i.slybuss()

data_science = data_science()
web_dev= web_dev()
class_obj = [data_science,web_dev]
class_parcer(class_obj)  # a function behave differently depend on the object which i m going to pass