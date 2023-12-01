# day 01

import os

REL_PATH = os.path.relpath('../input/01-2.sample', start=os.path.pardir)
PATH = os.path.abspath(REL_PATH)

def main():
    with open(PATH, 'r') as FILE:
        total = []
        for LINE in FILE:
            replace = string_to_num(LINE)
            numbers = ''
            for l in replace: 
                if l.isdigit():
                    numbers = ''.join((numbers, l))
            num = numbers[0] + numbers[len(numbers)-1]
            total.append(int(num))
    print(sum(total))
    
    
def string_to_num(LINE):
    num_string = {"one": 1, "two": 2, "three" : 3,
                  "four": 4, "five": 5, "six": 6,
                  "seven": 7, "eight": 8, "nine": 9
                  }
    line_cp = LINE
    spot = {}
    for k in num_string.keys():
        if not LINE.find(k) == -1:
            i for i
            spot.update({LINE.find(k): k})
    sorted_spot = dict(sorted(spot.items()))
    
    for v in sorted_spot.values():
        line_cp = line_cp.replace(v, str(num_string.get(v)))
    return line_cp
    

# https://stackoverflow.com/questions/4664850/how-to-find-all-occurrences-of-a-substring
def findall(p, a):
    i = a.find(p)
    while i != -1:
        yield i
        i = a.find(p, i+1) 
   
    
if __name__ == '__main__':
    main()