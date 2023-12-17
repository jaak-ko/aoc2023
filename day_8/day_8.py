import numpy as np
import re
from collections import deque

def part_one(nodes, turns):

    current = "AAA"
    amount = 0
    while True:
        current = nodes[current][0] if turns[0] == 'L' else nodes[current][1]
        amount += 1
        turns.rotate(-1)
        if current == "ZZZ":
            return amount
        

def part_two(nodes, turns):
    pass

def main():

     with open("day_8/input.txt", 'r') as f:
        lines = [line.strip() for line in f]

        turns = deque(lines[0])
        nodes = {}

        for row in lines[2:]:
            ls = re.findall(r"\b[A-Z]{3}\b", row)
            nodes.update({ls[0]: (ls[1], ls[2])})

        print(f"part 1: {part_one(nodes, turns)}\npart 2: {part_two(nodes, turns)}")

if __name__ == "__main__":
    main()