
import pdb
import itertools

def main():
    """ 
    1. Read the input.txt file
    2. Extract a single passport
    3. Extract all fields from a passport into a dict
    4. Add new key to passport if it has all the required keys
    5. Count the # of passports that are valid
    """    
    with open("./day6/input.txt", "r") as f:
        raw = f.read().splitlines()

    cur_line = 0
    answer_cnt = 0
    while cur_line < len(raw):
        group, cur_line = get_next_group(raw, cur_line)
        unq_answers = get_unique_answers(group)
        answer_cnt += len(unq_answers)

    print(answer_cnt)
       

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
    return set(itertools.chain(*group))



if __name__ == "__main__":
    main()