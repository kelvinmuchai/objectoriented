class employee:

    #class variable
    num_of_employees = 0
    raiseamount = 1.04

    #constructer 
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay =  pay
        self.email =  self.first + self.last + '@company.com'
        employee.num_of_employees += 1
        
    
    def fullname(self):
        fullname = self.first +' '+ self.last
        print(fullname)
       
    def apply_raise(self):
         self.pay = int( self.pay * self.raiseamount )


emp_1 = employee('kelvin','muchai',40000)
emp_2 = employee('jane','wangui',60000)
emp_3 = employee('james','mungai',290000)
print(employee.raiseamount)
print(employee.num_of_employees)
emp_1.apply_raise()
emp_1.apply_raise()
emp_1.apply_raise()
print(emp_1.pay)