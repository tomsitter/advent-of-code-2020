import pdb
import math

def main():
    """ 
    1. Read the input.txt file
    2. Determine row, aisle for each boarding pass
    3. Calculate seat ID
    4. Return max seat ID
    """
    max_seat_id = 0
    with open("./day5/input.txt", "r") as f:
        passes = f.read().splitlines()
        
    seats = []
    for p in passes:
        row, aisle = p[:7], p[7:]
        row_range = (0,127)
        aisle_range = (0, 7)
        for c in row:
            row_range = split_seat(c, *row_range)
        for c in aisle:
            aisle_range = split_seat(c, *aisle_range)
        seats.append((row_range[0], aisle_range[0]))

    for seat in seats:
        max_seat_id = max(max_seat_id, seat_id(*seat))

    print(max_seat_id)
    

def split_seat(c, low, high):
    span = high - low
    if c in ('F', 'L'):
        # take bottom half
        return (low, high-math.ceil(span/2))
    else:
        return (low+math.ceil(span/2), high)

def seat_id(row, aisle):
    return row*8 + aisle

if __name__ == "__main__":
    main()