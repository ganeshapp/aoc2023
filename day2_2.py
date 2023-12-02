lines = []
with open('day2_input.txt') as f:
    lines = f.readlines()

power_sum = 0
for line in lines:
    draws = line.strip().split(':')[1].split(';')
    # print('draws', draws)
    red_count = 0
    green_count = 0
    blue_count = 0
    for draw in draws:
        cubes = draw.split(',')
        #print(cubes)
        for cube in cubes:
            cube_color = cube.strip().split(' ')[1]
            cube_count = int(cube.strip().split(' ')[0])
            #print(cube_color, cube_count)
            
            if cube_color =='red':
                red_count = max(red_count, cube_count)
            if cube_color == 'green':
                green_count = max(green_count, cube_count)
            if cube_color =='blue':
                blue_count = max(blue_count, cube_count)
            #print(red_count, green_count, blue_count)

    power_sum += max(red_count,1) * max(green_count,1) * max(blue_count,1)
    #print(line.strip().split(':')[0], power_sum)
print(power_sum)