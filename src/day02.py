# day 02

import os


REL_PATH = os.path.relpath('../input/02', start=os.path.pardir)
PATH = os.path.abspath(REL_PATH)


def main():
    part_one = part_1()
    print(f"Part 1: Summe {part_one}")

    #part_two = part_2()
    #print(f"Part 2: Summe {part_two}")

 
def part_1():
    total = []
    p = [12, 13, 14]
    
    with open(PATH, 'r') as FILE:
        for LINE in FILE: 
            game_id, subset_list = parse_game(LINE)
            print(f"game: {game_id}")
            print(f"subset: {subset_list}")
            r, g, b = 0, 0, 0
            for i in range(len(subset_list)):
                r = r + subset_list[i][0]
                g = g + subset_list[i][1]
                b = b + subset_list[i][2]
            if r < p[0]+1:
                if g < p[1]+1:
                    if b < p[2]+1:
                        print(f"Tue")
                        total.append(int(game_id))
    print(f"total {total}")
    return sum(total)


def parse_game(LINE):
    subset_list = [0, 0, 0]
    game_id, subset = LINE.split(':', 1)
    game_id = game_id.split(' ')[1]
    subset = subset.strip().split('; ')
    
    for i in range(len(subset)):
        bag = subset[i].split(', ')
        # 0 = red, 1, green, 2, blue
        subset_list.append([0, 0, 0])
        for x in range(len(bag)):
            if bag[x].find("red") != -1:
                subset_list[i][0] = int(bag[x].split(' ', 1)[0].strip())
            if bag[x].find("green") != -1:
                subset_list[i][1] = int(bag[x].split(' ', 1)[0].strip())
            if bag[x].find("blue") != -1:
                subset_list[i][2] = int(bag[x].split(' ', 1)[0].strip())
    return game_id, subset_list

        
if __name__ == '__main__':
    main()