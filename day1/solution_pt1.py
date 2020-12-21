
def main():
    """ 
    1. Read the input.txt file in a sorted list
    2. Sum the lowest and highest value in the list of numbers
    3. If the sum is > 2020, then we need to decrease the highest number,
       if the sum is < 2020, then we need to increase the lowest number
    4. Iterate until a solution is found and print the results.
    """
    with open("./day1/input.txt", "r") as data:
        entries = sorted([int(x) for x in data.readlines()])
        low, high = 0, len(entries)-1

        total = entries[low]+entries[high]
         
        while total != 2020:
            if total < 2020:
                low += 1
            else:
                high -= 1
            total = entries[low]+entries[high]

        print(entries[low]*entries[high])

if __name__ == "__main__":
    main()