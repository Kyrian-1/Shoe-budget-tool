# Shoe Budget Tool
# This is a simple Python script to help track and manage a budget for buying shoes.
# It allows setting a monthly budget, adding shoe purchases, checking remaining budget,
# and getting a summary.

class ShoeBudgetTool:
    def __init__(self, monthly_budget=0.0):
        self.monthly_budget = monthly_budget
        self.purchases = []  # List to store purchase amounts
        self.total_spent = 0.0

    def set_budget(self, budget):
        """Set or update the monthly budget."""
        self.monthly_budget = budget
        print(f"Monthly budget set to ${budget:.2f}")

    def add_purchase(self, amount, description=""):
        """Add a shoe purchase to the tracker."""
        if amount <= 0:
            print("Purchase amount must be positive.")
            return
        self.purchases.append((amount, description))
        self.total_spent += amount
        print(f"Added purchase: ${amount:.2f} ({description})")

    def get_remaining_budget(self):
        """Calculate and return the remaining budget."""
        remaining = self.monthly_budget - self.total_spent
        return max(remaining, 0.0)  # Ensure non-negative

    def get_summary(self):
        """Print a summary of the budget and purchases."""
        print("\n--- Shoe Budget Summary ---")
        print(f"Monthly Budget: ${self.monthly_budget:.2f}")
        print(f"Total Spent: ${self.total_spent:.2f}")
        print(f"Remaining Budget: ${self.get_remaining_budget():.2f}")
        if self.total_spent > self.monthly_budget:
            print("Warning: You are over budget!")
        print("\nPurchases:")
        for i, (amount, desc) in enumerate(self.purchases, 1):
            print(f"{i}. ${amount:.2f} ({desc})")
        print("---------------------------\n")

# Example usage:
if __name__ == "__main__":
    tool = ShoeBudgetTool()
    
    # Interactive mode
    print("Welcome to the Shoe Budget Tool!")
    budget = float(input("Enter your monthly shoe budget: $"))
    tool.set_budget(budget)
    
    while True:
        action = input("\nWhat would you like to do? (add/summary/quit): ").lower()
        if action == "add":
            amount = float(input("Enter purchase amount: $"))
            desc = input("Enter description (optional): ")
            tool.add_purchase(amount, desc)
        elif action == "summary":
            tool.get_summary()
        elif action == "quit":
            tool.get_summary()
            print("Goodbye!")
            break
        else:
            print("Invalid action. Try 'add', 'summary', or 'quit'.")
