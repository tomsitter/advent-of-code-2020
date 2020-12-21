import pdb
import re
from functools import partial

def main():
    """ 
    1. Read the input.txt file
    2. Extract a single passport
    3. Extract all fields from a passport into a dict
    4. Check each passport if it has all the required keys and each key meets the validation criteria
    5. Count the # of passports that are valid
    """
    passports = []
    valid_cnt = 0
    validations = {
        'byr': partial(valid_year, 1920, 2002),
        'iyr': partial(valid_year, 2010, 2020),
        'eyr': partial(valid_year, 2020, 2030),
        'hgt': valid_hgt,
        'hcl': valid_hcl,
        'ecl': valid_ecl,
        'pid': valid_pid,
    }

    with open("./day4/input.txt", "r") as f:
        raw = f.read().splitlines()
        cur_line = 0
        while cur_line < len(raw):
            passport, cur_line = get_next_passport(raw, cur_line)
            pp = parse_passport(passport)

            if has_req_keys(validations.keys(), pp): 
                if all(validations[key](pp[key]) for key in validations.keys()):
                    valid_cnt += 1
    
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

def has_req_keys(req_keys, passport):
    return all(key in passport.keys() for key in req_keys)

def valid_year(min_yr, max_yr, fld):
    """
    byr - 1920 - 2002
    iyr - 2010 - 2020
    eyr - 2020 - 2030
    """
    return min_yr <= int(fld) <= max_yr

def valid_hcl(hcl):
    return re.match('^#[0-9a-f]{6}$', hcl) is not None

def valid_hgt(hgt):
    measure, units = int(hgt[0:-2]), hgt[-2:]
    if units == 'cm':
        return 150 <= measure <= 193
    elif units == 'in':
        return 59 <= measure <= 76
    else:
        return False

def valid_ecl(ecl):
    return ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def valid_pid(pid):
    return re.match('^\d{9}$', pid) is not None
    
if __name__ == "__main__":
    main()