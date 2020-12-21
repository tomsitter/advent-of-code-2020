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
            first, last = [int(c) for c in count_range.split("-")]
            ch = ch[:-1]
            pw = password.strip("\n")

            if is_valid(first, last, ch, pw):
                valid += 1

        print(valid)

def is_valid(first, last, ch, pw):
    return (pw[first-1] == ch)  != (pw[last-1] == ch)


if __name__ == "__main__":
    main()