# Question 4:-
# || Add a static method in problem 2, to greet the user with hello.

class Calculator:
    @staticmethod
    def static():
        print("Good Morning, Coder")

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
cl.static()
if(choice == 1):
    cl.square(n)
elif(choice == 2):
    cl.cube(n)
elif(choice == 3):
    cl.square_root(n)
else:
    print("Please Enter A Valid Input!!")