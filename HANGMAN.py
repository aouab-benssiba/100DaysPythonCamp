import random
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
'''] # length 7

word_dic =  {
    "cooking": ["spoon", "knife", "oven", "grill", "frying", "baking", "whisk", "stir", "boil", "recipe"],
    "math": ["algebra", "geometry", "calculus", "integer", "vector", "equation", "matrix", "derivative", "sum", "average"],
    "physics": ["gravity", "momentum", "friction", "energy", "force", "mass", "velocity", "quantum", "magnetism", "relativity"],
    "technology": ["computer", "keyboard", "software", "hardware", "network", "algorithm", "cloud", "server", "router", "monitor"],
    "biology": ["cell", "organism", "genome", "protein", "mitosis", "enzyme", "ecosystem", "evolution", "photosynthesis", "chromosome"],
    "space": ["galaxy", "planet", "asteroid", "orbit", "telescope", "comet", "nebula", "satellite", "cosmos", "meteor"],
    "sports": ["football", "basketball", "tennis", "cycling", "running", "cricket", "golf", "wrestling", "boxing", "swimming"],
    "music": ["piano", "guitar", "violin", "drums", "melody", "rhythm", "symphony", "composer", "chord", "harmony"],
    "literature": ["novel", "poem", "author", "plot", "genre", "chapter", "protagonist", "drama", "narrative", "poetry"],
    "travel": ["passport", "ticket", "flight", "journey", "destination", "luggage", "guidebook", "adventure", "tourism", "itinerary"]
}
def life_check():
    if lives == lives_max - 1:
        print(stages[6])
    elif lives == lives_max - 2:
        print(stages[5])
    elif lives == lives_max - 3:
        print(stages[4])
    elif lives == lives_max - 4:
        print(stages[3])
        print("Hint!\n")
        print(f"The hangman did {random_category} in his life!!")
    elif lives == lives_max - 5:
        print(stages[2])
    elif lives == lives_max - 6:
        print(stages[1])
    elif lives == lives_max - 7:
        print(stages[0])
    print(blank)

random_category = random.choice(list(word_dic.keys()))

chosen_word = random.choice(word_dic[random_category])
blank = ""

for char in chosen_word:
    blank += "_"
print(blank)
blank_list = list(blank)
lives = 0
for i in chosen_word:
    lives += 1
indexes = []
lives_max = lives

while lives != 0:
    guess_letter = str(input("please guess a letter:\n  ")).lower()
    # if we had guessed the word then the for loop is done
    if blank == chosen_word:
        break
    elif guess_letter in chosen_word:
        # taking the index of the guessed letter
        for index in range(len(chosen_word)):
            if chosen_word[index] == guess_letter:
                indexes.append(index)
        # assigning the guess letter to the blank_list
        # and checking if we already did it
        # if so we assign to the next index the guess letter
        if len(indexes) >= 2:
            index1, index2 = indexes[0], indexes[1]
            # checking if you already typed the letter
            if blank_list[index1] == guess_letter and blank_list[index2] == guess_letter:
                life_check()
                print(f"you have already typed {guess_letter}\n")
                lives -= 1
            elif blank_list[index1] != guess_letter:
                print("Right")
                blank_list[index1] = guess_letter
            elif blank_list[index1] == guess_letter:
                print("Right")
                blank_list[index2] = guess_letter

            indexes = []
        elif 1 <= len(indexes) < 2:
            index1 = indexes[0]
            # check if had already typed the guess_letter
            if blank_list[index1] != guess_letter:
                blank_list[index1] = guess_letter
                print("Right")
            else:
                lives -= 1
                life_check()
                print(f"you have already typed {guess_letter}\n")
            indexes = []
        # Updating the blank word
        blank = ""
        for letter in blank_list:
            blank += letter
        print(blank)
        print(f"****************************{lives}/{lives_max}LIVES LEFT****************************\n")
    else:
        lives -= 1
        life_check()
        print("Wrong\n")
        print(f"****************************{lives}/{lives_max}LIVES LEFT****************************\n")


if blank == chosen_word:
    print("You have won!!\nHangman is Alive!!")
    print("the word you have guessed: " + chosen_word)
else:
    print(stages[0])
    print("You have lost!\nHangman is Dead!!")
    print("the word you didn\'t guess: " + chosen_word)
