import pdb

def main():
    """ 
    1. Read the input.txt file
    2. Extract a single passport
    3. Extract all fields from a passport into a dict
    4. Add new key to passport if it has all the required keys
    5. Count the # of passports that are valid
    """
    passports = []
    valid_cnt = 0
    with open("./day4/input.txt", "r") as f:
        raw = f.read().splitlines()
        cur_line = 0
        while cur_line < len(raw):
            passport, cur_line = get_next_passport(raw, cur_line)
            passports.append(parse_passport(passport))
        
        for pp in passports:
            if is_valid_passport(pp): valid_cnt += 1
    
    print(valid_cnt)
       

def get_next_passport(raw, cur_line):
    """
    Iterates through the rows of the file appending them to a list, starting at cur_line
    Once a blank row is found, joins all rows into a single string and returns it
    As well as the next row (which would be non-blank)
    """
    passport = []
    
    while cur_line < len(raw) and raw[cur_line] != '':
        passport.append(raw[cur_line])
        cur_line += 1

    return " ".join(passport), cur_line+1

def parse_passport(passport):
    kvs = passport.split(" ")
    return {key:value for (key,value) in [kv.split(":") for kv in kvs]} 

def is_valid_passport(passport):
    req_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    is_valid = True
    if all(key in passport.keys() for key in req_keys):
        if 
    else:
        is_valid = False
    
    return is_valid

if __name__ == "__main__":
    main()