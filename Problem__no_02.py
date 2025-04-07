# Question 2:-
# || Write a class "Calculator" which is capable of finding the square, cube and square root of a number

import math

class Calculator:
    def square(self,n):
        self.sq = n**2
        print(f"The square of the given number is: {self.sq}")

    def cube(self,n):
        self.cub = n**3
        print(f"The cube of the given number is: {self.cub}")
    def square_root(self,n):
        sqrt = n ** 0.5
        print("Square root of {} is {:.2f}".format(n, sqrt))

n = int(input("Enter the number: "))
choice = int(input("Enter 1 for square, 2 for cube, 3 for sqrt: "))
cl = Calculator()
if(choice == 1):
    cl.square(n)
elif(choice == 2):
    cl.cube(n)
elif(choice == 3):
    cl.square_root(n)
else:
    print("Please Enter A Valid Input!!")