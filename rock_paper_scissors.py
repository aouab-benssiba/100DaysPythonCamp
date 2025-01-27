import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
try:
    choice = int(input("What do you choose, 0 for rock, 1 for paper, 2 for scissors\n  "))
    if choice < 0 or choice > 2:
        raise ValueError("you should enter only 0 or 1 or 2")
except ValueError as e:
    print(f"Error: {e}")

    exit()

game_moves = [rock, paper, scissors]

computer_choice = random.choice(game_moves)

# displaying moves:

print("Your choice:\n" + game_moves[choice] + "\n")
print(f"computer\'s choice:\n{computer_choice}")


if choice == 0 and computer_choice == 2:
    print("you have won")

elif choice == 1 and computer_choice == 0:
    print("you have won")

elif choice == 2 and computer_choice == 1:
    print("you have won")

elif game_moves[choice] == computer_choice:
    print("it\'a draw")
else:
    print("you have lost")
