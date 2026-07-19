"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://python.org
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers."""
    return [number, number + 1, number + 2]


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers."""
    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number."""
    return number in rounds


def card_average(hand):
    """Calculate and returns the average card value from the list."""
    return sum(hand) / len(hand)


def approx_average_is_average(hand):
    """Check if approximate averages match the actual average."""
    true_avg = card_average(hand)
    
    first_last_avg = (hand[0] + hand[-1]) / 2
    middle_card = hand[len(hand) // 2]
    
    return true_avg in (first_last_avg, middle_card)


def average_even_is_average_odd(hand):
    """Check if even-indexed and odd-indexed card averages match."""
    even_cards = hand[::2]
    odd_cards = hand[1::2]
    
    even_avg = sum(even_cards) / len(even_cards)
    odd_avg = sum(odd_cards) / len(odd_cards)
    
    return even_avg == odd_avg


def maybe_double_last(hand):
    """Multiply a Jack (11) in the last index position by 2."""
    if hand[-1] == 11:
        hand[-1] = 22
    return hand
