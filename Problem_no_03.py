# Question 3:-
# || Create a class attribute a; create an aboject from it and set 'a' directly using object a=0. Does this change the class attribute

class MyClass:
    a = 10  # class attribute

obj = MyClass()   # create object
obj.a = 0         # set 'a' using the object

print("Class attribute:", MyClass.a)
print("Object attribute:", obj.a)

# The output for the above code is:
# Class attribute: 10
# Object attribute: 0

# So from the given example we understand that setting 'a' directly using the object does not change the class attribute. 
# It only creates an instance attribute instead