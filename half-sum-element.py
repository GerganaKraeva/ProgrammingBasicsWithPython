import sys

n = int(input())
sum1 = 0
max_number = -sys.maxsize

for i in range(0, n):
    number = int(input())
    sum1 += number
    if number > max_number:
        max_number = number
if max_number == (sum1 - max_number):
    print("Yes")
    print(f'Sum = {max_number}')
else:
    diff = abs(max_number-(sum1-max_number))
    print("No")
    print(f'Diff = {diff}')
