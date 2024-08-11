class ATM:
    def __init__(self):
        # Initialize the ATM with default values
        self.balance = 0  # Set the initial balance to 0 dollars
        self.pin = "1234"  # Set the default PIN (Personal Identification Number) to "1234"
        self.transaction_history = []  # Create an empty list to keep track of all transactions

    def check_balance(self):
        # Display the current balance and record this action in the transaction history
        print(f"Your current balance is ${self.balance:.2f}")  # Show the balance in dollars with two decimal places
        self.transaction_history.append("Checked balance")  # Add "Checked balance" to the transaction history

    def deposit(self, amount):
        # Add money to the balance if the amount is positive, and record the deposit in the history
        if amount > 0:  # Check if the deposit amount is greater than 0
            self.balance += amount  # Add the deposit amount to the current balance
            print(f"Deposited ${amount:.2f}")  # Print a message confirming the deposit
            self.transaction_history.append(f"Deposited ${amount:.2f}")  # Record the deposit in the history
        else:
            print("Deposit amount must be positive.")  # Show an error message if the deposit amount is not positive

    def withdraw(self, amount):
        # Withdraw money if there are enough funds and record the withdrawal in the history
        if amount > 0:  # Check if the withdrawal amount is greater than 0
            if amount <= self.balance:  # Check if there is enough money in the balance
                self.balance -= amount  # Subtract the withdrawal amount from the current balance
                print(f"Withdrew ${amount:.2f}")  # Print a message confirming the withdrawal
                self.transaction_history.append(f"Withdrew ${amount:.2f}")  # Record the withdrawal in the history
            else:
                print("Insufficient funds.")  # Show an error message if there are not enough funds
        else:
            print("Withdrawal amount must be positive.")  # Show an error message if the withdrawal amount is not positive

    def change_pin(self, old_pin, new_pin):
        # Change the PIN if the old PIN is correct and the new PIN is a valid 4-digit number
        if old_pin == self.pin:  # Check if the old PIN entered matches the current PIN
            if len(new_pin) == 4 and new_pin.isdigit():  # Check if the new PIN is exactly 4 digits long and contains only numbers
                self.pin = new_pin  # Update the PIN to the new value
                print("PIN changed successfully.")  # Print a success message
                self.transaction_history.append("Changed PIN")  # Record the PIN change in the history
            else:
                print("New PIN must be a 4-digit number.")  # Show an error message if the new PIN is not valid
        else:
            print("Old PIN is incorrect.")  # Show an error message if the old PIN is incorrect

    def print_transaction_history(self):
        # Print out all the transactions or notify if there are no transactions
        if not self.transaction_history:  # Check if the transaction history is empty
            print("No transactions yet.")  # Show a message if there are no transactions
        else:
            for transaction in self.transaction_history:  # Loop through each transaction in the history
                print(transaction)  # Print each transaction

# Main loop to operate the ATM
if __name__ == "__main__":
    atm = ATM()  # Create an instance of the ATM class

    while True:
        # Display the menu options for the user
        print("\nATM Menu:")
        print("1. Check Balance")  # Option to check the balance
        print("2. Deposit")  # Option to deposit money
        print("3. Withdraw")  # Option to withdraw money
        print("4. Change PIN")  # Option to change the PIN
        print("5. View Transaction History")  # Option to view all transactions
        print("6. Exit")  # Option to exit the ATM
        
        # Get the user's choice from the menu
        choice = input("Enter your choice (1/2/3/4/5/6): ")  # Ask the user to enter their choice
        
        if choice == '1':
            atm.check_balance()  # Call the method to check the balance
        elif choice == '2':
            try:
                amount = float(input("Enter the amount to deposit: "))  # Ask the user to enter the deposit amount
                atm.deposit(amount)  # Call the method to deposit the entered amount
            except ValueError:
                print("Invalid amount. Please enter a number.")  # Show an error message if the input is not a number
        elif choice == '3':
            try:
                amount = float(input("Enter the amount to withdraw: "))  # Ask the user to enter the withdrawal amount
                atm.withdraw(amount)  # Call the method to withdraw the entered amount
            except ValueError:
                print("Invalid amount. Please enter a number.")  # Show an error message if the input is not a number
        elif choice == '4':
            old_pin = input("Enter your old PIN: ")  # Ask the user to enter their old PIN
            new_pin = input("Enter your new 4-digit PIN: ")  # Ask the user to enter a new 4-digit PIN
            atm.change_pin(old_pin, new_pin)  # Call the method to change the PIN
        elif choice == '5':
            atm.print_transaction_history()  # Call the method to print all transactions
        elif choice == '6':
            print("Thank you for using the ATM. Goodbye!")  # Print a goodbye message
            break  # Exit the loop and end the program
        else:
            print("Invalid choice. Please select a valid option.")  # Show an error message for invalid menu choices
