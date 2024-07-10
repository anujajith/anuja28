class Account:
    def init(self):
        self.balance=0
        print("welcome to the bank")
    def deposit(self):
        amount=int(input("Enter amount to be deposited:"))
        self.balance=amount
        print("Deposited")
    def withdrawal(self):
        amount=int(input("enter amount to be withdrawed:"))
        if amount<=self.balance:
                              self.balance-=amount
        else:
                              print("insufficient balance")
    def check_balance(self):
                              print("current balance",self.balance)
account=Account()
while True:
                              print("1.Deposit")
                              print("2.withdraw")
                              print("3.check balance")
                              print("4.Exit")
                              choice=int(input("Enter your choice:"))

                              if choice==1:
                                  account.deposit()
                              elif choice==2:
                                  account.withdrawal()
                              elif choice==3:
                                  account.check_balance()
                              elif choice==4:
                                  print("Thanks for banking with us")
                                  break
                              else:
                                  print("invalid choice")
                              
