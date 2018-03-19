class Employee:
    'Common base class for all employees'
    empCount = 0

    def __init__(self, name, salary, age):
        self.name = name
        self.age = age
        self.salary = salary
        Employee.empCount += 1
   
    def showCount(self):
        print ("Total Employee %d" % Employee.empCount)

    def printEmployee(self):
        print ("Name : ", self.name,  ", Age: ", self.age, ", Salary: ", self.salary)

"This would create first object of Employee class"
emp1 = Employee("Zara", 2000, 25)
"This would create second object of Employee class"
emp2 = Employee("Manni", 5000, 27)
emp1.printEmployee()
emp2.printEmployee()
print ("Total Employee %d" % Employee.empCount)

#emp1.age = 8  # Modify 'age' attribute.
#emp1.printEmployee()
#del emp1.age  # Delete 'age' attribute.
#emp1.printEmployee()
#print ("Employee.__doc__:", Employee.__doc__)
#print ("Employee.__name__:", Employee.__name__)
#print ("Employee.__module__:", Employee.__module__)
#print ("Employee.__bases__:", Employee.__bases__)


