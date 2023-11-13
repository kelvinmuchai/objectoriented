class employee:
    raiseamount = 1.04
    employees = 0

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay =  pay
        self.email =  self.first + self.last + '@company.com'
        employee.employees += 1
       
    
    def fullname(self):
        fullname = self.first +' '+ self.last
        return fullname
       
    def apply_raise(self):
        self.pay = int( self.pay * self.raiseamount )

    @classmethod
    def number_of_employees(cls):
        return ('There are ' + str(employee.employees) + ' employess')

#inheritance
class developer(employee):
    def __init__(self,first,last,pay,prog_lang):
        #super().__init__(first,last,pay)
        #another way
        employee.__init__(self,first,last,pay)
        self.prog_lang = prog_lang


class manager(employee):
    def __init__(self,first,last,pay,employees = None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_employee(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_employees(self):
        for emp in self.employees:
            print(emp.email)


dev_1 = developer('corey','schafer',50000,'python')
dev_2 = developer('kelvin','muchahi',4000000,'java')
manager_1 = manager('john','muthiga',4000000,None)
manager_2 = manager('sam','smith',90900000,[manager_1,dev_1,dev_2])


for i in manager_2.employees:
   #isinstance helps tell which class an object belongs
    if isinstance(i,developer):
        print(i.fullname() , '--> Developer')
        
    else:
        print(i.fullname(), '--> manager')

#issubclass helps check if a class is a subclass of another class
print(issubclass(developer,employee))# returns True




       





