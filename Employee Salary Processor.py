def calculate_salary(base_salary, bonus=0, tax_rate=10):
    # Calculate the total salary (base salary + bonus)
    total_salary = base_salary + bonus

    # Calculate the tax amount
    tax_amount = (total_salary * tax_rate) / 100

    # Calculate the net salary (total salary - tax amount)
    net_salary = total_salary - tax_amount

    # Return the net salary
    return net_salary


# Example usage:
base_salary = float(input("Enter the base salary: "))
bonus = float(input("Enter the bonus (default=0): ") or 0)
tax_rate = float(input("Enter the tax rate (default=10): ") or 10)

net_salary = calculate_salary(base_salary, bonus, tax_rate)
print(f"Net Salary: {net_salary:.2f}")