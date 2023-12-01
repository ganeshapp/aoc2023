lines = []
with open('input1.txt') as f:
    lines = f.readlines()

sum = 0
import re
for line in lines:
    # get all the numbers in the alphanumeric string
    numbers = re.findall(r'\d+', line)
    #print(line)
    #print(int(str(numbers[0][0])), int(numbers[-1])%10)
    sum = sum + int(str(numbers[0][0]))*10 + int(numbers[-1])%10
print(sum)