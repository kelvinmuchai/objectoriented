class employee:
     def __init__(self,first,last):
        self.first = first
        self.last = last
    
    #a property decorater
     @property
     def fullname(self):
        fullname = self.first +' '+ self.last
        return fullname
     
     #a property decorater
     @property
     def email(self):
         email =  self.first + self.last + '@company.com'
         return email
    
     #create a setter method for fullname
     @fullname.setter
     def fullname(self,name):
         first,last = name.split(' ')
         self.first = first
         self.last = last
    #creates a deleter method for fullname
     @fullname.deleter
     def fullname(self):
         self.first = None
         self.last = None
         print('deleted')

emp_1=employee('kelvin','muchai')


emp_1.fullname = 'james muigai'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
del emp_1.fullname
print(emp_1.fullname)