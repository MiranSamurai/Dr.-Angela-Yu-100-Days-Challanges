import random

import art

print(art.logo)



def BlackJack():

    players_cards = []
    computer_cards = []
    computer_total = 0

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    players_card1 = random.choice(cards)
    players_cards = [players_card1]
    computer_card1 = random.choice(cards)
    computer_card2 = random.choice(cards)
    computer_cards = [computer_card1]
    should_play = input("do you want to play a game of BlackJack (Y)es or (N)o: ").lower()
    if should_play == "y":
        continue_Playing = True


        while continue_Playing:
            players_cards.append(random.choice(cards))
            for computer in computer_cards:
                computer_total += computer
            if computer_total < 21 :
                if random.choice([True, False]):
                    computer_cards.append(random.choice(cards))


            players_total = 0
            computer_total = 0
            for player in players_cards:
                players_total +=player


            print(f"your cards are{players_cards}, current score : {players_total}")
            if len(computer_cards) == 1:
                print(f"computers First Card is: {computer_cards[0]}")
            else:
                print(f"computers First Card is {computer_cards[0]}")
            if players_total > 21:
                print(
                    f"your  final cards are {players_cards} score is :{players_total}\n Computers Final cards are {computer_cards} score is: {computer_total}")
                print("You went Over , You Lost")
                print("\n" * 20)
                BlackJack()
            choice = input("type 'y' to draw another card or type 'n' to pass: ").lower()
            if choice == "n":
                continue_Playing = False
                if players_total > computer_total:
                        print(f"your  final cards are {players_cards} score is :{players_total}\n Computers Final cards are {computer_cards} score is: {computer_total}")
                        print("you win")
                        print("\n" * 20)
                        BlackJack()

                elif players_total < computer_total :
                    print(f"your  final cards are {players_cards} score is :{players_total}\n Computers Final cards are {computer_cards} score is: {computer_total}")
                    print("you Lose")
                    print("\n" * 20)
                    BlackJack()





BlackJack()


