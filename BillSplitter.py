# this is a programm that give you a total bill after a given precentage tip, and the amount of people that are welling to pay it
print("Welcome to the tip calculator!\n")
bill = float(input("What was the total bill? $\n\n"))
tip = int(input("What percentage tip would you like to give? 10 12 15 \n\n"))
people = int(input("How many people to split the bill? \n\n"))

tip_percentage = tip / 100 # if 12% then 0.12
total_tip = (bill * (1 + tip_percentage))
calculation = total_tip / people
rounded_calculation = round(calculation, 2)

print(f"Each person should pay: {rounded_calculation}" )

