import numpy as np
import re
from collections import deque


def parts(lines):
    
    nexts = {"left": [], "right": []}
    for h in lines:
        hs = [deque(map(int, re.findall(r'[+-]?\d+', h))), ]        
        while any(item != 0 for item in hs[-1]):
            hs.append(deque([hs[-1][i+1] - hs[-1][i] for i in range(len(hs[-1])-1)]))

        for i in range(len(hs)-2, -1, -1):
            hs[i].append(hs[i+1][-1] + hs[i][-1])
            hs[i].appendleft(hs[i][0] - hs[i+1][0])

        nexts["right"].append(hs[0][-1])
        nexts["left"].append(hs[0][0])

    return sum(nexts["right"]), sum(nexts["left"])

def main():

     with open("day_9/input.txt", 'r') as f:
        
        lines = [line.strip() for line in f]
        print(f"part 1: {parts(lines)[0]}\npart 2: {parts(lines)[-1]}")

if __name__ == "__main__":
    main()