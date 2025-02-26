logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)

name = str(input("what\'s is your name? ")).lower()
bid = int(input("how much would you bid?: $"))
other_bidders = str(input("Are there any other bidders? [Y/N]\n  ")).lower()

data = {
    name: bid,
}

while other_bidders != "n":
    if other_bidders != "y":
        break
    name = str(input("what\'s is your name? ")).lower()
    bid = int(input("how much would you bid?: $"))
    other_bidders = str(input("Are there any other bidders? [Y/N]\n  ")).lower()
    data[name] = bid

import os
os.system("cls")

max_bid = 0
for key in data:
    if data[key] >= max_bid:
        max_bid = data[key]
        winner_name = key

print(f"the winner is {winner_name} with a bid of ${max_bid}")
