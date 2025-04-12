# Super() Method 
class abc:
    def __init__(self):
        print("This is an abc class")
    a = 1
class bca(abc):
    def __init__(self):
        print("This is a bca class")
    b = 2
class cab(bca):
    def __init__(self):
        super().__init__()
        print("This is a cba class")
    c = 3

z = cab()
print(z.c)

# Class Method
# @Property Decorators
# @.Getters and @.Setters

class Value:
    a = 1
    def show_value(self):
        print(f"The instamce value of a is {self.a}")
    @classmethod
    def cla_value(cls):
        print(f"The class value of a is {cls.a}")
    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    @name.setter
    def name(self,value): 
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

o = Value()
o.a = 45

o.name = "Larry Parry"
print(o.name)
print(o.fname, o.lname)

o.show_value()
o.cla_value()
