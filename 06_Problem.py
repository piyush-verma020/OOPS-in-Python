# Question 6:-
# || Can you change the self-parameter inside a class to something else(Let's say "Py"). Try changing self to "slf" or "Py" and see the effects

class test:
    def check(py):
        py.num = int(("Enter a number: "))
        print(f"The solution of {py.num} ^ {py.num} is: {py.num ** py.num}")
cl = test()
cl.check()

# As from the given example there is no error while changing the self parameter into py and neither will anything else unless it's predefined library for example else it will surely give an error
