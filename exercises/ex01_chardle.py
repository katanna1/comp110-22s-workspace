"""Fun Wordle-like Program :)."""

__author__ = "730479768"

word: str = input("Enter a 5-character word: ")
if len(word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
letter: str = input("Enter a single character: ")
if len(letter) != 1:
    print("Error: Character must be a single character.")
    exit()

print("Searching for " + letter + " in " + word)

instance: int = 0
if letter == word[0]:
    instance = instance + 1
if letter == word[1]:
    instance = instance + 1
if letter == word[2]:
    instance = instance + 1
if letter == word[3]:
    instance = instance + 1
if letter == word[4]:
    instance = instance + 1

if letter == word[0]:
    print(letter + " found at index " + str(0)) 
if letter == word[1]:
    print(letter + " found at index " + str(1))        
if letter == word[2]:
    print(letter + " found at index " + str(2))
if letter == word[3]:
    print(letter + " found at index " + str(3))
if letter == word[4]:
    print(letter + " found at index " + str(4))


if instance == 1:
    print("1 instance of " + letter + " found in " + word)
else:
    if instance == 2:
        print("2 instances of " + letter + " found in " + word)
    else:
        if instance == 3:
            print("3 instances of " + letter + " found in " + word)
        else:
            if instance == 4:
                print("4 instances of " + letter + " found in " + word)
            else:
                if instance == 5:
                    print("5 instances of " + letter + " found in " + word)
                else:
                    if instance == 0:
                        print("No instances of " + letter + " found in " + word)