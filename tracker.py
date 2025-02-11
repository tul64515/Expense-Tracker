def main():
    expenses = []
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Total")
        print("3. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            amount = float(input("Enter expense amount: "))
            category = input("Enter category: ")
            expenses.append((amount, category))
            print("Expense added!")
        
        elif choice == '2':
            total = sum(expense[0] for expense in expenses)
            print(f"Total expenses: ${total:.2f}")
        
        elif choice == '3':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
