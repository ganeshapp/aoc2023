lines = []
with open('day4_input.txt') as f:
    lines = f.readlines()

sum = 0
for line in lines:
    line = line.strip()
    card_id = line.split(':')[0].strip().split(' ')[1]
    winning_numbers = line.split('|')[0].split(':')[1].strip().split(' ')
    your_numbers = line.split('|')[1].strip().split(' ')
    #print(card_id, winning_numbers, your_numbers)

    i = 0
    for number in your_numbers:
        if number!= '':
            if number in winning_numbers:
                i += 1
    #print(i)

    if i > 0:
        sum += 2**(i-1)

print(sum)