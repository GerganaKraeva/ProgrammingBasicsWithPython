age = int(input())
price_washing_machine = float(input())
price_toy = int(input())
number_toys = 0
money = 0

for i in range(1, age + 1):
    if i % 2 != 0:
        number_toys += 1
    else:
        money += ((i / 2) * 10 - 1)
if money + number_toys * price_toy >= price_washing_machine:
    diff = money + (number_toys * price_toy) - price_washing_machine
    print(f'Yes! {diff:.2f}')
else:
    diff = price_washing_machine - money - (number_toys * price_toy)
    print(f'No! {diff:.2f}')
