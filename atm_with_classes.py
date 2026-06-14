class BankAccount:

    def __init__(self,name,balance,transaction):
        self.name = name
        self.balance = balance
        self.transaction = transaction

    def show_options():
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. View Transaction History")
        print("5. Exit")

    def deposit(self):
        amount = int(input("Enter amount to deposit:"))
        if(amount > 0):
            self.balance += amount
            print(f"\n${amount} deposited")
            print(f"New balance : ${self.balance}\n\n")
            tran_msg = f"${amount} deposited successfully"
            self.transaction.append(tran_msg)
        else:
            print("\nEnter a valid amount to deposit\n\n")

    def withdraw(self):
        amount = int(input("Enter amount to withdraw:"))
        if(amount < self.balance):
            self.balance -= amount
            print(f"\n${amount} withdrawn")
            print(f"Updated balance : ${self.balance}\n\n")
            tran_msg = f"${amount} withdrawn successfully"
            self.transaction.append(tran_msg)
        else:
            print("\nEnter a valid amount to withdraw\n\n")

    def show_transactions(self):
        if len(self.transaction) == 0:
            print("\nNo transactions made yet!\n\n")
        else:
            index = 1
            print("\nAll Transactions:")
            for t in self.transaction:
                print(f"{index}. {t}")
                index +=1
            print("\n\n")

customer1 = BankAccount("customer1",10000,[])
customer2 = BankAccount("customer2",10000,[])
customer3 = BankAccount("customer3",10000,[])
customer4 = BankAccount("customer4",10000,[])

customer4.deposit()
print(customer4.balance)

