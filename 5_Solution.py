# Q5> Write a class 'Vector' representating a vector of n dimentions. Overload + and * operator which will calculate the sum and dot(.) product of them.

class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k
    
    def __add__(self, other):
        return Vector(self.i + other.i, self.j + other.j, self.k + other.k)

    def dot(self, other):
        return self.i * other.i + self.j * other.j + self.k * other.k

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"

print("Enter the values of the first vector: ")
x1 = int(input("Enter the value of x: "))
y1 = int(input("Enter the value of y: "))
z1 = int(input("Enter the value of z: "))
print("\n")
print("Enter the values of the second vector: ")
x2 = int(input("Enter the value of x: "))
y2 = int(input("Enter the value of y: "))
z2 = int(input("Enter the value of z: "))

v1 = Vector(x1, y1, z1)
v2 = Vector(x2, y2, z2)

ch = int(input("Enter 1 for addition of two vectors or else press 0 for multiplication: "))
if(ch == 1):
    print(f"The Addition of the two given vectors is: {v1 + v2}")
elif(ch == 0):
    print(f"The Multiplication of the two given vectors is: {v1.dot(v2)}")
else:
    print("Enter a valid input!!")