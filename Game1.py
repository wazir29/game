import random

#Game Setup
secret_number = random.randint(1, 50)
attempts_left = 5

print("^_^ Welcome to the Number Guessing Battle!")
print("I have picked a number between 1 and 50.")
print("You have 7 attempts to guess it correctly.\n")

while attempts_left > 0:
    guess = int(input(f"Attempts left({attempts_left}). Enter your guess: "))

    if guess == secret_number:
        print("🎉 Congraulations! You guessed the correct number!")
        break
    elif guess < secret_number:
        print("📉 Too low! Try a higher number.\n")
    else:
        print("📈 Too high! Try a lower number.\n")

    attempts_left -= 1

if attempts_left == 0:
    print(f"❌ Out of attempts! The number was {secret_number}.")

print("Thanks for playing! ^_^")