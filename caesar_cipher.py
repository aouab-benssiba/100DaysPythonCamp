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
           'w', 'x', 'y', 'z']


# Asking to fill up the needed variables

try:
    choice = str(input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")).lower()
    if choice != "encode" and choice != "decode":
        raise ValueError(f"you have misspelled {choice}.")
except ValueError as e:
    print(f"Error: {e}")
    exit()
message = str(input("Type your message:\n"))

shift = int(input("Type the shift number:\n"))

total_letters = len(letters)

# Function section:

def encode():
    message_list = list(message)

    # TODO : if the index of message_list is a number or a special character, it should be ignored
    #  while it position is saved and called back again when it is encoded to it same position

    outsiders_dic = {}
    filtered_list = []
    # using enumerate to get the indexes and mitigate errors when char replicates
    for index, char in enumerate(message_list):
        if char not in letters:
            outsiders_dic[index] = char
        if char in letters:
            filtered_list.append(char)

    # TODO 1: for each char in message_list,
    #  i want to extract it index in the letters list, and assign it to a indexes_list, for example: h his index is 7
    indexes_list = []
    for char in filtered_list:
        number = letters.index(char)  # 7
        indexes_list.append(number)

    # TODO 2: then add the shift number to each index in the indexes list
    for index, number in enumerate(indexes_list):
        # using modulo to wrap up the shift back to the beginning
        indexes_list[index] = (number + shift) % total_letters

    # TODO 3: then translate each index_number in indexes_list to it char in letters list, and assign them into encode_list
    encode_list = []
    for i in indexes_list:
        encode_list += letters[i]

    # TODO 4: then make encode_list back to a word
    for index, char in outsiders_dic.items():
        encode_list.insert(index, char)

    encoded_word = ""
    for char in encode_list:
        encoded_word += char

    print("\n" + "Here's the encoded result: " + encoded_word)


def decode():
    message_list = list(message)
    outsiders_dic = {}
    filtered_list = []
    for index, char in enumerate(message_list):
        if char not in letters:
            outsiders_dic[index] = char
        if char in letters:
            filtered_list.append(char)
    indexes_list = []
    # TODO 1: for each char in message_list,
    #     #  i want to extract it index in the letters list, and assign it to a indexes_list, for example: h his index is 7

    for char in filtered_list:
        number = letters.index(char)  # 7
        indexes_list.append(number)


    # TODO 2: then subtract the shift number for each index in the indexes list

    for index, number in enumerate(indexes_list):
        # we are using modulo to wrap up the shift back to the beginning
        indexes_list[index] = (number - shift) % total_letters

    # TODO 3: then translate each index_number in indexes_list to it char in letters list, and assign them into encode_list

    decode_list = []
    for i in indexes_list:
        decode_list += letters[i]
    # TODO 4: then make encode_list back to a word

    for index, char in outsiders_dic.items():
        decode_list.insert(index, char)

    decoded_word = ""
    for char in decode_list:
        decoded_word += char

    print("\n" + "Here's the decoded result: " + decoded_word)


while True:
    if choice == "encode":
        encode()
    elif choice == "decode":
        decode()
    answer = str(input("do you want to play again? y/[N]")).lower()
    if answer != "y":
        break

    try:
        choice = str(input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")).lower()
        if choice != "encode" and choice != "decode":
            raise ValueError(f"you have misspelled {choice}.")
    except ValueError as e:
        print(f"Error: {e}")
        exit()
    message = str(input("Type your message:\n"))

    shift = int(input("Type the shift number:\n"))
