class Chair:
    def __init__(self, color, material, size):
        self.color = color
        self.material = material
        self.size = size

    def sit(self):
        print(f"You've sat down")

    def get_up(self):
        print(f"You've gotten up")

    def describe(self):
        print(
            f"The chair is made of {self.material}, is {self.color} in color, and is {self.size} in size.")


chair1 = Chair("red", "wood", "medium")
chair1.describe()
chair2 = Chair("blue", "plastic", "small")
chair2.describe()


class BankAccount:
    def __init__(self, holder, balance):
        self.holder = holder
        self.__balance = balance

    def deposit(self):
        try:
            amount = float(input("Enter the amount you want to deposit: $"))

            if amount <= 0:
                print("The deposit amount must be greater than zero.")
            else:
                self.__balance += amount
                print(f"You successfully deposited ${amount:.2f}.")

        except ValueError:
            print("Please enter a valid number.")

    def withdraw(self):
        try:
            amount = float(input("Enter the amount you want to withdraw: $"))

            if amount <= 0:
                print("The withdrawal amount must be greater than zero.")
            elif amount > self.__balance:
                print("You do not have enough balance.")
            else:
                self.__balance -= amount
                print(f"You successfully withdrew ${amount:.2f}.")

        except ValueError:
            print("Please enter a valid number.")

    def check_balance(self):
        print(f"Your current balance is ${self.__balance:.2f}")


holder1 = BankAccount("Raul Perez", 5000)

print(holder1.holder)
holder1.check_balance()

holder1.deposit()
holder1.withdraw()

holder1.check_balance()
