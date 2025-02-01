print(r''' ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     'Y8 a8P_____88 I8[    "" ""     'Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  '"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 '"Ybbd8"' '"8bbdP"Y8  '"Ybbd8"' '"YbbdP"' '"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 '"Ybbd8"' 88 88'YbbdP"'  88       88  '"Ybbd8"' 88          
              88                                             
              88           ''')

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']


# Asking to fill up the needed variables

try:
    choice = str(input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")).lower()
    if choice != "encode" and choice != "decode":
        raise ValueError(f"you have misspelled {choice}.")
except ValueError as e:
    print(f"Error: {e}")
    exit()
message = str(input("Type your message only letters:\n"))

shift = int(input("Type the shift number:\n"))



# Function section:

def encode():
    message_list = list(message)
    indexes_list = []
    # TODO 1: for each char in message_list,
    #  i want to extract it index in the letters list, and assign it to a indexes_list, for example: h his index is 7
    for char in message_list:
        number = letters.index(char)  # 7
        indexes_list.append(number)

    # TODO 2: then add the shift number to each index in the indexes list
    for i in indexes_list:
        original_i = i  # 7
        i += shift  # 8
        original_index = indexes_list.index(original_i)  # 0
        indexes_list[original_index] = i

    # TODO 3: then translate each index_number in indexes_list to it char in letters list, and assign them into encode_list
    encode_list = []
    for i in indexes_list:
        index = i  # 8
        letter = letters[index]  # i
        encode_list += letter

    # TODO 4: then make encode_list back to a word
    encoded_word = ""
    for char in encode_list:
        encoded_word += char

    print("\n" + "Here's the encoded result: " + encoded_word)

def reset_encode():
    indexes_list = []
    message_list = []
    encode_list = []
    encoded_word = ""


def decode():
    message_list = list(message)
    indexes_list = []
    # TODO 1: for each char in message_list,
    #     #  i want to extract it index in the letters list, and assign it to a indexes_list, for example: h his index is 7

    for char in message_list:
        number = letters.index(char)  # 7
        indexes_list.append(number)


    # TODO 2: then subtract the shift number for each index in the indexes list

    for i in indexes_list:
        original_i = i  # 8
        i -= shift  # 7
        original_index = indexes_list.index(original_i)  # 0
        indexes_list[original_index] = i

    # TODO 3: then translate each index_number in indexes_list to it char in letters list, and assign them into encode_list

    decode_list = []
    for i in indexes_list:
        index = i  # 7
        letter = letters[index]  # h
        decode_list += letter
    # TODO 4: then make encode_list back to a word
    decoded_word = ""
    for char in decode_list:
        decoded_word += char

    print("\n" + "Here's the decoded result: " + decoded_word)

def reset_decode():
    indexes_list = []
    message_list = []
    decode_list = []
    decoded_word = ""


while True:
    if choice == "encode":
        encode()
        reset_encode()
    elif choice == "decode":
        decode()
        reset_decode()
    answer = str(input("do you want to play again? y/[N]")).lower()
    if answer != "y":
        break
    elif answer == "y":
        try:
            choice = str(input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")).lower()
            if choice != "encode" and choice != "decode":
                raise ValueError(f"you have misspelled {choice}.")
        except ValueError as e:
            print(f"Error: {e}")
            exit()
        message = str(input("Type your message only letters:\n"))

        shift = int(input("Type the shift number:\n"))

