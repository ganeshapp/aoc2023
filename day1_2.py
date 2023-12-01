import re

lines = []
with open('input1.txt') as f:
    lines = f.readlines()

sum = 0

'''
## This is an attempt where it is assumed that eighthree is 8hree and not 83
def convert_string_to_numbers(input_string):
    patterns = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    resolved = False
    line = input_string
    while not resolved:
        #print(line)
        first_position = []
        for pattern in patterns:
            match = re.search(pattern, line)
            if match:
                first_position.append(match.start())
            else:
                first_position.append(-1)
        #print(first_position)
        if max(first_position) == -1:
            resolved = True
            return line
        else:
            min_index = first_position.index(min(filter(lambda x: x >= 0, first_position)))+1
            line = line.replace(patterns[min_index-1], str(min_index), 1)
    return line

# This is an attempt where it assumes the same as above but only for first and last values. So eighthreetwone is 8hreetw1
def convert_string_to_numbers(input_string):
    patterns = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    line = input_string
    first_position = []
    for pattern in patterns:
        match = re.search(pattern, line)
        if match:
            first_position.append(match.start())
        else:
            first_position.append(-1)
    
    if max(first_position) == -1:
        return line
    else:
        min_index = first_position.index(min(filter(lambda x: x >= 0, first_position)))+1
        line = line.replace(patterns[min_index-1], str(min_index), 1)
        first_position = []

        for pattern in patterns:
            match = re.search(pattern, line)
            if match:
                first_position.append(match.start())
            else:
                first_position.append(-1)
        
        if max(first_position) == -1:
            return line
        else:
            max_index = first_position.index(max(filter(lambda x: x >= 0, first_position)))+1
            line = line.replace(patterns[max_index-1], str(max_index), -1)
        
    return line
'''

# This is the final attempt where eighthreetwone is 8321

for line in lines:

    line = line.strip()
    patterns = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine','1','2','3','4','5','6','7','8','9']
    
    first_position = []
    last_position = []
    
    for pattern in patterns:
        first_match = re.search(pattern, line)
        if first_match:
            first_position.append(first_match.start())
        else:
            first_position.append(-1)
        
        last_match = re.finditer(pattern, line)
        last_position.append(max((match.start() for match in last_match), default=-1))

    min_index = first_position.index(min(filter(lambda x: x >= 0, first_position)))
    max_index = last_position.index(max(filter(lambda x: x >= 0, last_position)))
    #print(line)
    #print(min_index, max_index)
    first_num = 0
    second_num = 0
    if min_index > 8:
        first_num = (min_index - 8)*10
    else:
        first_num = (min_index + 1)*10
    
    if max_index > 8:
        second_num = max_index - 8
    else:
        second_num = max_index + 1
    #print(first_num, second_num)
    sum = sum + first_num + second_num
    
print(sum)