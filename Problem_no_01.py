# Question 1:-
# || Create a class "Programmer" for storing the information of few programmer working in microsoft

class programer:
    company = "Microsoft"
    # Constructor to initialize object and collect programmer data
    def __init__(self):

        self.num = int(input("Enter the number of programers you wish to store: "))
        self.data = {}
        
        for i in range(1, self.num + 1):
            # Take the name of the programmer
            self.name = input(f"Enter the name of the {i} programer: ")
            # Take the identity number of the programmer
            self.value = input(f"Enter the identity number of {i} programer: ")
            # Store the name and identity number in the dictionary
            self.data.update({self.name: self.value})

    # Method to write the collected data to a file
    def update_info_file(self):
        # Opens a file in write mode and storing the dictionary values as a string
        with open("microsoft.txt", "w") as f:
            f.write(str(self.data))  # Note: This only writes it as plain string not in readable JSON format

# Create an object of the class which will collect the data
k = programer()
print(k.company)
# Calling the method to write the data to an wxisting file
k.update_info_file()
