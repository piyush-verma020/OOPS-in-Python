class employee:
    name = input("Enter your name: ")
    language = input("Enter your language you are working on: ")
    salary = 120000

    def __init__(self):     # __init__ is a dunder method which atomatically get's called
        print("Be assured coder I will come when you don't need me")

    def getinfo(self):      # We could have also used somthing else instead of sel but self seems pretty reasonable to be used
        print(f"The language is: {self.language} and the salary is: {self.salary}")
    @staticmethod
    def greet():
        time = int(input("Enter the time at your location according to the 24 hours clock: "))
        if(time >= 6 and time < 12):
            print("Good Morning!")
        elif(time > 12 and time <= 17):
            print("Good Afternoon!")
        elif(time >18 and time <=20):
            print("Good Evening!")
        elif(time >20 and time <= 00):
            print("Good night!")
        else:
            print("Please do not disturb me with your nonsence stuff!!")

cl = employee()
cl.language = "javascript"
cl.greet()
cl.getinfo()                # 1
# employee.getinfo(cl)        # 2
# 1 and 2 has the same task but the syntaxes are a little different
