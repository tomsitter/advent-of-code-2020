import pdb
import itertools
import re

def main():
    """ 
    1. Read the input.txt file
    2. Parse out the colour and the bags it can hold into a {key: [values]} dict
    3. Sol'n part 1:
    4. Iterate through each bag and determine if it holds our target colour, if not
        recursivley check each colour it holds to see if any of them can hold the target colour
    5. Print the total number of bags that can hold our bag
    6. Sol'n part 2:
    7. For each bag in our target bag, count how many are held, then recursively check how many
        they hold and so forth
    8. Print the total number of bags in bags - 1 (for the target bag which is excluded)
    """    
    with open("./day7/input.txt", "r") as f:
        lines = f.read().splitlines()
    
    bags = {}
    bag_count = 0
    for line in lines:
        colour = re.match(r'(.+?) bags contain', line)[1]
        bags[colour] = re.findall(r'(\d+?) (.+?) bags?', line)

    target_colour = "shiny gold"
    for bag in bags:
        if holds_colour(target_colour, bags):
            bag_count += 1
    print(bag_count)

    bags_in_bags = count_bags(target_colour, bags) - 1
    print(bags_in_bags)
    

def holds_colour(colour, bags):
    """For each bag, check if it directly holds the 
        colour we want, otherwise recursively check if any of the bags
        in it hold the colour, return the result
    """
    if colour == "shiny gold":
        return True
    else:
        return any(has_shiny_gold(c) for _, c in bags[colour])

def count_bags(colour, bags):
    """
    Return 1 (for the current bag) + the number of each bag in it * the number of bags in that bag
    and so on and so forth.
    When calling this, you have to subtract one since we are NOT counting the starting bag
    """
    #pdb.set_trace()
    return 1 + sum(int(n)*count_bags(c, bags) for n,c in bags[colour])

if __name__ == "__main__":
    main()