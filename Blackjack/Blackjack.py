import os
import random
from Art import blackjack_logo

#---------------------------------------------------------
def clear():
    os.system('cls' if os.name=='nt' else 'clear')

#---------------------------------------------------------
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

#---------------------------------------------------------
def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 1:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

#---------------------------------------------------------
def compare_score(user_score, dealer_score):
    if user_score > 21 and dealer_score > 21:
        return "You went over. You lose 😤"
    if user_score == dealer_score:
        return "Draw 🙃"
    elif dealer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif dealer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > dealer_score:
        return "You win 😃"
    else:
        return "You lose 😤"

#---------------------------------------------------------
def play_blackjack():
    user_cards = []
    dealer_cards = []
    game_over = False

    print(blackjack_logo)

    for _ in range(2):
        user_cards.append(deal_card())
        dealer_cards.append(deal_card())

    while not game_over:
        user_score = calculate_score(user_cards)
        dealer_score = calculate_score(dealer_cards)

        print(f'Your cards: {user_cards}. Current Score: {user_score}')
        print(f"Dealer's first card: {dealer_cards[0]}")

        if user_score == 0 or dealer_score == 0 or user_score > 21:
            game_over = True
        else:
            did_hit = input("Type 'h' to hit, or any other key to pass: ")
            if did_hit == 'h':
                user_cards.append(deal_card())
            else:
                game_over = True

    while dealer_score != 0 and dealer_score < 17:
        dealer_cards.append(deal_card())
        dealer_score = calculate_score(dealer_cards)

    print(f"Your final hand: {user_cards} Score: {user_score}")
    print(f"Dealer's final hand: {dealer_cards} Score: {dealer_score}")

    print(compare_score(user_score, dealer_score))

#---------------------------------------------------------
def main():
    
    clear()
    print(blackjack_logo)

    while input("Play a game of Blackjack?") == 'y':
        clear()
        play_blackjack()

#---------------------------------------------------------
if __name__ == "__main__":
    main()