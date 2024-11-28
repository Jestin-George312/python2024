print("Name: Jestin George\n ")
print("\n Admission_number: A24MCA035")
print("\n experiment number:12")

class Bank_Account:
	def __init__(self):
		self.balance=0
		print("Hello!!! Welcome to the Deposit & Withdrawal Machine")

	def deposit(self):
		amount=float(input("Enter amount to be Deposited: "))
		self.balance += amount
		print("\n Amount Deposited:",amount)

	def withdraw(self):
		amount = float(input("Enter amount to be Withdrawn: "))
		if self.balance>=amount:
			self.balance-=amount
			print("\n You Withdrew:", amount)
		else:
			print("\n Insufficient balance ")

	def display(self):
		print("\n Net Available Balance=",self.balance)


s = Bank_Account()

while True :
    ch=int(input("Enter : \n1-deposit \n 2-withdraw \n 3-display balance \n 4-exit \n Enter your choice : "))

    if ch == 1:
      s.deposit()
    elif ch ==2:
        s.withdraw()
    elif ch==3:
        s.display()
    else:
        exit(1)