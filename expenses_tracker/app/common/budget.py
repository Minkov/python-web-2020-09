def calculate_budget_left(profile, expenses):
    expenses_cost = sum(expense.price for expense in expenses)
    return profile.budget - expenses_cost
