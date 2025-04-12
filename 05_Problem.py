# Question 5:-
# || Write a class train which has methods to book train ticket, get status(no. of seats) and get fair information of the train running under Indian Railways.

import random

class Train:
    def __init__(self):
        self.seats = 4
        self.booked = False

    def book(self):
        print("There are only 4 seats available")
        self.book = int(input("Enter how many number of seats do you wish to book: "))
        if(self.book > self.seats):
            print(f"Not enough seats. Only {self.seats} seats available.")
            return
        else:
            self.available = self.seats - self.book
            self.booked = True
            print(f"Booking successful! You have booked {self.book} seat(s).")

    def fair(self):
        self.price = 3076
        print(f"The fair for your seat is: ₹{self.price}")

    def get_status(self):
        if not self.booked:
            print("You haven't booked any seat yet.")
            return
        self.num = "0123456789"
        self.sym = "@#$/"
        self.length = 6
        print("Your train ticket details:")
        for i in range(self.book):
            ticket = ''.join(random.choices(self.num + self.sym, k=self.length))
            seat_no = random.randint(1, 100)
            print(f"Ticket #{i+1}: {ticket} | Seat: {seat_no}")
        print("Thank you for choosing Indian Railways!")

print("Welcome Sir/ma'am")
cl = Train()
ch = 1
while(ch != 0):
    print("\nThe train is going to Delhi from Kolkata")
    print("What do you wish to do: ")
    print("1. BOOK A TICKET")
    print("2. GET STATUS")
    print("3. FAIR INFORMATION")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        cl.book()
    elif choice == 2:
        if not cl.booked:
            query = int(input("Did you book your train seats? Press 1 to book, or 0 to continue: "))
            if query == 1:
                cl.book()
        else:
            cl.get_status()
    elif choice == 3:
        cl.fair()
    else:
        print("Please Enter a Valid Input!!")
    
    ch = int(input("Enter 0 if you wish to exit or else press any number: "))
