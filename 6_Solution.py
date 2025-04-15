# Q6> Write a __str__() method to print the vector as follows:-
#     7i + 8j + 10k
#     Assume the dimmension 3 for this problem.

class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k
    
    def __add__(self,other):
        self.result = Vector(self.i + other.i, self.j + other.j, self.k + other.k)
        return self.result
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
print(v1 + v2)