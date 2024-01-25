#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

#So need to randomly generate a number
#Prompt for guess
#Track guesses remaining (based on difficulty for start)
#Make a function to compare the guess to the mystery number - actually used while loop
#Make function to check if lost, and keep in scope

import random
target = random.randint(1,100)


print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

difficulty = ""
while difficulty != "easy" and difficulty != "hard":
  difficulty = input("Choose your difficulty. Easy or hard? ").lower()

if difficulty == "easy":
  guesses = 10
elif difficulty == "hard":
  guesses = 5

won = 0
lost = 0

def check_if_lost(guesses_remaining):
  if guesses_remaining == 0:
    print(f"You lose. The number was {target}.")
    return 1
  else:
    return 0

while won == 0 and lost == 0:
  print(f"You have {guesses} guesses remaing.")
  guess = int(input("Make a guess: "))
  if guess == target:
    print(f"You win! The number was {target}!")
    won = 1
  elif target < guess:
    print("Too high.")
    guesses -= 1
    lost = check_if_lost(guesses)
  elif target > guess:
    print("Too low.")
    guesses -= 1
    lost = check_if_lost(guesses)
    