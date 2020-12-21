from itertools import combinations
from functools import reduce

def main():
    """ 
    1. Read the input.txt file in a sorted list
    2. Generate every possible combination of 3 numbers
    3. If the sum is == 2020, print the product of the 3 numbers
    """
    with open("./day1/input.txt", "r") as data:
        entries = [int(x) for x in data.readlines()]
        
        combs = combinations(entries, 3)

        for comb in combs:
            if sum(comb) == 2020:
                print(reduce(lambda x,y: x*y, comb))
                break


if __name__ == "__main__":
    product = main()