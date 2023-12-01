import numpy as np


def part_one(lines):

    int_lines = [list(filter(lambda x: x.isdigit(), line)) for line in lines]

    return sum([int(line[0] + line[-1]) for line in int_lines])

def part_two(lines):

    for i in range(len(lines)):
        lines[i] = list(filter(lambda x: x.isdigit(), \
                        lines[i].replace('one', 'one1one').\
                        replace('two', 'two2two').\
                        replace('three', 'three3three').\
                        replace('four', 'four4four').\
                        replace('five', 'five5five').\
                        replace('six', 'six6six').\
                        replace('seven', 'seven7seven').\
                        replace('eight', 'eight8eight').\
                        replace('nine', 'nine9nine')))
                        
        
    return sum([int(line[0] + line[-1]) for line in lines])

def main():

    with open("day_1/input.txt", 'r') as f:
        
        lines = [line.strip() for line in f]
        print(f"part 1: , part 2: {part_two(lines)}")

if __name__ == "__main__":
    main()