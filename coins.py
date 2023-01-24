import math

money = float(input())
cents = 100 * money
counter = 0

while cents > 0:
    if cents // 200 >= 1:
        counter += cents // 200
        cents = cents % 200
    elif cents // 100 >= 1:
        counter += cents // 100
        cents = cents % 100
    elif cents // 50 >= 1:
        counter += cents // 50
        cents = cents % 50
    elif cents // 20 >= 1:
        counter += cents // 20
        cents = cents % 20
    elif cents // 10 >= 1:
        counter += cents // 10
        cents = cents % 10
    elif cents // 5 >= 1:
        counter += cents // 5
        cents = cents % 5
    elif cents // 2 >= 1:
        counter += cents // 2
        cents = cents % 2
    elif cents / 1 == 1:
        counter += 1
        cents -= 1
print(math.floor(counter))
