def calculate_discount(amount):
    if amount > 5000:
        discount = 0.20  # 20% discount
    elif amount > 2000:
        discount = 0.10  # 10% discount
    else:
        discount = 0.00  # No discount

    final_amount = amount - (amount * discount)
    return final_amount

# Example usage:
amount = float(input("Enter the purchase amount: "))
final_amount = calculate_discount(amount)
print("Final amount after discount: ", final_amount)