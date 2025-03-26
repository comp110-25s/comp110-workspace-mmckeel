"""Megan M's Wordle!"""

__author__: str = "730556813"


def contains_char(word_input: str, character: str) -> bool:
    """A function evaluating whether a character is located within our secret word"""
    assert len(character) == 1, f"len('{character})' is not 1"
    idx: int = 0
    while idx < len(word_input):
        if word_input[idx] == character:
            return True
        idx += 1
    return False


def emojified(guessed_word: str, secret_word: str) -> str:
    """A function that converts characters of a word into emojis (based on accuracy)"""
    assert len(guessed_word) == len(secret_word), "Guess must be same length as secret"
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    idx: int = 0
    indicated_emoji: str = ""
    while idx < len(guessed_word):
        if guessed_word[idx] == secret_word[idx]:
            indicated_emoji = indicated_emoji + GREEN_BOX
        elif contains_char(secret_word, guessed_word[idx]):
            indicated_emoji = indicated_emoji + YELLOW_BOX
        else:
            indicated_emoji = indicated_emoji + WHITE_BOX
        idx += 1
    return indicated_emoji


def input_guess(nlength_word: int) -> str:
    """Prompts user until a word with the expected length is provided"""
    player_guess = input(f"Enter a {nlength_word} character word: ")
    if len(player_guess) != nlength_word:
        player_guess = input(f"That wasn't {nlength_word} chars! Try again:")
    return player_guess


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    while turn < 7:
        print(f"=== Turn {turn}/6 ===")
        user_word: str = input_guess(nlength_word=len(secret))
        print(emojified(guessed_word=user_word, secret_word=secret))
        if user_word == secret:
            print(f"You won in {turn}/6 turns!")
        else:
            turn += 1
    print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
