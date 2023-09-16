class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__account_balance}")
        else:
            print("Invalid deposit amount. Please deposit a positive amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__account_balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def display_balance(self):
        print(f"Account Balance for {self.__account_holder_name} (Account #{self.__account_number}): ${self.__account_balance}")


# Testing the BankAccount class
if __name__ == "__main__":
    # Create a new BankAccount instance
    my_account = BankAccount(account_number="123456", account_holder_name="John Doe", initial_balance=1000)

    # Display the initial balance
    my_account.display_balance()

    # Deposit money
    my_account.deposit(500)

    # Withdraw money
    my_account.withdraw(200)

    # Try to withdraw more money than the balance
    my_account.withdraw(1500)

    # Display the updated balance
    my_account.display_balance()

