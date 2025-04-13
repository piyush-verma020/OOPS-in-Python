# Q2> Create a class 'Pets' from a class 'Animals and further create a class 'Dog' from 'Pets'. And add a method 'bark' to class 'Dog'.

class Animals:
    def __init__(self):
        self.l2 = ["Dog", "Cat", "Parrot", "Rabbit", "Hamster", "Cow"]

class Pets(Animals):
    def __init__(self):
        super().__init__()

    def show(self):
        print("\nThe following animals are commonly kept as pets:")
        for animal in self.l2:
            print(f"- {animal}")
        print("\nNote: Some humans try to tame wild or endangered animals, which is clearly illegal.")

class Cow(Animals):
    def __init__(self):
        super().__init__()
    def mooooo(self):
        print("Moo Moo")
        print("Well what else did you expect from a cow to say! Skibidi.")
        print("Well other animals you might be interested in are: ")
        for animals in self.l2:
            print(f"-{animals}")

class Cats(Pets):
    def __init__(self):
        super().__init__()

    def meowing(self):
        print("\nBATMAN: Where is the cat nip!")
        print("CAT: Meow! me wou wonn")

class Dog(Pets):
    def __init__(self):
        super().__init__()

    def wof(self):
        print("\nDog: Wooof!")

# Create objects
meow = Cats()
bark = Dog()
info = Pets()
mo = Cow()

# List of options
l1 = ["bark", "meow", "moo"]
print("Available actions:", l1)

# Input
user = input('Enter the type of noise from the list, or type "pets" to see pet options: ').lower()

# Logic
if(user in l1):
    if(user == "bark"):
        bark.wof()
    elif(user == "meow"):
        meow.meowing()
    elif(user == "moo"):
        mo.mooooo()
    else:
        print("\nMooing sound is not defined yet. Try barking or meowing.")
elif(user == "pets"):
    info.show()
else:
    print("\nINVALID INPUT!")
    print("Please enter a valid option from the list.")