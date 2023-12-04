import numpy as np
import re
from collections import defaultdict

def amount_of_ws(win_cards, my_cards):
    return len(set(win_cards) & set(my_cards))

def part_one(lines):
    sum_ = 0
    for line in lines:
        win_cards, all_cards = line.split(":")[1].split("|")
        w_amount = amount_of_ws(win_cards.split(), all_cards.split())
        sum_ += 2 ** (w_amount - 1) if w_amount > 0 else 0
    return sum_

def part_two(lines):
    
    def fucking_recursion(card, card_wins, cards):

        wins = list(range(card+1, card+1+card_wins[card]))
        cards.update({c:cards[c] + 1 + cards[card] for c in wins})

        if card +1 in card_wins.keys():
            cards = fucking_recursion(card+1, card_wins, cards)
            
        return cards

    init_card_wins = defaultdict(lambda: 0)

    for line in lines:
        card = int(line.split(":")[0].split()[1])
        win_cards, all_cards = line.split(":")[1].split("|")

        init_card_wins[card] += amount_of_ws(win_cards.split(), all_cards.split())

    cards = fucking_recursion(1, init_card_wins, defaultdict(lambda: 0))
    
    # add the initial wins
    return sum(list({c: cards[c] + 1 for c in init_card_wins.keys()}.values()))

def main():

     with open("day_4/input.txt", 'r') as f:
        
        lines = [line.strip() for line in f]
        print(f"part 1: {part_one(lines)}, part 2: {part_two(lines)}")

if __name__ == "__main__":
    main()