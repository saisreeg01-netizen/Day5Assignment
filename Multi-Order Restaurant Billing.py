def restaurant_bill(customer, *items, **charges):
    print(f"Customer: {customer}")
    print("Items Ordered:")
    total = sum(items)
    for item in items:
        print(f"- {item}")

    print("\nExtra Charges:")
    for charge, amount in charges.items():
        print(f"- {charge}: {amount}")
        total += amount

    print(f"\nTotal Amount: {total:.2f}")


# Example usage:
restaurant_bill("John Doe", 15.99, 8.99, 4.99, Tax=2.00, Service_Charge=5.00, Tip=3.00)

