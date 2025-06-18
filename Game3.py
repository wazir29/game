import random

print("Welcome to Multi-Level Number Guessing Game")

while True:
    print("\n===== Game Menu =====")
    print("1. Level 1 (1 - 20)")
    print("2. Level 2 (1 - 50)")
    print("3. Level 3 (1 - 100)")
    print("4. Exit Game")


    choice = input("Select a level (1 - 4): ")

    if choice == "1":
        secret_number = random.randint(1, 20)
        attemps = 5
        max_number = 20
    elif choice == "2":
        secret_number = random.randint(1, 50)
        attemps = 7
        max_number = 50
    elif choice == "3":
        secret_number = random.randint(1, 100)
        attemps = 10
        max_number = 100
    elif choice == "4":
        print("Thanks for playing! Goodbye!")
        break
    else:
        print("Invalid choice! Try again.")
        continue
    print(f"\n Level Selected! Guess the number between 1 and {max_number}!")
    while attemps > 0:
        guess = int(input(f"Attempts left: {attemps}. Enter your guess: "))

        if guess == secret_number:
            print("Correct! You won this level!")
        elif guess < secret_number:
            print("Too low!")
        else:
            print("Too high!")
        attemps -= 1

    if attemps == 0:
        print(f"Out of attempts! The number was {secret_number}.")
    play_again = input("\nDo you want to return to menu? (y/n): ")
    if play_again.lower() != 'y':
        print("Goodbye Thanks for playing!")
        break    









