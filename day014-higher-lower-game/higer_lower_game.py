from art import logo, vs
from game_data import data
import random

#randomly choose the first two accounts, and subsequent to compare - prob make a function
#accept A B input
#create a loop that cont until wrong
#track points

print(logo)

def get_rand_dict_account():
    return random.choice(data)

def present_candidates(candidateA, candidateB):
    print(f"Choice A: {candidateA['name']}, a {candidateA['description']}, from {candidateA['country']}.")
    print(vs)
    print(f"Choice B: {candidateB['name']}, a {candidateB['description']}, from {candidateB['country']}.")

def get_player_choice():
    return input("Who has more Instagram followers, choice A or B? ").upper()

def print_follower_counts(candidateA, candidateB):
    print(f"Choice A, {candidateA['name']}, has {candidateA['follower_count']} million followers. Choice B, {candidateB['name']}, has {candidateB['follower_count']} million followers.")

def get_results(candidateA, candidateB, choice):
    a_followers = candidateA['follower_count']
    b_followers = candidateB['follower_count']
    print_follower_counts(candidateA, candidateB)
    if a_followers > b_followers and choice == "A":  
        return 0
    elif b_followers > a_followers and choice == "B":
        return 0
    else:
        print("Incorrect answer. You lose.")
        print(f"You had {correct_answers} correct answer(s).")
        return 1

def choose_candidates(candidateA, candidateB):
    present_candidates(candidateA, candidateB)
    choice = get_player_choice()
    lost = get_results(candidateA, candidateB, choice)
    if lost == 0:
          print("Correct answer.")
          global correct_answers
          correct_answers += 1
          print(f"You have {correct_answers} correct answer(s).\n")
          if choice == "A":
              choose_candidates(candidateA, get_rand_dict_account())
          elif choice == "B":
              choose_candidates(candidateB, get_rand_dict_account())
    
correct_answers = 0


choose_candidates(get_rand_dict_account(), get_rand_dict_account())