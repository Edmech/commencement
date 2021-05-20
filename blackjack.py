"""

Program Name: Assignment 5
@author: Lance Doyle
Date created: March 31 / 2021
Purpose: This program is an interactive game of Blackjack

"""
import random
import time

players_cards = []
dealers_cards = []


def main():
    """
    ensures the lists are clear of data and starts the program
    """
    players_cards.clear()
    dealers_cards.clear()
    user_choice()


def user_choice():
    """
    This takes the user input for wanting to play the game or not.
    If user decides to play, it then draws the cards for dealer and player, populating the
    two lists
    """

    choice = input('\nWould you like to play a game of Blackjack? Y/N >>> ').upper()

    if choice == 'Y':
        for card in range(0,2):
            print('')
            dealers_cards.append(draw_cards())
            players_cards.append(draw_cards())
        player_turn()
    elif choice == 'N':
        print('\nThanks for playing!')
        exit()
    else:
        print('Please enter a valid Y or N ')
        main()

def draw_cards():
    """
    this randomly generates a "card" between 1 and 10
    """
    cards = random.randint(1,10)
    return cards

def hold():
    """
    This gives the user time to read along with the game
    """
    time.sleep(1)


def player_turn():
    """
    the players turn. Displays both initial sets of cards
    """
    option = 'HIT'
    player_total = sum(players_cards)

    print(f'Your cards are: {players_cards[0]} and {players_cards[1]},\
 Your total is: {player_total}')
    print(f'The dealer shows {dealers_cards[0]}, and one card face down')


    while player_total < 21 and option == 'HIT':
        option = input('\nWould you like to "HIT" or "STAND"? >>> ').upper()

        if option == 'HIT':
            players_cards.append(draw_cards())
            player_total = sum(players_cards)
            print(f'\nYour cards are: {players_cards}. Your total is: {player_total}')

        elif option == 'STAND':
            print(f'\nYou are staying with: {player_total}')
            hold()
            dealer_turn()

        else:
            print('Sorry, you have entered an invalid selection, please start a new game.')
            main()

    if player_total == 21:
        print('You STAND with a total of 21!')
        hold()
        dealer_turn()

    if player_total > 21:
        print('\nYou BUST, thank you for playing\n')
        main()

def dealer_turn():
    """
    The dealers turn, deal cards
    """
    dealer_total = sum(dealers_cards)

    print('\nIt is now the dealers turn\n')
    hold()
    print(f'The dealer shows {dealers_cards}, With a total of {dealer_total}\n')

    while dealer_total <= 16:
        hold()
        print('The dealer will HIT\n')
        time.sleep(1.5) # wanted a moment longer than hold()
        dealers_cards.append(draw_cards())
        dealer_total = sum(dealers_cards)
        print(f'The dealer has cards {dealers_cards}, With a total of {dealer_total}\n')

    if 17 <= dealer_total <=21:
        hold()
        print(f'Dealer has {dealer_total}, The dealer STANDS\n')
        time.sleep(1.5) # wanted a moment longer than hold()
        compare()
    if dealer_total > 21:
        hold()
        print('Dealer BUST! Congratulations, You win!!')
        main()

def compare():
    """
    This compares the dealer and player totals, and declairs the winner
    """
    dealer_total = sum(dealers_cards)
    player_total = sum(players_cards)
    hold()
    print(f'The dealer has {dealer_total}. \nYou have {player_total}.')
    hold()
    if dealer_total == player_total:
        print('The hand is tied, Dealer wins!')
        main()
    if dealer_total < player_total:
        print('Congratulations, you WIN!!')
        main()
    if dealer_total > player_total:
        print('I\'m sorry, Dealer wins.')
        main()





if __name__ == '__main__':
    main()
