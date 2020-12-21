import pdb

def main():
    """ 
    1. Read the input.txt file
    2. Parse the password rule
    3. Count each character to see if it is within the rules
    4. If valid, increase valid count by 1
    """
    with open("./day2/input.txt", "r") as data:
        entries = data.readlines()
        print(len(entries))
        valid = 0

        for entry in entries:
            count_range, ch, password = entry.split()
            min_cnt, max_cnt = [int(c) for c in count_range.split("-")]
            ch = ch[:-1]
            pw = password.strip("\n")

            if is_valid(min_cnt, max_cnt, ch, pw):
                valid += 1

        print(valid)

def is_valid(min_cnt, max_cnt, ch, pw):
    cnt = pw.count(ch)
    #pdb.set_trace()
    if not (min_cnt <= cnt <= max_cnt):
        return False
    return True

if __name__ == "__main__":
    main()