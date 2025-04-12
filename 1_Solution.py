# Q1> Create a class(2-D vector) and use it to create another class representing another 3-D vector.

class Two_D_vector:
    def __init__(self, i, j):
        self.i = i
        self.j = j
    
    def show(self):
        print(f"The 2-D vector has following dimensions: {self.i}i +{self.j}j")

class Three_D_vector(Two_D_vector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k
    
    def show(self):
        print(f"The 3-D vecor has the following dimmensions: {self.i}i + {self.j}j + {self.k}k")

d2 = Two_D_vector(2, 3)
d3 = Three_D_vector(2, 3, 1)
d2.show()
d3.show()