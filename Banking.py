class BankAccount:
    def __init__(self, bank_name, acc_no, name, pin, balance=0):
        self.bank_name = bank_name
        self.acc_no = acc_no
        self.name = name
        self.__pin = pin
        self._balance = balance
        self.transactions = []

    def authenticate(self, pin):
        return self.__pin == pin

    def deposit(self, amount):
        self._balance += amount
        self.transactions.append(f"Deposited ₹{amount}")
        print(f"₹{amount} deposited successfully")

    def withdraw(self, amount, pin):
        if not self.authenticate(pin):
            print("Invalid PIN")
            return

        if amount > self._balance:
            print("Insufficient Balance")
        else:
            self._balance -= amount
            self.transactions.append(f"Withdraw ₹{amount}")
            print(f"₹{amount} withdrawn successfully")

    def transfer(self, receiver, amount, pin):
        if not self.authenticate(pin):
            print("Invalid PIN")
            return

        if amount > self._balance:
            print("Insufficient Balance")
            return

        self._balance -= amount
        receiver._balance += amount

        self.transactions.append(
            f"Transferred ₹{amount} to {receiver.name}"
        )
        receiver.transactions.append(
            f"Received ₹{amount} from {self.name}"
        )

        print("Transfer Successful")

    def check_balance(self, pin):
        if self.authenticate(pin):
            print(f"Balance: ₹{self._balance}")
        else:
            print("Invalid PIN")

    def show_transactions(self):
        print("\nTransaction History")
        for t in self.transactions:
            print(t)


# Inheritance
class SavingsAccount(BankAccount):
    def add_interest(self, rate):
        interest = self._balance * rate / 100
        self._balance += interest
        print(f"Interest Added: ₹{interest}")


class CurrentAccount(BankAccount):
    def __init__(self, bank_name, acc_no, name, pin,
                 balance=0, overdraft=5000):
        super().__init__(
            bank_name, acc_no, name, pin, balance
        )
        self.overdraft = overdraft

    def withdraw(self, amount, pin):
        if not self.authenticate(pin):
            print("Invalid PIN")
            return

        if amount > self._balance + self.overdraft:
            print("Overdraft Limit Exceeded")
        else:
            self._balance -= amount
            print(f"₹{amount} withdrawn successfully")


# Driver Code
acc1 = SavingsAccount("SBI", 101, "Dhanush", 1234, 10000)

acc2 = CurrentAccount("HDFC", 102, "Rahul", 5678, 5000)

acc3 = SavingsAccount("ICICI", 103, "Deepu", 1111, 15000)

acc4 = CurrentAccount("Axis", 104, "Kiran", 2222, 8000)

acc5 = SavingsAccount("Canara", 105, "Ravi", 3333, 20000)

accounts = [acc1, acc2, acc3, acc4, acc5]

for acc in accounts:
    print(f"{acc.name} ")
