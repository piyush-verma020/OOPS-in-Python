class Programmer:
    salary = 12000
    name = "Jef"

class Coder:
    language = "Python"
    def show_language(self):
        print(f"Out of all possible language you choose {self.language}")

# Multiple Inheritance
class Print(Programmer, Coder):
    def show_name(self):
        print(f"The name of the programmer is {self.name} and the language he is good with is {self.language} and his monthly salary is {self.salary}")

p = Programmer()
c = Coder()
P = Print()
c.show_language()
P.show_name()

# Multilevel Inheritance
class abc:
    a = 1
class bca(abc):
    b = 2
class cab(bca):
    c = 3
x = abc()
y = bca()
z = cab()
print(x.a) # Prints the a attribute
# print(x.b)  # This will show an error since there is no b present in the abc class
print(y.a,y.b)
print(z.a,z.b,z.c)