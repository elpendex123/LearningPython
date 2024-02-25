import random

def initialize_deck():
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['H', 'D', 'C', 'S']
    return [{'rank': rank, 'suit': suit} for rank in ranks for suit in suits]

def deal_card(deck):
    return deck.pop(random.randint(0, len(deck)-1))

def calculate_score(cards):
    score = sum(int(card['rank']) if card['rank'].isdigit() else 10 if card['rank'] in ['J', 'Q', 'K'] else 11 for card in cards)
    num_aces = sum(1 for card in cards if card['rank'] == 'A')
    while score > 21 and num_aces:
        score -= 10
        num_aces -= 1
    return score

def blackjack():
    while True:
        decks = initialize_deck() * 8
        player_hand = [deal_card(decks), deal_card(decks)]
        dealer_hand = [deal_card(decks), deal_card(decks)]

        def display_hands(show_all=False):
            me_hand = ', '.join([f"{card['rank']}{card['suit']}" for card in player_hand])
            dealer_hand_str = ', '.join([f"{card['rank']}{card['suit']}" for card in dealer_hand])
            print(f"Me: {me_hand}, score: {calculate_score(player_hand)}")
            if show_all:
                print(f"Dealer: {dealer_hand_str}, score: {calculate_score(dealer_hand)}")
            else:
                print(f"Dealer: {dealer_hand[0]['rank']}{dealer_hand[0]['suit']}, ???")

        def handle_split():
            nonlocal player_hand, decks
            if player_hand[0]['rank'] == player_hand[1]['rank']:
                if player_hand[0]['rank'] in ['10', 'J', 'Q', 'K'] and player_hand[1]['rank'] in ['10', 'J', 'Q', 'K']:
                    print("Splitting your hand!")
                    player_hand = [[player_hand[0], deal_card(decks)], [player_hand[1], deal_card(decks)]]
                elif player_hand[0]['rank'] == 'A':
                    print("Cannot split aces.")
                else:
                    print("Splitting your hand!")
                    player_hand = [[player_hand[0], deal_card(decks)], [player_hand[1], deal_card(decks)]]

        def handle_double_down():
            nonlocal player_hand, decks
            if len(player_hand) == 2:
                print("Doubling down!")
                player_hand.append(deal_card(decks))
                # End the player's turn after doubling down
                return True
            return False

        def play_round():
            nonlocal player_hand, dealer_hand, decks
            player_blackjack = calculate_score(player_hand) == 21
            player_busted = False
            player_wins = False

            # Check for dealer's blackjack
            if calculate_score(dealer_hand) == 21:
                display_hands(show_all=True)
                if player_blackjack:
                    print("It's a tie! Both have blackjack.")
                else:
                    print("Dealer has blackjack. You lose.")
                return

            while not player_busted and not player_blackjack:
                display_hands()
                if len(player_hand) == 2:
                    options = "Type 'h' to hit, 's' to stand, 'd' to double down"
                    if player_hand[0]['rank'] == player_hand[1]['rank']:
                        handle_split()
                        options += ", 'p' to split"
                    if player_hand[0]['rank'] in ['10', 'J', 'Q', 'K']:
                        handle_split()
                        options += ", 'p' to split"
                    action = input(f"{options}: ").lower()
                    if action == 'd':
                        if handle_double_down():
                            # End the player's turn after doubling down
                            break
                    elif action == 'h':
                        player_hand[0].append(deal_card(decks))
                    elif action == 's':
                        break
                else:
                    action = input("Type 'h' to hit, 's' to stand: ").lower()
                    if action == 'h':
                        player_hand[0].append(deal_card(decks))
                    elif action == 's':
                        break

                player_score = calculate_score(player_hand[0])
                if len(player_hand[0]) == 2 and player_score == 21:  # Check for blackjack only on the first 2 cards
                    player_blackjack = True
                elif player_score > 21:
                    player_busted = True

            # Continue with the dealer's turn
            while calculate_score(dealer_hand) < 17:
                dealer_hand.append(deal_card(decks))

            display_hands(show_all=True)

            if player_busted:
                print("You busted. You lose.")
            else:
                if calculate_score(dealer_hand) > 21:
                    player_wins = True
                elif calculate_score(player_hand[0]) > calculate_score(dealer_hand):
                    player_wins = True

                if player_blackjack:
                    if calculate_score(dealer_hand) == 21:
                        print("It's a tie! Both have blackjack.")
                    else:
                        print("Blackjack! You win!")
                elif player_wins:
                    print("You win!")
                elif calculate_score(player_hand[0]) == calculate_score(dealer_hand):
                    print("It's a draw.")
                else:
                    print("You lose.")

        play_round()

        print("-----------------------------------------------------------------------------------------------")

        play_again = input("Press 'c' to continue playing, 'q' to quit: ").lower()
        if play_again != 'c':
            break

# Run the game
blackjack()
