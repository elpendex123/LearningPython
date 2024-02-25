from bj_utils.deck import initialize_deck, deal_card, calculate_score


def display_hands(player_hand, dealer_hand, show_all=False):
    me_hand = ', '.join([f"{card['rank']}{card['suit']}" for card in player_hand])
    dealer_hand_str = ', '.join([f"{card['rank']}{card['suit']}" for card in dealer_hand])
    print(f"Me: {me_hand}, score: {calculate_score(player_hand)}")
    if show_all:
        print(f"Dealer: {dealer_hand_str}, score: {calculate_score(dealer_hand)}")
    else:
        print(f"Dealer: {dealer_hand[0]['rank']}{dealer_hand[0]['suit']}, ???")


def handle_split(player_hand, decks):
    if len(player_hand) == 2 and player_hand[0]['rank'] == player_hand[1]['rank']:
        if player_hand[0]['rank'] in ['10', 'J', 'Q', 'K']:
            print("Splitting your hand!")
            return [player_hand[0], deal_card(decks)], [player_hand[1], deal_card(decks)]
        elif player_hand[0]['rank'] == 'A':
            print("Cannot split aces.")
        else:
            print("Splitting your hand!")
            return [player_hand[0], deal_card(decks)], [player_hand[1], deal_card(decks)]
    return None


def handle_double_down(player_hand, decks):
    if len(player_hand) == 2:
        print("Doubling down!")
        player_hand.append(deal_card(decks))
        return True
    return False


def play_round():
    decks = initialize_deck() * 8
    player_hand = [deal_card(decks), deal_card(decks)]
    dealer_hand = [deal_card(decks), deal_card(decks)]

    player_blackjack = calculate_score(player_hand) == 21
    player_busted = False
    player_wins = False

    while not player_busted and not player_blackjack:
        display_hands(player_hand, dealer_hand)
        if len(player_hand) == 2:
            options = "Type 'h' to hit, 's' to stand, 'd' to double down"
            split_result = handle_split(player_hand, decks)
            if split_result:
                player_hand = split_result
                break
            if handle_double_down(player_hand, decks):
                # End the player's turn after doubling down
                break
            action = input(f"{options}: ").lower()
            if action == 'h':
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

    display_hands(player_hand, dealer_hand, show_all=True)

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


def blackjack():
    while True:
        play_round()
        print("-----------------------------------------------------------------------------------------------")
        play_again = input("Press 'c' to continue playing, 'q' to quit: ").lower()
        if play_again != 'c':
            break


# Run the game if this file is executed directly
if __name__ == "__main__":
    blackjack()
