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


