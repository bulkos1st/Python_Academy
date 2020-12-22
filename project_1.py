"""
Python Academy Project 1
"""
TEXTS = [
    '''Situated about 10 miles west of Kemmerer, 
    Fossil Butte is a ruggedly impressive 
    topographic feature that rises sharply 
    some 1000 feet above Twin Creek Valley 
    to an elevation of more than 7500 feet 
    above sea level. The butte is located just 
    north of US 30N and the Union Pacific Railroad, 
    which traverse the valley. ''',

    '''At the base of Fossil Butte are the bright 
    red, purple, yellow and gray beds of the Wasatch 
    Formation. Eroded portions of these horizontal 
    beds slope gradually upward from the valley floor 
    and steepen abruptly. Overlying them and extending 
    to the top of the butte are the much steeper 
    buff-to-white beds of the Green River Formation, 
    which are about 300 feet thick.''',

    '''The monument contains 8198 acres and protects 
    a portion of the largest deposit of freshwater fish 
    fossils in the world. The richest fossil fish deposits 
    are found in multiple limestone layers, which lie some 
    100 feet below the top of the butte. The fossils 
    represent several varieties of perch, as well as 
    other freshwater genera and herring similar to those 
    in modern oceans. Other fish such as paddlefish, 
    garpike and stingray are also present.'''
]

USER_DB = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
    }

WIDTH = 60
SPACER = "-" * WIDTH
texts_count = len(TEXTS)

# Greet or welcome the user to the app
print(SPACER)
print("Welcome to the app. Please log in".center(WIDTH, " "))
print(SPACER)

# Ask the user for entering username and password
while True:
    username = input("Username: ")
    password = input("Password:")

    # Check whether the password and username entered are among those registered.
    if username in USER_DB and USER_DB[username] == password:
        print("Login Successful!")
        break

    print("Username or password is not valid. Please try again.")
    print(SPACER)

# Ask the user to select among the three texts stored in the variable TEXTS
print(SPACER)
print(f"We have {texts_count} texts to be analyzed.".center(WIDTH, " "))
print(SPACER)

while True:
    try:
        select_text = int(input(f"Enter a number between 1 and {texts_count} to select text: "))
    except ValueError:
        print("Only numbers are allowed. App will exit now.")
        exit()

    if 1 <= select_text <= texts_count:
        break
    else:
        print(f"Invalid value entered! Select value between 1 and {texts_count} ")

# Calculate the following statistics for the selected text:

word_list = [word.strip(",.:") for word in TEXTS[select_text - 1].split()]
titlecase_list = [word for word in word_list if word.istitle()]  # number of words starting with capital letter
upcase_list = [word for word in word_list if word.isupper()]  # number of uppercase words
lowcase_list = [word for word in word_list if word.islower()]  # number of lowercase words
numeric_list = [int(word) for word in word_list if word.isnumeric()]  # number of numeric-only words

print(SPACER)
print(f"There are {len(word_list)} words in the selected text.")
print(f"There are {len(titlecase_list)} titlecase words.")
print(f"There are {len(upcase_list)} uppercase words.")
print(f"There are {len(lowcase_list)} lowercase words.")
print(f"There are {len(numeric_list)} numeric strings.")
print(SPACER)

# Create a bar chart depicting the frequencies of word lengths in the text.
word_lengths = {}
while word_list:
    word_len = len(word_list.pop())
    word_lengths.setdefault(word_len, 0)
    word_lengths[word_len] += 1

sorted_word_lengths = {k: word_lengths[k] for k in sorted(word_lengths)}  # new dict with sorted keys

for word_len, word_count in sorted_word_lengths.items():
    print(f"{word_len}{'.' * word_count} {word_count}")

# Calculate the sum of all the numeric "words" in the given text.
print(SPACER)
print(f"If we summed all the numbers in this text we would get: {sum(numeric_list)}")
print(SPACER)
