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


def input_guess(expected_length: int, secret: str) -> str:
    """Asks user for input."""
    expected_length = len(secret)
    user_guess: str = input(f"Enter a {expected_length} word: ")
    while len(user_guess) != expected_length:
        user_guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return user_guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    i: int = 0
    while i < 6:
        j: int = i + 1
        print(f"=== Turn {j}/6 ===")
        guess: str = input_guess(len(secret_word), secret_word)
        print(emojified(guess, secret_word))
        if guess == secret_word:
            print(f"You won in {j}/6 turns!")
            exit()
        else:
            if i == 5:
                print("X/6 - Sorry, try again tomorrow!")
            i = i + 1


if __name__ == "__main__":
    main()
