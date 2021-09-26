"""
Week 13 Assignment 5 - Thomas Kiernan
Blackjack / Twenty-one
Blackjack is a popular card game. The objective of the game is to draw cards and obtain the highest total not exceeding 21.

Simplified game requirements
The possible card values range from 1 to 10 and, unlike a real deck, the probability of drawing a card is equal
The game begins by dealing two visible cards to the player, and two cards to the dealer. However, in the case of the dealer, one card is visible to other player while the other is hidden.
The player decides whether to "hit" (draw another card), or "stand" which ends their turn.
The player may hit any number of times. Should the total of the cards exceed 21, the player "busts" and loses the game to the dealer. The round then ends and the dealer does not have to draw/show any additional cards.
If the player reaches 21, the player stands
The dealer's turn begins by revealing the hidden card
The dealer must continue to hit if the total is 16 or less, and must stand if the value is 17 or more
The dealer busts if their total is over 21 and the player wins.
The dealer wins all ties (i.e. if both the dealer and the player reach 21, the dealer wins)
The program indicates who the winner is and asks to play again
It is up to you as the developer on how you will choose to handle invalid user input, but note the program cannot crash upon invalid input. Options can involve asking the user again or exiting the program with a user-friendly message.
"""

import random
import sys
import time
import msvcrt

def main():

    global player_cards
    global dealer_cards

    while True:
        print('\nHello, would you like to play a game of BlackJack? ')
        playing_blackjack = msvcrt.getch()
        time.sleep(.1)
        if playing_blackjack == b'N' or playing_blackjack == b'n':
            print('Ok.  Have a nice day')
            sys.exit()
        elif playing_blackjack == b'Y' or playing_blackjack == b'y':
            break
        else:
            print('Please type Y or N\n')

    while True:
        player_cards = []
        dealer_cards = []
        end_game = False

        deal_1st_cards()
        print (f'\nYour hand    ', end="")
        print (*player_cards)
        print (f'Dealer hand  {dealer_cards[0]} ?')
        print (f'Player has {sum(player_cards)} and the Dealer shows a {dealer_cards[0]}')

        end_game = players_turn()  #there are better ways to do this but I wanted to play wiht a returned value from the function
        if end_game != True:
            dealers_turn()
        play_again()

def get_card():
    CARDS = [10,9,8,7,6,5,4,3,2,1]
    return random.choice(CARDS)

def deal_1st_cards():
    # deal cards - player dealer player dealer (real life sequence)
    card = get_card()
    player_cards.append(card)
    card = get_card()
    dealer_cards.append(card)
    card = get_card()
    player_cards.append(card)
    card = get_card()
    dealer_cards.append(card)

def players_turn():
    end_game = False
    while sum(player_cards) < 21:
        print('Hit (h) or Stand (s)? ', end="", flush = True)
        deal_card = msvcrt.getch()
        time.sleep(.25)
        if deal_card == b'S' or deal_card == b's':
            print('Stand \n')
            break
        elif deal_card == b'H' or deal_card == b'h':
            print('Hit')
            card = get_card()
            player_cards.append(card)
            print (f'\nYour hand  ', end="")
            print (*player_cards)
            if sum(player_cards) < 21:
                print (f'Player has {sum(player_cards)} and the Dealer shows {dealer_cards[0]}')
        if sum(player_cards) == 21:
            print('You hit 21!\n')
        if sum(player_cards) > 21:
            print(f'You busted with {sum(player_cards)} and the Dealer wins!')
            print("The dealer had ", end = "")
            print(*dealer_cards)
            end_game = True
            return end_game

def dealers_turn():
    print(f'Dealer shows ', end = "")
    print(*dealer_cards)
    while True:
    #    if sum(dealer_cards) > 16:
        if sum(dealer_cards) > 21:
            print(f'Dealer busted with {sum(dealer_cards)}! You win!')
            break
        elif sum(dealer_cards) == 21:
            print('Dealer hits 21!  You loose!')
            break
        elif sum(dealer_cards) >= sum(player_cards):
            print(f'Dealer wins with {sum(dealer_cards)} over your {sum(player_cards)}!')
            break
        elif sum(dealer_cards) > 16 and sum(dealer_cards) < sum(player_cards):
            print(f"You win with {sum(player_cards)} over the Dealer's {sum(dealer_cards)}!")
            break
        if sum(dealer_cards) <= 16: #and sum(dealer_cards) < sum(player_cards):
            card = get_card()
            dealer_cards.append(card)
            print (f'Dealer draws ', end="")
            print (*dealer_cards)
            print (f'Dealer has {sum(dealer_cards)} : Player has {sum(player_cards)}\n')
        time.sleep(1)

def play_again():
    while True:
        print ('\nWould you like to play again?')
        want_to_play = msvcrt.getch()
        time.sleep(.1)
        if want_to_play == b'N' or want_to_play == b'n':
            print('Ok.  Have a nice day')
            playing_blackjack = False
            sys.exit()
        elif want_to_play == b'Y' or want_to_play == b'y':
            print('Another round!')
            time.sleep(1)
            break
        else:
            print('Please type Y or N\n')

if __name__ == '__main__':
    main()
