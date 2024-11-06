import random

# List of words for the game
words = ["python", "hangman", "challenge", "programming", "development"]

# Function to display the current state of the game
def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   -----
                   |   |
                   |   O
                   |  /|\\
                   |  / \\
                   -
                """,
                # head, torso, both arms
                """
                   -----
                   |   |
                   |   O
                   |  /|\\
                   |  /
                   -
                """,
                # head, torso, one arm
                """
                   -----
                   |   |
                   |   O
                   |  /|
                   |  
                   -
                """,
                # head, torso
                """
                   -----
                   |   |
                   |   O
                   |  
                   |  
                   -
                """,
                # head
                """
                   -----
                   |   |
                   |   
                   |  
                   |  
                   -
                """,
                # initial empty state
                """
                   -----
                   |   |
                   |   
                   |  
                   |  
                   -
                """
    ]
    return stages[tries]

# Main game function
def play_hangman():
    word = random.choice(words)  # Randomly choose a word
    word_completion = "_" * len(word)  # Create a string of underscores
    guessed = False  # To track if the word has been guessed
    guessed_letters = []  # To store guessed letters
    tries = 5  # Number of tries

    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(word_completion)

    while not guessed and tries > 0:
        guess = input("Please guess a letter: ").lower()  # User input
        if len(guess) != 1 or not guess.isalpha():  # Validate input
            print("Invalid input. Please enter a single letter.")
            continue
        if guess in guessed_letters:  # Check if letter was already guessed
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)  # Add letter to guessed list

        if guess in word:  # Correct guess
            print(f"Good job! '{guess}' is in the word.")
            # Update the word completion
            word_completion = ''.join([letter if letter in guessed_letters else '_' for letter in word])
            if "_" not in word_completion:  # Word is fully guessed
                guessed = True
        else:  # Wrong guess
            tries -= 1
            print(f"Sorry, '{guess}' is not in the word. You have {tries} tries left.")

        print(display_hangman(tries))
        print(word_completion)

    if guessed:
        print("Congratulations! You've guessed the word!")
    else:
        print(f"Sorry, you've run out of tries. The word was '{word}'.")

# Start the game
if __name__ == "__main__":
    play_hangman()
