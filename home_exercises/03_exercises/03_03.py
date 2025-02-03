import random

suits_order = {"Hearts": 4, "Spades": 3, "Diamonds": 2, "Clubs": 1}
deck = [(number, suit) for suit in suits_order.keys() for number in range (2, 15)]
random.shuffle(deck)

def format_card(card):
    number_names = {11: "Jack", 12: "Queen", 13: "King", 14: "Ace"}
    rank = number_names.get(card[0], card[0])
    return f"{rank} of {card[1]}"

def card_order(card):
    return (suits_order[card[1]], card[0])

def linear_search(deck, target):
    loops = 0
    for i, card in enumerate(deck):
        loops += 1
        if card == target:
            print(f"Number of loops: {loops}")
            print(f"The target card {format_card(target)} is located on index {i}.")
            return i
    print(f"Number of loops: {loops}")
    print(f"The card {format_card(target)} is not found in the deck.")

def binary_search(deck, target):
    deck.sort(key=card_order)
    left, right = 0, len(deck) - 1
    loops = 0
    while left <= right:
        loops += 1
        mid = (left + right) // 2
        if deck[mid] == target:
            print(f"Number of loops: {loops}")
            print(f"The target {format_card(target)} is located on index {mid}.")
            return mid
        elif card_order(deck[mid]) < card_order(target):
            left = mid + 1
        else:
            right = mid - 1
    print(f"Number of loops: {loops}")
    print(f"The target {format_card(target)} is not found in the list.")

target_card = (12, "Hearts")  # Searching for 10 of Hearts

print("Linear Search:")
linear_search(deck, target_card)

print("\nBinary Search:")
binary_search(deck, target_card)