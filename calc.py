subtotal = float(input("Enter the bill amount: ₹"))
tax_rate = float(input("Enter tax percentage: "))

tax = subtotal * tax_rate / 100
total = subtotal + tax

print("\n--- Bill Summary ---")
print(f"Subtotal: ₹{subtotal:.2f}")
print(f"Tax:      ₹{tax:.2f}")
print(f"Total:    ₹{total:.2f}")
