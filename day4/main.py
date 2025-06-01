import random

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

game_image = [rock, paper, scissors]

player = int(input("What do you choose? Type 0 for rock, 1 for paper and 2 for scissors"))
if player >= 0 and player <= 2:
    print(game_image[player])

computer = random.randint(0,2)
print("Computer chose:")
print(game_image[computer])

#logic
if player >= 3 or player < 0:
    print("You typed in wrong. You Lose!")
elif computer == 0 and player == 2:
    print("You lose!")
elif player == 0 and computer == 2:
    print("You Win!")
elif computer > player:
    print("you lose!")
elif player > computer:
    print("you win!")

print("Thank you for playing.Hope it was fun!")
