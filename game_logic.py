import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

# Max mistakes = last melting stage
MAX_MISTAKES = len(STAGES) - 1

def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]

def display_game_state(mistakes, secret_word, guessed_letters):
    """Shows the snowman stage and the word so far."""
    print(STAGES[mistakes])

    # Show guessed letters and underscores for the rest
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: " + display_word)

def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    print("Welcome to Snowman Meltdown!")

    # Keep going until the snowman melts or the word is solved
    while mistakes < MAX_MISTAKES:
        display_game_state(mistakes, secret_word, guessed_letters)

        # Win check: every letter has been guessed
        if all(letter in guessed_letters for letter in secret_word):
            break

        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in secret_word:
            guessed_letters.append(guess)
        else:
            guessed_letters.append(guess)
            mistakes += 1

    # End message
    if all(letter in guessed_letters for letter in secret_word):
        print("You saved the snowman! The word was: " + secret_word)
    else:
        print("The snowman melted! The word was: " + secret_word)

if __name__ == "__main__":
    play_game()
