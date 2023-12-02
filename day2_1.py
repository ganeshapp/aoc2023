lines = []
with open('day2_input.txt') as f:
    lines = f.readlines()

sum = 0
for line in lines:
    # print(line)
    game_id = int(line.strip().split(':')[0].replace('Game ', ''))
    valid_game = True
    # print(game_id)
    draws = line.split(':')[1].split(';')
    for draw in draws:
        # print(draw)
        cubes = draw.split(',')
        for cube in cubes:
            cube_color = cube.strip().split(' ')[1]
            # print(color)
            cube_count = int(cube.strip().split(' ')[0])
            #print(cube_color, cube_count)
            if cube_color =='red' and cube_count > 12:
                valid_game = False
                break
            if cube_color == 'green' and cube_count > 13:
                valid_game = False
                break
            if cube_color =='blue' and cube_count > 14:
                valid_game = False
                break
    if valid_game:
        sum += game_id
        # print('valid game', game_id)

print(sum)