import tkinter as tk

class ExpenseTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")
        self.root.geometry("300x200")

        self.expenses = []

        # Labels and Input Fields
        tk.Label(root, text="Amount:").grid(row=0, column=0, padx=5, pady=5)
        self.amount_entry = tk.Entry(root)
        self.amount_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(root, text="Category:").grid(row=1, column=0, padx=5, pady=5)
        self.category_entry = tk.Entry(root)
        self.category_entry.grid(row=1, column=1, padx=5, pady=5)

        # Buttons
        tk.Button(root, text="Add Expense", command=self.add_expense).grid(row=2, column=0, columnspan=2, pady=5)
        tk.Button(root, text="View Total", command=self.view_total).grid(row=3, column=0, columnspan=2, pady=5)

        # Output Label
        self.output_label = tk.Label(root, text="Total: $0.00", font=("Arial", 12))
        self.output_label.grid(row=4, column=0, columnspan=2, pady=10)

    def add_expense(self):
        try:
            amount = float(self.amount_entry.get())
            category = self.category_entry.get().strip()
            if category:
                self.expenses.append((amount, category))
                self.amount_entry.delete(0, tk.END)
                self.category_entry.delete(0, tk.END)
                self.output_label.config(text="Expense Added!")
            else:
                self.output_label.config(text="Enter a category!")
        except ValueError:
            self.output_label.config(text="Invalid Amount")

    def view_total(self):
        total = sum(exp[0] for exp in self.expenses)
        self.output_label.config(text=f"Total: ${total:.2f}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTracker(root)
    root.mainloop()
