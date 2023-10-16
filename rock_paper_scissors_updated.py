"""
Created on Mon Oct 16 13:43:26 2023
Update: Implement multi-round gameplay.
Track the scores of both the player and the computer.
@author: danielcook
"""

import random

def get_player_choice():
    """Prompt the user to enter a choice and validate it."""
    player_choice = input("\nEnter your choice (rock/paper/scissors): ").lower()

    while player_choice not in ["rock", "paper", "scissors"]:
        player_choice = input('Invalid choice. Please enter rock, paper, or scissors: ').lower()

    return player_choice


def get_winner(player_choice, computer_choice):
    """Determine the winner based on choices."""
    if player_choice == computer_choice:
        return "tie"
    elif player_choice == "rock":
        return "player" if computer_choice == "scissors" else "computer"
    elif player_choice == "paper":
        return "player" if computer_choice == "rock" else "computer"
    else: # player_choice == "scissors"
        return "player" if computer_choice == "paper" else "computer"


def display_round_result(player_choice, computer_choice, winner):
    """Display the results of a round."""
    print(f"\nYou chose {player_choice}.")
    print(f"Computer chose {computer_choice}.")
    
    if winner == "tie":
        print("It's a tie!")
    elif winner == "player":
        print("You win this round!")
    else:
        print("Computer wins this round!")


def main():
    print("Let's play Rock, Paper, Scissors!")
    num_rounds = int(input("How many rounds would you like to play? "))
    player_score = 0
    computer_score = 0

    for _ in range(num_rounds):
        player_choice = get_player_choice()
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        winner = get_winner(player_choice, computer_choice)
        
        display_round_result(player_choice, computer_choice, winner)
        
        if winner == "player":
            player_score += 1
        elif winner == "computer":
            computer_score += 1

    # Final score
    print("\n--- Final Scores ---")
    print(f"Player: {player_score}")
    print(f"Computer: {computer_score}")

    if player_score > computer_score:
        print("Congratulations! You won the game!")
    elif player_score < computer_score:
        print("Computer wins the game. Better luck next time!")
    else:
        print("It's a tie game!")

if __name__ == "__main__":
    main()
