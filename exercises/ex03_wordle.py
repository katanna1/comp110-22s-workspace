"""Wordle game."""

__author__ = "730479768"

secret_word: str = "codes"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(guess: str, letter: str) -> bool:
    """This function sees if the letter is in the word."""
    assert len(letter) == 1
    i: int = 0
    while i < len(guess):
        if guess[i] == letter:
            return True
        i = i + 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Shows right and wrong letters through emojis."""
    assert len(guess) == len(secret)
    word_emojis: str = ""
    i: int = 0
    while i < len(guess):
        if guess[i] == secret[i]:
            word_emojis = word_emojis + GREEN_BOX
        else:
            if contains_char(secret, guess[i]) is True:
                word_emojis = word_emojis + YELLOW_BOX
            else:
                word_emojis = word_emojis + WHITE_BOX
        i = i + 1
    return word_emojis


def input_guess(expected_length: int) -> str:
    """Asks user for input."""
    user_guess: str = input(f"Enter a {expected_length} word: ")
    while len(user_guess) != expected_length:
        user_guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return user_guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    turns: int = 1
    not_won: bool = True
    while turns < 7:
        print(f"=== Turn {turns}/6 ===")
        guess: str = input_guess(len(secret_word))
        print(emojified(guess, secret_word))
        if guess == secret_word:
            print(f"You won in {turns}/6 turns!")
            turns = 7
            not_won = False
        else:
            turns = turns + 1
    if not_won is True:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()
