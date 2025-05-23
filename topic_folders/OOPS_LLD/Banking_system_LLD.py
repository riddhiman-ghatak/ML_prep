from abc import ABC, abstractmethod

# ----------------------------------------
# Simple Logger demonstrating duck typing
# ----------------------------------------
class Logger:
    """
    Simple logger class using duck typing.
    Any object with an 'info' method can be used in place of Logger.
    """
    def info(self, msg):
        print(f"[INFO] {msg}")

# ----------------------------------------
# Mixin for interest calculation
# ----------------------------------------
class InterestMixin:
    """
    Provides a method to calculate interest based on balance and interest_rate.
    Used via multiple inheritance in SavingsAccount.
    """
    def calculate_interest(self):
        # interest = balance * (interest_rate / 100)
        return self.balance * (self.interest_rate / 100)

# ----------------------------------------
# Abstract Base Account Class
# ----------------------------------------
class Account(ABC):
    # Class variable to keep track of how many Account instances are created
    _account_count = 0

    def __init__(self, owner, balance=0):
        """
        Constructor (Encapsulation):
         - 'owner' is a public attribute
         - '_balance' is a private attribute with controlled access via property
         - 'logger' demonstrates composition (Account has a Logger)
        """
        self.owner = owner
        self._balance = balance
        Account._account_count += 1
        self.logger = Logger()

    # ----------------------------------------
    # Encapsulation with @property
    # ----------------------------------------
    @property
    def balance(self):
        """
        Getter for private attribute _balance.
        """
        return self._balance

    @balance.setter
    def balance(self, amount):
        """
        Setter for _balance with validation.
        Prevents setting a negative balance.
        """
        if amount < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = amount

    # ----------------------------------------
    # Class method: operates on class rather than instance
    # ----------------------------------------
    @classmethod
    def get_account_count(cls):
        """
        Returns the total number of Account instances created.
        """
        return cls._account_count

    # ----------------------------------------
    # Static method: utility function not bound to class/instance state
    # ----------------------------------------
    @staticmethod
    def validate_amount(amount):
        """
        Ensures amount is positive. Used in deposit/withdraw methods.
        """
        if amount <= 0:
            raise ValueError("Amount must be positive")

    # ----------------------------------------
    # Abstract method: must be overridden by subclasses
    # ----------------------------------------
    @abstractmethod
    def withdraw(self, amount):
        """
        Withdraw method to be implemented by each account type.
        """
        pass

    # ----------------------------------------
    # Concrete method: available to all subclasses
    # ----------------------------------------
    def deposit(self, amount):
        """
        Deposits money into the account after validation.
        Logs the operation.
        """
        Account.validate_amount(amount)         # Static method call
        self._balance += amount                # Directly update private attribute
        self.logger.info(
            f"Deposited {amount}. New balance: {self._balance}"
        )  # Composition use of Logger

    # ----------------------------------------
    # Operator Overloading: define custom behavior for '+'.
    # ----------------------------------------
    def __add__(self, other):
        """
        Allows adding two Account objects to get combined balance.
        Returns total balance of both accounts.
        """
        if not isinstance(other, Account):
            return NotImplemented
        return self.balance + other.balance

    def __str__(self):
        """
        String representation of Account for easy printing.
        """
        return f"Account(owner={self.owner}, balance={self.balance})"

# ----------------------------------------
# SavingsAccount with Interest Mixin
# ----------------------------------------
class SavingsAccount(Account, InterestMixin):
    """
    Savings account supporting interest calculation.
    Inherits from Account and InterestMixin (multiple inheritance).
    """
    def __init__(self, owner, balance=0, interest_rate=3.5):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate  # Public attribute specific to savings

    def withdraw(self, amount):
        """
        Withdraw money if sufficient balance.
        Validates amount and prevents overdraft.
        """
        Account.validate_amount(amount)
        if amount > self._balance:
            raise ValueError("Insufficient funds in savings")
        self._balance -= amount
        self.logger.info(
            f"Withdrew {amount}. New balance: {self._balance}"
        )

# ----------------------------------------
# CurrentAccount with Overdraft Facility
# ----------------------------------------
class CurrentAccount(Account):
    """
    Current account supporting overdraft up to a limit.
    """
    def __init__(self, owner, balance=0, overdraft_limit=500):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        """
        Withdraw money within balance + overdraft limit.
        Validates amount and rejects if overdraft exceeded.
        """
        Account.validate_amount(amount)
        if amount > self._balance + self.overdraft_limit:
            raise ValueError("Overdraft limit exceeded")
        self._balance -= amount
        self.logger.info(
            f"Withdrew {amount}. New balance: {self._balance}"
        )

# ----------------------------------------
# Customer demonstrating composition/aggregation
# ----------------------------------------
class Customer:
    """
    A customer can hold multiple accounts.
    Demonstrates aggregation: Customer 'has' Accounts.
    """
    def __init__(self, name):
        self.name = name
        self.accounts = []  # List to aggregate Account instances

    def open_account(self, account: Account):
        """
        Adds an Account to this Customer's portfolio.
        Prints confirmation.
        """
        self.accounts.append(account)
        print(f"Account opened for {self.name}: {account}")

    def total_balance(self):
        """
        Calculates total balance across all owned accounts.
        Demonstrates polymorphism: uses .balance property uniformly.
        """
        return sum(acc.balance for acc in self.accounts)

# ----------------------------------------
# Example Usage (Demonstrates all OOP Concepts)
# ----------------------------------------
if __name__ == "__main__":
    # Create a customer
    cust = Customer("Alice")

    # Open a savings and a current account
    sav = SavingsAccount("Alice", balance=1000)
    cur = CurrentAccount("Alice", balance=500)

    # Aggregate accounts under customer
    cust.open_account(sav)
    cust.open_account(cur)

    # Deposit into savings
    sav.deposit(200)        # Uses Account.deposit()
    sav.withdraw(150)       # Uses overridden withdraw()
    print(f"Savings interest: {sav.calculate_interest()}")  # From InterestMixin

    # Withdraw from current (demonstrates overdraft)
    cur.withdraw(300)

    # Polymorphic total balance across accounts
    print(f"Total balance for {cust.name}: {cust.total_balance()}")

    # Operator overloading: add two accounts directly
    print(f"Combined balance via + operator: {sav + cur}")

    # Class method shows how many accounts exist
    print(f"Total accounts created: {Account.get_account_count()}")
