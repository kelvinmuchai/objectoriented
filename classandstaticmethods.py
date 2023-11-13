class employee:
    #class variable
    num_of_employees = 0
    raiseamount = 1.04

    #class method
    @classmethod
    def setraiseamount(cls,amount):
        cls.raiseamount = amount
       
    #constructer 
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay =  pay
        self.email =  self.first + self.last + '@company.com'
        employee.num_of_employees += 1
        
    #normal method
    def fullname(self):
        fullname = self.first +' '+ self.last
        print(fullname)
       
    def apply_raise(self):
         self.pay = int( self.pay * self.raiseamount )

    #static method
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday==6:
            return False
        return True
        
import datetime
my_date = datetime.date(2016,5,10)
print(employee.is_workday(my_date))
employee.setraiseamount(1.05)
print(employee.raiseamount)

