# Q3> Create a class 'Employee' and add salary and increament properties to it.
#     Write a method 'salaryAfterIncreament' method with a @property decorator along with a setter which changes the value of increament based on the salary.

class Employee:
    salary = 20000
    salary_increament = 30

    @property
    def salaryAfterIncreament(self):
        return (self.salary + (self.salary * self.salary_increament/100))
    @salaryAfterIncreament.setter
    def salaryAfterIncreament(self, salary):
        self.salary_increament = ((salary / self.salary) -1) * 100
    
    def show(self, name):
        self.name = name
        print(f"The salary of the Employee named {self.name} is: {e.salaryAfterIncreament}")
        print(f"The increament of salary is: {self.salary_increament}%")

name = input("Enter the name of the employee: ")
e = Employee()
e.show(name)