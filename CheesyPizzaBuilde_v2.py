print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? small type: S, Medium type M or Large type L: ")
pepperoni = input("Do you want 2$ pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want 1$ extra cheese? Y or N: ")
bill = 0

## ask about size
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("wrong input!")

## ask about pepperoni
if pepperoni == "Y":
    if size == "S":
        bill += 2
    elif size == "M":
        bill += 3




## give final bill if they wanted cheese
if extra_cheese == "Y":
    if size == "S" or size == "M" or size == "L":
        bill += 1
        print(f"Your final bill is: ${bill}.")
else:
    print(f"Your final bill is: ${bill}.")
