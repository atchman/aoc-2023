# day 03

import os


REL_PATH = os.path.relpath('../input/03.sample', start=os.path.pardir)
PATH = os.path.abspath(REL_PATH)


def main():
    part_one = part_1()
    print(f"Part 1: Summe {part_one}")
    #part_two = part_2()
    #print(f"Part 2: Summe {part_two}")

 
def part_1():
    total = []
    with open(PATH, 'r') as FILE:
        for i,LINE in enumerate(FILE, 0):
            for j,char in enumerate(LINE, 0):
                number = []
                if char.isdigit():
                    number.append(int(char))
                if char.isascii():
                
                    



    return sum(total) 

        
if __name__ == '__main__':
    main()
