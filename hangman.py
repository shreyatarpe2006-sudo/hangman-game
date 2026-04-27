import random

# Predefined word list (5 words)
words = ["apple", "chair", "table", "plant", "bread"]

# Randomly choose a word
word = random.choice(words)

# Create display with underscores
guessed_word = ["_"] * len(word)

# Track guesses
guessed_letters = []
wrong_guesses = 0
max_wrong = 6

print("🎮 Welcome to Hangman Game!")
print("Guess the word:")

# Game loop
while wrong_guesses < max_wrong and "_" in guessed_word:
    
    print("\nWord:", " ".join(guessed_word))
    print("Wrong guesses left:", max_wrong - wrong_guesses)
    
    guess = input("Enter a letter: ").lower()

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    # Check if guess is correct
    if guess in word:
        print("✅ Correct guess!")
        
        # Fill the guessed letter
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        print("❌ Wrong guess!")
        wrong_guesses += 1

# Final result
if "_" not in guessed_word:
    print("\n🎉 Congratulations! You guessed the word:", word)
else:
    print("\n💀 Game Over! The word was:", word)