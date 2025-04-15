# Q7> Override the __len__() method on vector of problem 5 to display the dimmension of the vector.

class Vector:
    def __init__(self, l):
        self.l = l
    
    def __len__(self):
        return len(self.l)


print("Enter the values of the first vector: ")
x1 = int(input("Enter the value of x: "))
y1 = int(input("Enter the value of y: "))
z1 = int(input("Enter the value of z: "))

v1 = Vector([x1, y1, z1])
print(len(v1))