class ATM:
    def __init__(self):
      
        self.balance = 0 
        self.pin = "1234"  
        self.transaction_history = [] 

    def check_balance(self):
       
        print(f"Your current balance is ${self.balance:.2f}")  
        self.transaction_history.append("Checked balance") 

    def deposit(self, amount)
        if amount > 0: 
            self.balance += amount 
            print(f"Deposited ${amount:.2f}")  
            self.transaction_history.append(f"Deposited ${amount:.2f}")  
        else:
            print("Deposit amount must be positive.")  

    def withdraw(self, amount):
      
        if amount > 0: 
            if amount <= self.balance:  
                self.balance -= amount  
                print(f"Withdrew ${amount:.2f}") 
                self.transaction_history.append(f"Withdrew ${amount:.2f}")  
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")  

    def change_pin(self, old_pin, new_pin):
                if old_pin == self.pin: 
            if len(new_pin) == 4 and new_pin.isdigit():  
                self.pin = new_pin 
                print("PIN changed successfully.")
                self.transaction_history.append("Changed PIN")
            else:
                print("New PIN must be a 4-digit number.") 
        else:
            print("Old PIN is incorrect.")  

    def print_transaction_history(self):
        
        if not self.transaction_history:  
            print("No transactions yet.") 
        else:
            for transaction in self.transaction_history:  
                print(transaction)


if __name__ == "__main__":
    atm = ATM() 
    while True:
    
        print("\nATM Menu:")
        print("1. Check Balance") 
        print("2. Deposit") 
        print("3. Withdraw")  
        print("4. Change PIN") 
        print("5. View Transaction History") 
        print("6. Exit") 
        
       
        choice = input("Enter your choice (1/2/3/4/5/6): ")  
        
        if choice == '1':
            atm.check_balance()  
        elif choice == '2':
            try:
                amount = float(input("Enter the amount to deposit: ")) 
                atm.deposit(amount)  
            except ValueError:
                print("Invalid amount. Please enter a number.") 
        elif choice == '3':
            try:
                amount = float(input("Enter the amount to withdraw: ")) 
                atm.withdraw(amount)
            except ValueError:
                print("Invalid amount. Please enter a number.") 
        elif choice == '4':
            old_pin = input("Enter your old PIN: ")  
            new_pin = input("Enter your new 4-digit PIN: ")
            atm.change_pin(old_pin, new_pin) 
        elif choice == '5':
            atm.print_transaction_history() 
        elif choice == '6':
            print("Thank you for using the ATM. Goodbye!") 
            break  
        else:
            print("Invalid choice. Please select a valid option.")
