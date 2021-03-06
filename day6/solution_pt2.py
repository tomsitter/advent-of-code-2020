
import pdb
import itertools

def main():
    """ 
    1. Read the input.txt file
    2. Extract a group of answers
    3. Extract all unique answers from the group
    4. Count how many unique answers appear in the group and add to total
    5. Print the total
    """
    answers = []
    all_answered = 0
    with open("./day6/input.txt", "r") as f:
        raw = f.read().splitlines()

    cur_line = 0
    all_answered = 0
    while cur_line < len(raw):
        group, cur_line = get_next_group(raw, cur_line)
        for u in get_unique_answers(group):
            if all(u in g for g in group): all_answered += 1

    print(all_answered)
       

def get_next_group(raw, cur_line):
    """
    Iterates through the rows of the file appending them to a list, starting at cur_line
    Once a blank row is found, joins all rows into a single string and returns it
    As well as the next row (which would be non-blank)
    """
    group = []
    
    while cur_line < len(raw) and raw[cur_line] != '':
        group.append(raw[cur_line])
        cur_line += 1

    return group, cur_line+1

def get_unique_answers(group):
    """Given a list of lists, return a flattened set with all unique entries"""
    return set(itertools.chain(*group))

if __name__ == "__main__":
    main()