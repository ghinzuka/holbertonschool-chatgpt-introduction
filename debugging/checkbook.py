#!/usr/bin/python3
class Checkbook:
    """
    Represents a simple checkbook allowing deposits,
    withdrawals, and balance checks.
    """

    def __init__(self):
        """
        Initializes the Checkbook with a balance of $0.0.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposits the specified amount into the checkbook.

        Args:
            amount (float): The amount to deposit.

        Raises:
            ValueError: If the specified amount is not a valid numeric value.
        """
        try:
            amount = float(amount)
        except ValueError:
            print("Invalid amount. Please enter a valid numeric value.")
            return
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraws the specified amount from the checkbook.

        Args:
            amount (float): The amount to withdraw.

        Raises:
            ValueError: If the specified amount is not a valid numeric value.
        """
        try:
            amount = float(amount)
        except ValueError:
            print("Invalid amount. Please enter a valid numeric value.")
            return
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Prints the current balance of the checkbook.
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """
    Provides a command-line interface for
    interacting with the Checkbook object.
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, "
                       "balance, exit): ")
        if action.lower() == 'exit':
            break
        elif action.lower() == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
            except ValueError:
                print("Invalid amount. Please enter a valid numeric value.")
                continue
            cb.deposit(amount)
        elif action.lower() == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
            except ValueError:
                print("Invalid amount. Please enter a valid numeric value.")
                continue
            cb.withdraw(amount)
        elif action.lower() == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
