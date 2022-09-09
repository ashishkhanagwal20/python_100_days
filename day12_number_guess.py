import random

print("Welcome to the number guessing game!")
print("I'am thinking of a number between 1 and 100.")
choosen_number = random.randint(1,100)
attempts = 0
is_number_guessed  = False
print(choosen_number)

difficulty = input("Choose a difficulty( type easy,medium or hard): ")

if difficulty == "hard":
    attempts = 5
elif difficulty == "medium":
    attempts = 8
else:
    attempts = 10

while not is_number_guessed or attempts == 0:
    print(f"you have {attempts} attempts remaining to guess the number")
    guessed_number = int(input("Make a guess: "))
    if guessed_number == choosen_number:
        print("You win")
        is_number_guessed = True
    elif guessed_number > choosen_number:
        attempts -= 1
        print("Too high")
    else:
        attempts-=1
        print("Too low")


