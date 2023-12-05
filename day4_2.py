lines = []
with open('day4_input.txt') as f:
    lines = f.readlines()

sum = 0

max_card_numbers = len(lines)
card_count = {}
for i in range(max_card_numbers):
    card_count[i] = 0

#print(card_count)

for line in lines:
    line = line.strip()
    card_id = int(line.split(':')[0].strip().split(' ')[-1])
    #print("card_id", card_id-1)
    previous_card_count = card_count[card_id-1]
    #print("previous_card_count", previous_card_count)
    card_count[card_id-1] += 1
    #print(card_count)
    winning_numbers = line.split('|')[0].split(':')[1].strip().split(' ')
    your_numbers = line.split('|')[1].strip().split(' ')
    #print(card_id, winning_numbers, your_numbers)
    
    i = 0
    for number in your_numbers:
        if number!= '':
            if number in winning_numbers:
                i += 1
    #print("matches found", i)
                
    if i > 0:
        j = 1
        while j<=i:
            if card_id+j < max_card_numbers:
                card_count[card_id+j-1] += 1 + previous_card_count
            j = j+1

#print(card_count)

for card in card_count:
    sum += card_count[card]

print(sum)