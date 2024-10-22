# day 01

import os
import re

REL_PATH = os.path.relpath('../input/01-2.sample', start=os.path.pardir)
PATH = os.path.abspath(REL_PATH)


def main():
    part_one = part_1()
    print(f"Part 1: Summe {part_one}")

    part_two = part_2()
    print(f"Part 2: Summe {part_two}")


def part_1():
    with open(PATH, 'r') as FILE:
        total = []
        for LINE in FILE:
            numbers = [] 
            for l in LINE: 
                if l.isdigit():
                    numbers.append(int(l))
            if len(numbers) > 1:
                num = (numbers[0] * 10) + numbers[-1]
                total.append(int(num))
    return sum(total)


def part_2():
    total = []
    num_map = { "1": 1, "2": 2, "3": 3, "4": 4, "5": 5,
                "6": 6, "7": 7, "8": 8, "9": 9,
                "one": 1, "two": 2, "three" : 3,
                "four": 4, "five": 5, "six": 6,
                "seven": 7, "eight": 8, "nine": 9 }
    spots = []
    with open(PATH, 'r') as FILE:
        for LINE in FILE:
            for k in num_map.keys():
                spots.extend(list(find_all(k, LINE)))
            spots.sort()
            print(spots)
            numbers = [0,0]
            if len(spots) > 0:
                for k in num_map.keys():
                    if LINE.startswith(k,spots[0]):
                        numbers[0] = num_map.get(k)
                    if LINE.startswith(k,spots[-1]):
                        numbers[1] = num_map.get(k)
            print(numbers)
            num = (numbers[0] * 10) + numbers[-1]
            print(num)
            total.append(int(num))
    return sum(total)


def find_all(item, a_str):
    i = a_str.find(item)
    while i != -1:
        yield i
        i = a_str.find(item, i+1)

    
if __name__ == '__main__':
    main()
