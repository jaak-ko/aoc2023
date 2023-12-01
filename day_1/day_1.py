import numpy as np

def part_one(lines):

    int_lines = [[i for i in line if i.isdigit()] for line in lines]
    
    return sum([int(line[0] + line[-1]) for line in int_lines])

def part_two(lines):

    digits = {"one": '1', "two": '2', "three": '3', "four": '4', "five": '5', 
                "six": '6', "seven": '7', "eight": '8', "nine": '9', "zero": '0'}

    new_lines = []
    for line in lines:
        new_line = []

        for f in range(len(line.strip())):
            if line[f].isdigit():
                new_line.append(line[f])
                continue

            for i in [3, 4, 5]:
                if line[f:f+i] in digits.keys():
                    new_line.append(digits[line[f:f+i]])
                    break

        new_lines.append(new_line)  

    return sum([int(line[0] + line[-1]) for line in new_lines])


def main():

    with open("day_1/input.txt", 'r') as f:
        
        lines = f.readlines()
        print(f"part 1: {part_one(lines)}, part 2: {part_two(lines)}")

if __name__ == "__main__":
    main()