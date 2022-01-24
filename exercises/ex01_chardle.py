"""Fun Wordle-like Program :)"""

__author__ = "730479768"

word: str = input("Enter a 5-character word: ")
letter: str = input("Enter a single character: ")
instance: int = 0

print("Searching for " + letter + " in " + word)

if letter == word[0]:
    instance = instance + 1
    print(letter + " found at index " + str(0)) 
if letter == word[1]:
    instance = instance + 1
    print(letter + " found at index " + str(1))        
if letter == word[2]:
    instance = instance + 1
    print(letter + " found at index " + str(2))
if letter == word[3]:
    instance = instance + 1
    print(letter + " found at index " + str(3))
if letter == word[4]:
    instance = instance + 1
    print(letter + " found at index " + str(4))


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


if instance == 1:
    print("1 instance of " + letter + "found in " + word)
else:
    if instance == 2:
        print("2 instances of " + letter + "found in " + word)
    else:
        if instance == 3:
            print("3 instances of " + letter + " found in " + word)
        else:
            if instance == 5:
                print("4 instances of " + letter + " found in " + word)
            else:
                if instance == 0:
                    print("No instances of " + letter + " found in " + word)