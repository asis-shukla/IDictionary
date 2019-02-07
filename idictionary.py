import json

file_ptr = open("dict_data.json", "r")  # Create a file pointer to dictionary data stored in disk
 
d_data = json.load(file_ptr)        # load json data to d_data


while True:
    word = input("Enter your word: ")
    if word == "" or word == " ":
        print("This is blank, Please enter correct word! ")
    else:
        temp = False
        word = word.lower()  # Convert string enttered by the user to all lower case 
        for key in d_data:
            if key == word:
                temp = True   # Just to remember that word is found in the dictionary
                # Now word is found in the dictionary, we print the each meaning as a sentence on the screen
                for sentence in d_data[key]:
                    print(sentence)         
            else:
                pass   # check word for another key
        if not temp:
            print(word,  "not found in the dictionary!, check for spelling error or enter another word!")
        else:
            pass

