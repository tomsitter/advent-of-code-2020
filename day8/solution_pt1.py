import pdb
import re

def main():
    """ 
    1. Read the input.txt file
    2. Initialize the accumulator, cur_pos, and path vars
    3. Read through the list, following instructions, and check if a instruction was re-visited
    4. Print the step and instruction that was repeated
    """    
    with open("./day8/input.txt", "r") as f:
        instructions = f.read().splitlines()

    prog = Program()
    instr = instructions[0]

    success, pos = prog.do_op(instr)
    while success:
        instr = instructions[pos]
        success, pos = prog.do_op(instr)

    print(f"{success}: {pos} ")
    print(f"Accumulator: {prog.accum}")

class Program:
    def __init__(self):
        self.accum = 0
        self.pos = 0
        self.path = [self.pos]

    def parse(self, instr):
        return re.findall(r'^(\w{3}) (.+)$', instr)[0]

    def do_op(self, instr):
        # delegate op to the appropriate operation
        op, arg = self.parse(instr)
        arg = int(arg)
        self.__getattribute__(op)(arg)
        if self.pos in self.path:
            return (False, self.pos)
        else:
            self.path.append(self.pos)
            return (True, self.pos)
    
    def acc(self, arg):
        self.accum += arg
        self.pos += 1

    def jmp(self, arg):
        self.pos += arg
    
    def nop(self, arg):
        self.pos += 1


if __name__ == "__main__":
    main()