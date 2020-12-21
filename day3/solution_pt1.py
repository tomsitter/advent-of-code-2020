import pdb

def main():
    """ 
    1. Read the input.txt file
    2. Determine rows and columns
    3. Begin traversing by slope until last row, counting "#"
    4. Print total "#" encountered
    """
    tree_cnt = 0
    moves = 0
    with open("./day3/input.txt", "r") as data:
        tree_map = data.read().splitlines()
        rows, cols = len(tree_map[0]), len(tree_map)
        x,y = 0, 0
        run, rise = 3, 1
        
        while y < (cols-1):
            moves += 1
            x = (x+run) % rows
            y = (y+rise)
            if tree_map[y][x] == "#":
                tree_cnt += 1

        print(f"Trees: {tree_cnt}")

def move(pos, slope):
    return list( map(add, pos, slope) )    


if __name__ == "__main__":
    main()