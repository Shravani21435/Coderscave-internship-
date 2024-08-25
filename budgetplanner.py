class BudgetPlanner:
    def __init__(self):
        self.income = 0
        self.expenses = 0
        self.expense_details = []

    def add_income(self, amount):
        self.income += amount
        print(f"Added income: ${amount:.2f}")

    def add_expense(self, description, amount):
        self.expenses += amount
        self.expense_details.append((description, amount))
        print(f"Added expense: {description} - ${amount:.2f}")

    def view_balance(self):
        balance = self.income - self.expenses
        print(f"\nIncome: ${self.income:.2f}")
        print(f"Total Expenses: ${self.expenses:.2f}")
        print(f"Balance: ${balance:.2f}\n")

    def view_expense_details(self):
        print("\nExpense Details:")
        for description, amount in self.expense_details:
            print(f"{description}: ${amount:.2f}")
        print("\n")


def main():
        planner = BudgetPlanner()

        while True:
            print("1. Add Income")
            print("2. Add Expense")
            print("3. View Balance")
            print("4. View Expense Details")
            print("5. Exit")

            choice = input("Choose an option: ")

            if choice == '1':
                amount = float(input("Enter income amount: $"))
                planner.add_income(amount)

            elif choice == '2':
                description = input("Enter expense description: ")
                amount = float(input("Enter expense amount: $"))
                planner.add_expense(description, amount)

            elif choice == '3':
                planner.view_balance()

            elif choice == '4':
                planner.view_expense_details()

            elif choice == '5':
                print("Exiting Budget Planner. Goodbye!")
                break

            else:
                print("Invalid option. Please choose again.\n")


if __name__ == "__main__":
    main()

