"""Part 2, Module 1: Create a guess the number game."""
import random


def main():
    secret = random.randint(1, 100)
    attempts = 0
    while True:
        guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1
        if guess < secret:
            print("Too low.")
        elif guess > secret:
            print("Too high.")
        else:
            print(f"You got it in {attempts} attempts!")
            break


if __name__ == "__main__":
    main()
