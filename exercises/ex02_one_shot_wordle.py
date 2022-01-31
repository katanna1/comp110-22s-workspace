"""Wordle game."""

__author__ = "730479768"

word: str = "python"
guess: str = input(f"What is your {len(word)} guess? ")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

word_emojis: str = ""


i: int = 0
while (len(guess) != len(word)):
    guess = input(f"That was not {len(word)} letters! Try again: ")
    
while (i < len(word)):
    """Loops as many indexes as the length of the secret word."""
    if guess[i] == word[i]:
        word_emojis = word_emojis + GREEN_BOX 
        """Correct letter placement get a green box."""
    else:
        alternate_i: int = 0
        exists: bool = False
        while exists is False and alternate_i < len(word):
            """In loop code compares the index of the guess among all letters of the secret word."""
            if guess[i] == word[alternate_i]:
                exists = True
            else:
                alternate_i = alternate_i + 1
        if exists is False:
            word_emojis = word_emojis + WHITE_BOX
            """White box for whenever the letter in the guess does not match any of the letter in the word."""
        else:
            word_emojis = word_emojis + YELLOW_BOX
    i = i + 1

print(word_emojis)
if guess != word: 
    print("Not quite. Play again soon! ")
else:
    print("Woo! You got it!")
