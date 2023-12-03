lines = []
with open('day3_input.txt') as f:
    lines = f.readlines()

for line in lines:
    lines[lines.index(line)] = line.strip()

i = 0
num_list = []
part_list = []
sum = 0
for line in lines:
    # get numbers in the string
    number_positions = []
    number_string = ''
    j = 0
    for char in line:
        if char.isdigit():
            number_string += char
            number_positions.append([i,j])
        if not char.isdigit() or j == len(line)-1:
            if number_string != '':
                #print(number_string)
                #print(number_positions)
                num_list.append([int(number_string), number_positions])
                number_string = ''
                number_positions = []
        j += 1
    i += 1   

for num in num_list:
    #print(num)
    is_part = False
    part_num = num[0]

    for postitions in num[1]:
        #print(postitions)

        m = postitions[0]
        n = postitions[1]
        check_positions = [[m-1,n],[m+1,n],[m,n-1],[m,n+1],[m-1,n-1],[m-1,n+1],[m+1,n-1],[m+1,n+1]]
        #print(num, check_positions)
        
        for check_position in check_positions:
            if check_position[0]>=0 and check_position[0]<len(lines) and check_position[1]>=0 and check_position[1]<len(lines[0]):
                if lines[check_position[0]][check_position[1]]!= '.' and not lines[check_position[0]][check_position[1]].isdigit():
                    is_part = True

    if is_part:
        part_list.append(part_num)
        sum += part_num

    #print(num, is_part, sum)
#print(part_list)
print(sum)