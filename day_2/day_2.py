import numpy as np
import re

cubes = {
        "blue": 14,
        "green": 13,
        "red": 12
        }

def part_one(lines):

    count = 0
    for line in lines:
        
        pairs = re.findall(r'(\d+) (\w+)', line)

        if all(int(pair[0]) <= cubes[pair[1]] for pair in pairs):
            count += int(line.split(':')[0].split(' ')[-1])

    return count

def part_two(lines):
     
    pauer = 0
    for line in lines:
    
        pairs = re.findall(r'(\d+) (\w+)', line)

        pauer += np.prod(
                [
                    max([int(pair[0]) for pair in pairs if pair[1] == "red"]),
                    max([int(pair[0]) for pair in pairs if pair[1] == "green"]),
                    max([int(pair[0]) for pair in pairs if pair[1] == "blue"])
                ]
                )
    
    return pauer


def main():

     with open("day_2/input.txt", 'r') as f:
        
        lines = [line.strip() for line in f]
        print(f"part 1: {part_one(lines)}, part 2: {part_two(lines)}")

if __name__ == "__main__":
    main()