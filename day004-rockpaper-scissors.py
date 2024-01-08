rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
comp_choice = random.randint(0,2)
hand_sign_list = [rock, paper, scissors]
human_choice_num = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors:\n"))
print(hand_sign_list[human_choice_num])
print("Computer chose:")
print(hand_sign_list[comp_choice])
if (human_choice_num == 0 and comp_choice == 2) or (human_choice_num == 1 and comp_choice == 0) or (human_choice_num == 2 and comp_choice == 1):
  print("you win")
elif human_choice_num == comp_choice:
  print("draw")
else:
  print("computer wins")