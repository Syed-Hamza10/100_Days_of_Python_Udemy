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

game_list = [rock, paper, scissors]

user_input = int(input('What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors\n'))
computer_input = random.randint(0, 2)

print(game_list[user_input])
print(f'Computer Choose:\n {game_list[computer_input]}')

if user_input == computer_input:
    print('It\'s a Draw')
elif (user_input == 0 and computer_input == 2) or \
     (user_input == 1 and computer_input == 0) or \
     (user_input == 2 and computer_input == 1):
    print('You Win.')
else:
    print('Computer Wins.')