class Account:
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self.balance = float(balance)

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        return self.balance

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        return self.balance

    def transfer_to(self, target: "Account", amount: float):
        if self is target:
            raise ValueError("Cannot transfer to the same account.")
        self.withdraw(amount)
        target.deposit(amount)
        return self.balance

    def __str__(self):
        return f"{self.owner}: ${self.balance:.2f}"


class Transaction:
    def __init__(self, employee_name: str, source_account: Account):
        self.employee_name = employee_name
        self.source_account = source_account

    def execute(self, amount: float, target_account: Account = None):
        raise NotImplementedError("Subclasses must override execute()")

    def receipt(self, amount: float, currency: str = "USD", note: str = None) -> str:
        """
        Demonstrates method overloading by accepting:
        - receipt(amount)
        - receipt(amount, currency)
        - receipt(amount, currency, note)
        """
        result = f"{self.employee_name} processed ${amount:.2f} {currency}."
        if note:
            result += f" Note: {note}."
        return result

    def summary(self, action: str, amount: float, target_account: Account = None) -> str:
        if target_account:
            return (
                f"Employee {self.employee_name} {action} ${amount:.2f} "
                f"from {self.source_account.owner} to {target_account.owner}."
            )
        return f"Employee {self.employee_name} {action} ${amount:.2f} for {self.source_account.owner}."


class Deposit(Transaction):
    def execute(self, amount: float, target_account: Account = None):
        if target_account is not None:
            raise ValueError("Deposit does not accept a target account.")
        self.source_account.deposit(amount)
        print(self.summary("deposited", amount))
        print(self.receipt(amount, note="Deposit completed"))


class Withdrawal(Transaction):
    def execute(self, amount: float, target_account: Account = None):
        if target_account is not None:
            raise ValueError("Withdrawal does not accept a target account.")
        self.source_account.withdraw(amount)
        print(self.summary("withdrew", amount))
        print(self.receipt(amount, note="Withdrawal completed"))


class Transfer(Transaction):
    def execute(self, amount: float, target_account: Account = None):
        if target_account is None:
            raise ValueError("Transfer requires a target account.")
        self.source_account.transfer_to(target_account, amount)
        print(self.summary("transferred", amount, target_account))
        print(self.receipt(amount, note=f"Transfer to {target_account.owner}"))


if __name__ == "__main__":
    # Create example accounts
    checking = Account("Checking", 1000.0)
    savings = Account("Savings", 500.0)

    employee = "Alex"

    print("Before transactions:")
    print(checking)
    print(savings)
    print("\n---\n")

    # Deposit funds using the Deposit subclass (method overriding)
    deposit_transaction = Deposit(employee, checking)
    deposit_transaction.execute(200.0)
    print("\n---\n")

    # Withdraw funds using the Withdrawal subclass (method overriding)
    withdrawal_transaction = Withdrawal(employee, checking)
    withdrawal_transaction.execute(150.0)
    print("\n---\n")

    # Transfer funds using the Transfer subclass (method overriding)
    transfer_transaction = Transfer(employee, checking)
    transfer_transaction.execute(100.0, savings)
    print("\n---\n")

    print("After transactions:")
    print(checking)
    print(savings)
