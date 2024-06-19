import random

user_wins = 0
bots_wins = 0

options = ["rock", "paper", "scissors"]

while True:
  user_choice = input("Enter a choice (Rock, Paper, Scissors or Q to quit): ").lower()
  if user_choice == "q":
    break

  if user_choice not in options:
    continue

  random_number = random.randint(0, 2)
  # rock: 0, paper: 1, scissors: 2
  bot_choice = options[random_number]
  print("Bot chose: " + bot_choice + ".")

  if user_choice == "rock" and bot_choice == "scissors":
    print("You won!")
    user_wins += 1
    continue

  elif user_choice == "paper" and bot_choice == "rock":
    print("You won!")
    user_wins += 1
    
  elif user_choice == "scissors" and bot_choice == "paper":
    print("You won!")
    user_wins += 1

  else:
    print("You lost!")
    bots_wins += 1

print("You won", user_wins, "times.")
print("Bot won", bots_wins, "times.")
print("Game Over!")
  