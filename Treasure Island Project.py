print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
First_choice = input("you want to move your boat to right[r] or left[l]?  ")
if First_choice == "l":
    print("you have reached the shore of the Treasure Island!\nbut your boat is broken!")
    Second_choice = input("you want to jump to water and swim[s] or wait[w]?  ")
    if Second_choice == "w":
        print("You have found another boat and landed into the Island!\nthen you have entered into a cave!")
        Third_choice = input("which door would you open, red[r] or blue[b] or yellow[y]  ")
        if Third_choice == "r":
            print("a Dragon was behind the door\nyou have been Burned by fire!\nGame Over.")
        elif Third_choice == "b":
            print("a wolf pack was behind the door!\nyou have been Eaten by beasts!\nGame Over.")
        elif Third_choice == "y":
            print("Congratulations\nyou have beaten the Game!")
        else:
            print("Game Over.")
    else:
        print("Attacked by trout!\nGame Over!")
else:
    print("you Fall into a hole.\nGame Over!!")
