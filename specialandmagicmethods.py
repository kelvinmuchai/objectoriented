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
        return fullname
       
    def apply_raise(self):
         self.pay = int( self.pay * self.raiseamount )

    def __repr__(self):
        return f'{self.email}'    

    def __str__(self):
       return f"{self.first} {self.last}"
    
    

    def __add__(self,other):
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.fullname())

emp_1 = employee('kelvin','muchai',40000)
emp_2 = employee('jane','wangui',60000)

print(emp_1)
print(emp_1 + emp_2)
print(len(emp_2))


