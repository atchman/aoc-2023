# day 02

import os


REL_PATH = os.path.relpath('../input/01', start=os.path.pardir)
PATH = os.path.abspath(REL_PATH)


def main():
    part_one = part_1()
    print(f"Part 1: Summe {part_one}")

    #part_two = part_2()
    #print(f"Part 2: Summe {part_two}")

 
def part_1():
    with open(PATH, 'r') as FILE:
        for LINE in FILE: 
            return 0 


def part_2():
    with open(PATH, 'r') as FILE:
        for LINE in FILE: 
            return 0 
        
        
if __name__ == '__main__':
    main()