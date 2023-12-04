# day 02

import os
import math


REL_PATH = os.path.relpath('../input/02', start=os.path.pardir)
PATH = os.path.abspath(REL_PATH)


def main():
    part_one = part_1()
    print(f"Part 1: Summe {part_one}")
    part_two = part_2()
    print(f"Part 2: Summe {part_two}")

    
def part_1():
    total = []
    with open(PATH, 'r') as FILE:
        for LINE in FILE: 
            game_id, subset = LINE.split(':', 1)
            game_id = game_id.split(' ')[1]
            subset = subset.strip().split('; ')
            
            possible = True
            map = { "red": 12, "green": 13, "blue": 14 }
            for i in subset:
                bag = i.split(', ')
                for item in bag: 
                    num, item_str  = item.split(' ')
                    if item_str == 'red':
                        map["red"] = map.get('red') - int(num)
                    if item_str == 'green':
                        map["green"] = map.get("green") - int(num)
                    if item_str == 'blue':
                        map["blue"] = map.get("blue") - int(num)
                    
                    # check if still in parameters
                    if any(value < 0 for value in map.values()):
                        possible = False
                        break
                if not possible:
                    break
            if possible:
                total.append(int(game_id))
    return sum(total)


def part_2():
    total = []
    with open(PATH, 'r') as FILE:
        for LINE in FILE: 
            game_id, subset = LINE.split(':', 1)
            game_id = game_id.split(' ')[1]
            subset = subset.strip().split('; ')
            
            map = { "red": 0, "green": 0, "blue": 0 }
            for i in subset:
                bag = i.split(', ')
                for item in bag: 
                    num, item_str  = item.split(' ')
                    num = int(num)
                    if item_str == 'red':
                        if num > map.get('red'):
                            map["red"] = num
                    if item_str == 'green':
                        if num > map.get("green"):
                            map["green"] = int(num)
                    if item_str == 'blue':
                        if num > map.get("blue"):
                            map["blue"] = int(num)
            power = math.prod(map.values())
            total.append(int(power))
    return sum(total)


if __name__ == '__main__':
    main()