"""
Created on Thu Apr 20 18:42:41 2023

@author: danielcook
"""

import random

print("Let's play Rock, Paper, Scissors!")

player_choice = input("Enter your choise (rock/paper/scissors): ").lower()

#validate player's input
while player_choice not in ["rock", "paper","scissors"]:
    player_choice = input('invalid choice. Pleae enter rock, paper, or scissors: ').lower()
    
    
#generate computer's choise randomly
computer_choice = random.choice(['rock', 'paper', 'scissors'])
print(f"\nComputer chose {computer_choice}.")

#determine the winner
if player_choice == computer_choice:
    print("It's a tie!")

elif player_choice == "rock":
    if computer_choice =="paper":
        print("Computer wins!")
    else:
        print("You win!")
elif player_choice == "paper":
    if computer_choice == "scissors":
        print("Computer wins!")
    else:
        print("You win")
else:
    player_choice == "scissors"
    if computer_choice == "rock":
        print("Computer wins!")
