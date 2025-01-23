# this is just beatiful !!
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? Small (S), Medium (M), or Large (L): ").upper()
pepperoni = input("Do you want pepperoni on your pizza? (Y/N): ").upper()
extra_cheese = input("Do you want extra cheese? (Y/N): ").upper()

# Set the base prices for different sizes
prices = {"S": 15, "M": 20, "L": 25}
bill = prices.get(size, 0)

if bill == 0:
    print("Invalid pizza size!")
else:
    # Add pepperoni price
    bill += 2 if pepperoni == "Y" and size == "S" else 3 if pepperoni == "Y" else 0

    # Add extra cheese
    bill += 1 if extra_cheese == "Y" else 0

    # Print final bill
    print(f"Your final bill is: ${bill}.")
