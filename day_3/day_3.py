import numpy as np
import re

def extract_nums_and_marks(lines):
    nums = {}
    marks = {}
    for y, row in enumerate(lines):
        nums.update(
            {(y, (i.start(), i.end())): int(i.group()) for i in re.finditer(r"(\d+)", row)})
        marks.update(
            {(y, (i.start())): i.group() for i in re.finditer(r"[^\d.]", row)})
        
    return nums, marks


def part_one(lines):

    # return true if mark is adjacent to num
    def is_adjacent_to_num(marks, num):

        possible_ys = range(num[0] - 1, num[0] + 2)
        possible_xs = range(num[1][0] - 1, num[1][1] + 1)

        return any((mark[0][0] in possible_ys and mark[0][1] in possible_xs) for mark in marks.items())
    
    nums, marks = extract_nums_and_marks(lines)
    
    return sum(dict(filter(lambda x: is_adjacent_to_num(marks, x[0]), nums.items())).values())
    

def part_two(lines):

    # return true if num is adjacent to mark
    def is_adjacent_to_mark(num, mark):
        if num == (9, (1, 3)):
            print(mark)

        possible_ys = range(mark[0] - 1, mark[0] + 2)
        possible_xs = range(mark[1] - 1, mark[1] + 2)
        
        return num[0] in possible_ys and any(i in possible_xs for i in range(num[1][0], num[1][1]))
    
    # if has excatly 2 gears, return gear ratio, else return 0 
    def gear_ratio(mark, nums):

        maybe_gear_ratios = dict(filter(lambda x: is_adjacent_to_mark(x[0], mark[0]), nums.items()))

        if len(maybe_gear_ratios) == 2:
            return np.prod(list(maybe_gear_ratios.values()))
        
        return 0
            
    nums, marks = extract_nums_and_marks(lines)

    possible_gears = dict(list(filter(lambda x: x[1] == '*', marks.items())))
    
    return sum([gear_ratio(x, nums) for x in possible_gears.items()]) # return sum of gear ratios


def main():

     with open("day_3/input.txt", 'r') as f:
        
        lines = [line.strip() for line in f]
        print(f"part 1: {part_one(lines)}, part 2: {part_two(lines)}")

if __name__ == "__main__":
    main()