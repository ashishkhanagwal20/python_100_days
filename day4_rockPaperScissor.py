import random

choice = int(input("What do you choose?\ntype 0 for rock,1 paper, 2 for scissors"))
computerChoice = random.randint(0, 2)

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
if choice == 0:
    print(rock)
    if computerChoice == 0:
        print('computer choose')
        print(rock)
        print("It's a tie")
    elif computerChoice == 1:
        print('computer choose ')
        print(paper)
        print("computer wins")
    elif computerChoice == 2:
        print('computer choose ')
        print(scissors)
        print("You win")
elif choice == 1:
    print(paper)
    if computerChoice == 0:
        print('computer choose')
        print(rock)
        print("You win")
    elif computerChoice == 1:
        print('computer choose ')
        print(paper)
        print("It's a tie")
    elif computerChoice == 2:
        print('computer choose ')
        print(scissors)
        print("computer wins")
elif choice == 2:
    print(scissors)
    if computerChoice == 0:
        print('computer choose')
        print(rock)
        print("Computer win")
    elif computerChoice == 1:
        print('computer choose ')
        print(paper)
        print("You win")
    elif computerChoice == 2:
        print('computer choose ')
        print(scissors)
        print("It's a tie")
else:
    print("Invalid choice")



