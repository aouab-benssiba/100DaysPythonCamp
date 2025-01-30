import random
word_list =  [
    "apple", "banana", "grape", "orange", "mango", "pear", "kiwi", "peach", "plum", "cherry",
    "carrot", "tomato", "cucumber", "spinach", "broccoli", "lettuce", "onion", "garlic", "potato", "celery",
    "elephant", "giraffe", "tiger", "lion", "zebra", "panda", "monkey", "kangaroo", "bear", "wolf",
    "sunflower", "rose", "daisy", "tulip", "orchid", "lily", "violet", "lilac", "hibiscus", "cactus",
    "computer", "laptop", "keyboard", "monitor", "mouse", "tablet", "phone", "camera", "headphone", "charger",
    "book", "notebook", "pen", "pencil", "eraser", "marker", "sharpener", "scissors", "ruler", "glue",
    "mountain", "river", "ocean", "forest", "desert", "island", "lake", "hill", "valley", "cliff",
    "airport", "train", "bus", "car", "bicycle", "skateboard", "motorcycle", "truck", "helicopter", "submarine",
    "doctor", "teacher", "engineer", "scientist", "artist", "writer", "actor", "musician", "dancer", "chef",
    "computer", "network", "internet", "database", "program", "algorithm", "software", "hardware", "cloud", "server",
    "peace", "harmony", "love", "friendship", "family", "joy", "hope", "dream", "faith", "trust"
]


chosen_word = random.choice(word_list)
blank = ""

for char in chosen_word:
    blank += "_"
print(blank)
blank_list = list(blank)
lives = 0
for i in chosen_word:
    lives += 1
indexes = []

for char in range(0, lives):
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
                print(f"you have already typed {guess_letter}\n")
            indexes = []
        # Updating the blank word
        blank = ""
        for letter in blank_list:
            blank += letter
        print(blank)
        print(f"available attempts: {lives}\n")
    else:
        print("Wrong\n")
        lives -= 1
        print(f"available attempts: {lives}\n")

print("the word is: \n" + chosen_word)
