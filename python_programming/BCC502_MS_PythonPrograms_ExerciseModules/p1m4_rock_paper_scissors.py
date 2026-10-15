"""Part 1, Module 4: Create a rock, paper, scissors game."""
import random

CHOICES = ("rock", "paper", "scissors")


def decide(player, computer):
    """Return 'win', 'lose', or 'tie' from the player's point of view."""
    if player == computer:
        return "tie"
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        return "win"
    else:
        return "lose"


def main():
    player = input("Choose rock, paper, or scissors: ").strip().lower()
    if player not in CHOICES:
        print("That is not a valid choice.")
        return
    computer = random.choice(CHOICES)
    print(f"Computer chose {computer}.")
    result = decide(player, computer)
    if result == "tie":
        print("It's a tie!")
    elif result == "win":
        print("You win!")
    else:
        print("You lose!")


if __name__ == "__main__":
    main()
