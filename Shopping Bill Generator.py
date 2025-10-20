def generate_bill(*prices):
    # Calculate the total amount
    total_amount = sum(prices)

    # Calculate the tax (5%)
    tax = total_amount * 0.05

    # Calculate the grand total
    grand_total = total_amount + tax

    # Return the total amount, tax, and grand total as a tuple
    return total_amount, tax, grand_total


# Example usage:
prices = list(map(float, input("Enter prices separated by space: ").split()))
total_amount, tax, grand_total = generate_bill(*prices)
print(f"Total Amount: {total_amount:.2f}")
print(f"Tax (5%): {tax:.2f}")
print(f"Grand Total: {grand_total:.2f}")