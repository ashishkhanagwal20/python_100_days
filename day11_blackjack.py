import random
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal_card():
    card = random.choice(cards)
    return card


def calculate_score(arr):
    if 11 in arr and 10 in arr:
        return 0

    if 11 in arr and sum(arr)>21:
        arr.remove(11)
        arr.append(1)

    score = 0
    for item in arr:
        score += item


    return score

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "You Lose,opponent blackjack(Zero)"
    elif user_score == 0:
        return "Win with a blackjack(Zero)"
    elif user_score > 21:
        return "You went over, You lose"
    elif computer_score >21:
        return "Opponent went over, you win"
    elif user_score > computer_score:
        return "You win(score> computer)"
    else:
        return "You lose!!(score < computer)"



def play_game():
    logo = """
    .------.            _     _            _    _            _    
    |A_  _ |.          | |   | |          | |  (_)          | |   
    |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
    | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
    |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
    `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
          |  \/ K|                            _/ |                
          `------'                           |__/           
    """
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"user cards:{user_cards} and score:{user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"your final hand is {user_cards} and score is {user_score} ")
    print(f"computer's final hand {computer_cards} and computer score {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of blackjack? Type 'y' or 'n': ") == 'y':
    os.system('cls')
    play_game()








