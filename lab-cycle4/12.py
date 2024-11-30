print("Name: Jestin George\n ")
print("\n Admission_number: A24MCA035")
print("\n experiment number: 12")

class Bank_Account:
    def __init__(self):
        self.balance = 0
        print("Hello!!! Welcome to the Deposit & Withdrawal Machine")

    def deposit(self):
        amount = float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited:", amount)

    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance ")

    def display(self):
        print("\n Net Available Balance=", self.balance)


try:
    s = Bank_Account()

    while True:
        ch = int(input("Enter: \n1 - deposit \n2 - withdraw \n3 - display balance \n4 - exit \nEnter your choice: "))

        if ch == 1:
            s.deposit()
        elif ch == 2:
            s.withdraw()
        elif ch == 3:
            s.display()
        elif ch == 4:
            print("\nExiting the program...!")
            break
        else:
            print("\nInvalid choice! Please enter a valid option.")
except Exception as e:
    print(f"An exception occurred: {e}")
