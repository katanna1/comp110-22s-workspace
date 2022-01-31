"""Wordle game"""

__author__ = "730479768"

word: str = "python"
guess: str = input("What is your 6-letter guess? ")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

word_emojis: str = ""
i: int = 0
while (len(guess) != len(word)):
    guess = input("That was not 6 letters! Try again: ")
    
while (i < len(word)):
    if guess[i] == word[i]:
        word_emojis = word_emojis + GREEN_BOX 
    else:
        word_emojis = word_emojis + WHITE_BOX
    i = i + 1
print(word_emojis)
if guess != word: 
    print("Not quite. Play again soon! ")
else:
    print("Woo! You got it!")
