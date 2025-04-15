# Q4> Write a class 'Complex' to represent complex numbers, along with overload operators '+' and '*' which adds and multiply them.

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def display(self):
        print(f"The complex number is {self.real} + {self.imag}i")

    def add(self, other):
        real = self.real + other.real
        imag = self.imag + other.imag
        return Complex(real, imag)

    def multiply(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return Complex(real, imag)

    def show(self):
        print(f"The result is: {self.real} + {self.imag}i")


a = int(input("Enter the real part of the first complex number: "))
b = int(input("Enter the imaginary part of the first complex number: "))
c1 = Complex(a, b)
c1.display()

ch = int(input("Enter 1 to add or 0 to multiply two complex numbers: "))


a2 = int(input("Enter the real part of the second complex number: "))
b2 = int(input("Enter the imaginary part of the second complex number: "))
c2 = Complex(a2, b2)


if ch == 1:
    result = c1.add(c2)
    print("Addition Result:")
    result.show()
elif ch == 0:
    result = c1.multiply(c2)
    print("Multiplication Result:")
    result.show()
else:
    print("Invalid input! Please enter 1 or 0.")
