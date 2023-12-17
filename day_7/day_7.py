import numpy as np
import re

cr1 = "AKQJT98765432"
cr2 = cr1.replace('J','') + 'J'

hand_ranks = {
    "five_of_kind": 7,
    "four_of_kind": 6,
    "full_house": 5,
    "three_of_kind": 4,
    "two_pair": 3,
    "one_pair": 2,
    "high_card": 1
}

def hand_type(hand):
    if len(set(hand)) ==  5:
        return "high_card"
    elif len(set(hand)) == 4 and any(hand.count(x) == 2 for x in hand):
        return "one_pair"
    elif len(set(hand)) == 3 and any(hand.count(x) == 3 for x in hand):
        return "three_of_kind"
    elif len(set(hand)) == 2 and any(hand.count(x) == 3 for x in hand):
        return "full_house"
    elif len(set(hand)) == 2 and any(hand.count(x) == 4 for x in hand):
        return "four_of_kind"
    elif len(set(hand)) == 1:
        return "five_of_kind"
    return "two_pair"

def rank1(hand):
        
        return (hand_ranks[hand_type(hand)], 
                *[len(cr1) - cr1.index(c) for c in hand])

def rank2(item):
        if not isinstance(item[1], tuple):
             return rank1(item[0])
        
        return (hand_ranks[hand_type(item[1][1])], 
                *[len(cr2) - cr2.index(c) for c in item[0]])
    
def part_one(cards):

    cards = dict(sorted(cards.items(), key=lambda item: rank1(item[0])))
    return sum([i[1] * (idx+1) for idx, i in enumerate(cards.items())])


def part_two(cards):

    for card in cards:
        if not 'J' in card:
             cards.update({card: (cards[card], card)})
             continue

        hand_on_juice = sorted([card.replace('J', c) for c in cr2], key=rank1)[-1]
        cards.update({card: (cards[card], hand_on_juice)})

    cards = dict(sorted(cards.items(), key=lambda item: rank2(item)))
    return sum([i[1][0] * (idx+1) for idx, i in enumerate(cards.items())])

def main():

     with open("day_7/input.txt", 'r') as f:
        
        lines = [line.strip() for line in f]

        cards = {i.split()[0]: int(i.split()[1]) for i in lines}

        print(f"part 1: {part_one(cards)}\npart 2: {part_two(cards)}")

if __name__ == "__main__":
    main()