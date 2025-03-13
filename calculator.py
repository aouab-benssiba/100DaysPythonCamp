import operator
print(r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
""")
# Mapping operators to functions
ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "**": operator.pow
}

def calculation(first_num, second_num):
    return ops[op](first_num, second_num)

number_one = int(input("what\'s the first number?: "))

while True:

    op = input("+\n-\n*\n/\nPick an operation: ")

    number_two = int(input("What\'s the next number?: "))

    result = calculation(number_one, number_two)

    print(f"{number_one} {op} {number_two} = {result}")

    again = str(input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation, or to leave type 'q': "))
    if again == 'y':
        number_one = result
        continue
    elif again == "q":
        break
    else:
        number_one = int(input("what\'s the first number?: "))
        continue
