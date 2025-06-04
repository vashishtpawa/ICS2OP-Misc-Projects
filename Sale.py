# Sale.py
# ICS201 Vashisht
# January 10, 2021

print("Laptops are 20% off on Black Friday!")
originalPrice = float(input("Enter a price to find your discount now! "))

discountedPrice = originalPrice * 0.8
amountSaved = originalPrice * 0.2

print("\nOriginal Price: $%.2f" %originalPrice)
print("Discounted Price: $%.2f" %discountedPrice)
print("Amount Saved: $%.2f" %amountSaved)
