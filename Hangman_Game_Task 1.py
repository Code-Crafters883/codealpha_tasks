import random

def hangman():
    # List of words to choose from
    words = ["python", "hangman", "challenge", "programming", "computer", "algorithm"]
    
    # Select a random word from the list
    word = random.choice(words)
    
    # Number of allowed incorrect guesses
    max_attempts = 6
    attempts = 0
    
    # Set to keep track of guessed letters
    guessed_letters = set()
    
    # Create a list to represent the current state of the word
    current_word = ["_"] * len(word)
    
    print("Welcome to Hangman!")
    print(" ".join(current_word))
    
    while attempts < max_attempts:
        # Prompt the player to guess a letter
        guess = input("Guess a letter: ").lower()
        
        # Check if the input is a single letter
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue
        
        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue
        
        # Add the guessed letter to the set of guessed letters
        guessed_letters.add(guess)
        
        # Check if the guessed letter is in the word
        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
            # Update the current word representation
            for i in range(len(word)):
                if word[i] == guess:
                    current_word[i] = guess
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            attempts += 1
            print(f"You have {max_attempts - attempts} attempts left.")
        
        # Display the current state of the word
        print(" ".join(current_word))
        
        # Check if the player has guessed the entire word
        if "_" not in current_word:
            print("Congratulations! You've guessed the word:", word)
            break
    
    # If the player runs out of attempts
    if attempts == max_attempts:
        print("You've run out of attempts. The word was:", word)

# Run the game
hangman()
