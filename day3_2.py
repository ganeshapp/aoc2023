lines = []
with open('day3_input.txt') as f:
    lines = f.readlines()

for line in lines:
    lines[lines.index(line)] = line.strip()

i = 0
num_list = []
part_list = []
sum = 0
#gear_positions = []

for line in lines:
    # get numbers in the string
    number_positions = []
    number_string = ''
    j = 0
    for char in line:
        # if char == '*':
        #    gear_positions.append([i,j])
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

#print(gear_positions) 
gear_numbers = []
for num in num_list:
    #print(num)
    is_part = False
    part_num = num[0]
    adjacent_positions = []
    
    for postitions in num[1]:
        #print(postitions)
        m = postitions[0]
        n = postitions[1]
        check_positions = [[m-1,n],[m+1,n],[m,n-1],[m,n+1],[m-1,n-1],[m-1,n+1],[m+1,n-1],[m+1,n+1]]
        #print(part_num, check_positions)
        for check_position in check_positions:
            if check_position[0]>=0 and check_position[0]<len(lines) and check_position[1]>=0 and check_position[1]<len(lines[0]):
                if lines[check_position[0]][check_position[1]]!= '.' and not lines[check_position[0]][check_position[1]].isdigit():
                    is_part = True
                    if lines[check_position[0]][check_position[1]] == '*':
                        if [check_position,part_num] not in gear_numbers:
                            gear_numbers.append([check_position,part_num])
    
    if is_part:
        part_list.append(part_num)
        sum += part_num


    #print(num, is_part, sum)
#print(part_list)
# print(gear_numbers)
gear_positions = []
#for gear_number in gear_numbers:
#    if gear_number[0] not in gear_positions:
#        gear_positions.append(gear_number[0])

gear_product = 0
n = len(gear_numbers)
m = 0
#print("gear_position_list", gear_positions)
while m < n:
    
    #print(gear_numbers[m][0])
    if gear_numbers[m][0] in gear_positions:
        m += 1
        continue
        #print("inside break")
    if gear_numbers[m][0] not in gear_positions:
        #print("first occurance of Gear", gear_numbers[m][0])
        gear_positions.append(gear_numbers[m][0])
        #print("gear_position_list", gear_positions)
        i = m+1
        while i < n:
            #print("base gear", gear_numbers[m][0], "checking gear", gear_numbers[i][0])
            if gear_numbers[i][0] == gear_numbers[m][0]:
                #print("product of", gear_numbers[m][1], "and", gear_numbers[i][1], "is", gear_numbers[m][1] * gear_numbers[i][1])
                gear_product = gear_product + gear_numbers[m][1] * gear_numbers[i][1]
            i += 1
    m += 1

print(gear_product)
print(sum)