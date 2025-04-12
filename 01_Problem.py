# Question 1:-
# || Create a class "Programmer" for storing the information of few programmer working in microsoft

class programer:
    company = "Microsoft"

    # Constructor to initialize object and collect programmer data
    def __init__(self):
        self.num = int(input("Enter the number of programmers you wish to store: "))
        self.data = {}

        for i in range(1, self.num + 1):
            name = input(f"Enter the name of the {i} programmer: ")
            identity = input(f"Enter the identity number of {i} programmer: ")
            salary = int(input(f"Enter the salary of {i} programmer: "))

            # Store the data in a nested dictionary
            self.data[name] = {"id": identity, "salary": salary}

    # Method to write the collected data to a file
    def update_info_file(self):
        with open("microsoft.txt", "w") as f:
            f.write(str(self.data))

    # Method to get salary of a specific programmer
    def get_salary(self, name):
        if name in self.data:
            return self.data[name]["salary"]
        else:
            return "Programmer not found."

# Create an object
k = programer()

# Access class variable
print(k.company)

# Save data to file
k.update_info_file()

# Example: Get salary
name_to_search = input("Enter the name of the programmer to get their salary: ")
print("Salary:", k.get_salary(name_to_search))
