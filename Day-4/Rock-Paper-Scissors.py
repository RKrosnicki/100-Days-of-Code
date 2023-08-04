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

import random

print("Welcome to the Rock, Paper, Scissors game!\n\n")
player = input("Which is it? rock, paper, or scissors?\n").lower()
choices = [rock, paper, scissors]
computer = choices[random.randint(0, 2)]

if player == 'rock' and computer == rock:
    print(f"Your choice is rock: {rock}")
    print(f"Computers choice is also rock{computer}")
    print("It's a tie!")
elif player == 'rock' and computer == paper:
    print(f"Your choice is rock: {rock}")
    print(f"Computers choice is paper{computer}")
    print("You lose!")
elif player == 'rock' and computer == scissors:
    print(f"Your choice is rock: {rock}")
    print(f"Computers choice is scissors{computer}")
    print("You win!")
elif player == 'paper' and computer == rock:
    print(f"Your choice is paper: {paper}")
    print(f"Computers choice is rock{computer}")
    print("You win!")
elif player == 'paper' and computer == paper:
    print(f"Your choice is paper: {paper}")
    print(f"Computers choice is also paper{computer}")
    print("It's a tie!")
elif player == 'paper' and computer == scissors:
    print(f"Your choice is paper: {paper}")
    print(f"Computers choice is scissors{computer}")
    print("You lose!")
elif player == 'scissors' and computer == rock:
    print(f"Your choice is scissors: {scissors}")
    print(f"Computers choice is rock{computer}")
    print("You lose!")
elif player == 'scissors' and computer == paper:
    print(f"Your choice is scissors: {scissors}")
    print(f"Computers choice is paper{computer}")
    print("You win!")
elif player == 'scissors' and computer == scissors:
    print(f"Your choice is scissors: {scissors}")
    print(f"Computers choice is also scissors{computer}")
    print("It's a tie!")
else:
    print("Try again, and type one of the following: rock, paper, scissors")
