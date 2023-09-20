#Python program to create Bankaccount class
#with both a deposit() and a withdraw() function
class Bank_Account:
  def __init__(self):
    self.balance=0
    print("hello!!! Welcome to the Deposit & Withdrawal Machine")

  def deposit(self): 
    amount=float(input("Enter amount to be Deposited:"))
    self.balance+=amount
    print("\n Amount Deposited:", amount)
    
    def withdraw(self):
      amount=float(input("Enter amount to be withdrawn:"))
      if self.balance>=amount:
        self.balance-=amount
        print("\n You Withdraw:",amount)
      else:
        print("\n Insufficient balance ")
        
    def display(self):
      print("\n Net Available Balance=",self.balance)

#Driver code

#creating an object of class
s = Bank_Account()

#calling function with that class object
s.deposit()
s.withdraw()
s.display()