import random

#word list

Words = ["Math", "Science", "History", "English", "Computer"]
secret_word = random.choice(Words)

guessed_letters = []
attempts_left = 8

print("Welcome to Word Guessing Game!")
print(f"The secret word has {len(secret_word)} letters.\n")


while attempts_left > 0:
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("word: ", display_word.strip())

    if "_ " not in display_word:
        print("🎉 You guessed the word correctly!")
        break

    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter. Try again.\n")
        continue

    guessed_letters.append(guess)
    if guess in secret_word:
        print("✅ Correct guess!\n")
    else:
        print("❌ Wrong guess!\n")
        attempts_left -= 1

if attempts_left == 0:
    print(f"Game Over! The Word Was '{secret_word}'.")

print("\nThanks for playing")


