import csv
import os

FILE_NAME = "expenses.csv"


# Function to add a new expense
def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (Food, Travel, Shopping, Bills etc): ")
    description = input("Enter description: ")
    amount = input("Enter amount: ")

    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)

        # Write header if file is empty
        if file.tell() == 0:
            writer.writerow(["Date", "Category", "Description", "Amount"])

        writer.writerow([date, category, description, amount])

    print("\nExpense added successfully!\n")


# Function to view all expenses
def view_expenses():
    if not os.path.exists(FILE_NAME):
        print("\nNo expenses found.\n")
        return

    print("\n------ Expense List ------\n")

    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)

        for row in reader:
            print(row)

    print()


# Function to show total summary
def show_summary():
    total = 0

    if not os.path.exists(FILE_NAME):
        print("\nNo expenses recorded.\n")
        return

    with open(FILE_NAME, mode='r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            total += float(row["Amount"])

    print("\nTotal Expenses =", total)
    print()


# Main program menu
def main():

    while True:

        print("======== Expense Tracker ========")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Expense Summary")
        print("4. Exit")
        print("=================================")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            show_summary()

        elif choice == "4":
            print("\nExiting Expense Tracker... Goodbye!")
            break

        else:
            print("\nInvalid choice. Please try again.\n")


# Run the program
if __name__ == "__main__":
    main()