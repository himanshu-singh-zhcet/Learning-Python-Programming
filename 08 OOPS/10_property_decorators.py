class pwskills:
    def __init__(self,course_price,course_name):
        self.__course_price = course_price
        self.course_name = course_name
    
    @property  # is ki madad se hum private variable ko acces kr skte hai 
    def course_price_access(self):
        return self.__course_price
    
    @course_price_access.setter   # iski help se hum variable ki value ko modify bhi kr skte hai 
    def course_price_set(self,price):
        if price<=3500:
            pass
        else:
            self.__course_price= price
        
    @course_price_access.deleter  # iski help se hum variable ko delete kr kste hai 
    def delete_course_price(self):
        del self.__course_price
    
pw = pwskills(1200,"data science")
print(pw.course_price_access)
pw.course_price_set =4500
print(pw.course_price_access)
del pw.delete_course_price
print(pw.course_price_access)
