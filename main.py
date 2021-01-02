# 100 Days of Code
# Dice Simulator

import random
from art import logo
from replit import clear

# variables
dice = []
rolling = True

# game loop
while rolling:
  print(logo)
  print("Welcome to the Dice Simulator.\n")
  total = 0
  # user input
  dice_num = int(input("How many dice would you like to roll?: \n"))
  sides = int(input("How many sides do the dice have?(6-20): \n"))
  print("Roll the dice!")

  # builds dice
  for i in range(sides):
    dice.append(i+1)

  # rolls dice
  for i in range(dice_num):
    roll = random.choice(dice)
    total += roll
    print(f"You rolled a {roll}")

  print(f"Your total score was {total}")

  # option to play again or quit
  if input("Roll again? y/n: ") == 'n':
    rolling = False
  clear()