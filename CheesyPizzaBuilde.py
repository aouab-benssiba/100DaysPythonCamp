print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? small type: S, Medium type M or Large type L: ")
if size == "S":
    pepperoni = input("Do you want 2$ pepperoni on your pizza? Y or N: ")
    bill = 15
    if pepperoni == "Y":
        bill += 2
        extra_cheese = input("Do you want 1$ extra cheese? Y or N: ")
        if extra_cheese == "Y":
            bill += 1
            print(f"Your final bill is: ${bill}.")
        else:
            print(f"Your final bill is: ${bill}.")
    else:
        extra_cheese = input("Do you want 1$ extra cheese? Y or N: ")
        if extra_cheese == "Y":
            bill += 1
            print(f"Your final bill is: ${bill}.")
        else:
            print(f"Your final bill is: ${bill}.")



elif size == "M":
    bill = 20
    pepperoni = input("Do you want 2$ pepperoni on your pizza? Y or N: ")
    if pepperoni == "Y":
        bill += 3
        extra_cheese = input("Do you want 1$ extra cheese? Y or N: ")
        if extra_cheese == "Y":
            bill += 1
            print(f"Your final bill is: ${bill}.")
        else:
            print(f"Your final bill is: ${bill}.")

    else:
        extra_cheese = input("Do you want 1$ extra cheese? Y or N: ")
        if extra_cheese == "Y":
            bill += 1
            print(f"Your final bill is: ${bill}.")
        else:
            print(f"Your final bill is: ${bill}.")

else:
    bill = 25
    extra_cheese = input("Do you want 1$ extra cheese? Y or N: ")
    if extra_cheese == "Y":
        bill += 1
        print(f"Your final bill is: ${bill}.")
    else:
        print(f"Your final bill is: ${bill}.")
