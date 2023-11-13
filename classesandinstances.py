class employee:

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay =  pay
        self.email =  self.first + self.last + '@company.com'
        print('new object formed')
    
    def fullname(self):
        fullname = self.first +' '+ self.last
        print(fullname)
       
     


emp_1 = employee('kelvin','muchai',40000)
emp_2 = employee('jane','wangui',60000)
emp_3 = employee('james','mungai',290000)

employee.fullname(emp_2)

print(emp_1.email)
emp_1.fullname()
emp_2.fullname()