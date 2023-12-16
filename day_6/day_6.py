import numpy as np
import re

def parts(lines):

    times = [int(i) for i in re.findall(r'\d+', lines[0])]
    dists = [int(i) for i in re.findall(r'\d+', lines[1])]

    p2_time = int(''.join([str(i) for i in times]))
    p2_dist = int(''.join([str(i) for i in dists]))

    sums = np.zeros(len(times))
    sum_ = 0

    for idx, t in enumerate(times):
            for t_ in range(int(t)):
                if (t-t_) * t_ > int(dists[idx]):
                    sums[idx] += 1 

    for t_ in range(int(p2_time)):
        if (p2_time-t_) * t_ > p2_dist:
            sum_ += 1 

    return int(np.prod(sums)), sum_

def main():

     with open("day_6/input.txt", 'r') as f:
        
        lines = [line.strip() for line in f]
        p1, p2 = parts(lines)
        print(f"part 1: {p1}\npart 2: {p2}")

if __name__ == "__main__":
    main()