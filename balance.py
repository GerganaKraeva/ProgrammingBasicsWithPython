user_input = input()
sum1 = 0
money = 0

while user_input != "NoMoreMoney":
    if user_input == "NoMoreMoney":
        break
    money = float(user_input)
    if money < 0:
        print('Invalid operation!')
        break
    sum1 += money
    print(f'Increase: {money:.2f}')
    user_input = input()
print(f'Total: {sum1:.2f}')



