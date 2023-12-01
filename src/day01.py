# day 01

import os

REL_PATH = os.path.relpath('../input/01', start=os.path.pardir)
PATH = os.path.abspath(REL_PATH)

def main():
    with open(PATH, 'r') as FILE:
        total = []
        for LINE in FILE:
            numbers = ''
            for l in LINE:
                if l.isdigit():
                    numbers = ''.join((numbers, l))
            num = numbers[0] + numbers[len(numbers)-1]
            total.append(int(num))
    print(sum(total))
    
if __name__ == '__main__':
    main()