# class test:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
# t = test(10,12)
# print(t.a)
# t.a =23    #encapsulation main user directly acces na kr paaye
# print(t.a)

class car:
    def __init__(self,year,make,model,speed):
        self.__year = year   #encapsulation ,private variable
        self.__make = make
        self.__model = model
        self.__speed = speed
    
    def set_speed(self,speed):   # is function ki help se hi varibale ko acces kr skte hai ya data ko nikal skte hai 
        self.__speed= 0 if speed<0 else speed
    
    def get_speed(self):
        return self.__speed
    




c = car(2021,"toyata","inova",80)
print(c._car__speed)   # claas ke naam use krke variable ko print kra skte hai  
c.set_speed(90)
print(c._car__speed)
s =c.get_speed()
print(s)

class bank_account:
    def __init__(self,balance):
        self.__balance = balance
    def deposit(self,amount):
        self.__balance = self.__balance+amount
    def withardwal(self,amount):
        if self.__balance>= amount:
            self.__balance = self.__balance-amount
            return True
        else :
            return False
    def check_balance(self):
        return self.__balance
    
    
sudh = bank_account(1000)
print(sudh.check_balance())
sudh.deposit(2)
print(sudh.check_balance())
