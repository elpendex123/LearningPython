import random


def initialize_deck():
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['H', 'D', 'C', 'S']
    return [{'rank': rank, 'suit': suit} for rank in ranks for suit in suits]


def deal_card(deck):
    return deck.pop(random.randint(0, len(deck) - 1))


def calculate_score(cards):
    score = sum(
        int(card['rank']) if card['rank'].isdigit() else 10 if card['rank'] in ['J', 'Q', 'K'] else 11 for card in
        cards)
    num_aces = sum(1 for card in cards if card['rank'] == 'A')
    while score > 21 and num_aces:
        score -= 10
        num_aces -= 1
    return score
