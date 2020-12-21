import pdb
from functools import reduce

#import numpy as np

def main():
    """ 
    1. Read the input.txt file
    2. Determine rows and columns
    3. Begin traversing by slope until last row, counting "#"
    4. Return # of trees encountered
    5. Once all slopes tested, multiple # of trees encountered for each slope
    """
    with open("./day3/input.txt", "r") as data:
        tree_map = data.read().splitlines()
        slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]

        tree_cnts = []
        for slope in slopes:
            tree_cnts.append(cnt_trees(tree_map, slope))

        print(f"Counts for each slope: {tree_cnts}")
        print(f"Product of all counts: {reduce(lambda x,y: x*y, tree_cnts)}")

def cnt_trees(tree_map, slope):
    rows, cols = len(tree_map[0]), len(tree_map)
    x,y = 0, 0
    tree_cnt = 0
    run,rise = slope

    while y < (cols-1):
        x = (x+run) % rows
        y = (y+rise)
        if tree_map[y][x] == "#":
            tree_cnt += 1
    
    return tree_cnt

if __name__ == "__main__":
    main()