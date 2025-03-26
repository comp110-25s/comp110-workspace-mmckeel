def main(secret: str) -> None:
    """The entrypoint of the program and main game loop"""


secret_word = "codes"
max_turns = 6
turn = 1
won = False
while turn <= max_turns and not won:
    print(f"=== Turn {turn}/{max_turns} ===")
    guess = input_guess(len(secret_word))
    result = emojified(guess, secret_word)
    print(result)
    if guess == secret_word:
        won = True
    else:
        turn += 1
    if won:
        print(f"You won in {turn}/{max_turns}!")
    else:
        print("X/6 - Sorry, try again tomorrow!")
