balance = 10000
transactions = []

def show_options():
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. View Transaction History")
    print("5. Exit")

def deposit():
    global balance
    amount = int(input("Enter amount to deposit:"))
    if(amount > 0):
        balance += amount
        print(f"\n${amount} deposited")
        print(f"New balance : ${balance}\n\n")
        tran_msg = f"${amount} deposited successfully"
        transactions.append(tran_msg)
    else:
        print("\nEnter a valid amount to deposit\n\n")

def withdraw():
    global balance
    amount = int(input("Enter amount to withdraw:"))
    if(amount < balance):
        balance -= amount
        print(f"\n${amount} withdrawn")
        print(f"Updated balance : ${balance}\n\n")
        tran_msg = f"${amount} withdrawn successfully"
        transactions.append(tran_msg)
    else:
        print("\nEnter a valid amount to withdraw\n\n")

def show_transactions():
    if len(transactions) == 0:
        print("\nNo transactions made yet!\n\n")
    else:
        index = 1
        print("\nAll Transactions:")
        for t in transactions:
            print(f"{index}. {t}")
            index +=1
        print("\n\n")

print("===================================================")
print("                      ATM                          \n")

show_options()



while True:
    choice = int(input("Enter your choice:"))

    if choice == 1:
        print(f"\nYour current balance is ${balance}\n\n")
        show_options()

    elif choice == 2:
        deposit()
        show_options()

    elif choice == 3:
        withdraw()
        show_options()

    elif choice == 4:
        show_transactions()
        show_options()

    elif choice == 5:
        break

    else:
        print("Please enter a valid choice")
        show_options()
        


