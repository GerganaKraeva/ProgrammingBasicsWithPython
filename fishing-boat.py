budget = int(input())
season = input()
people = int(input())
boat_price = 0

if season == "Spring":
    boat_price = 3000
elif season == "Summer" or season == "Autumn":
    boat_price = 4200
elif season == "Winter":
    boat_price = 2600

if people <= 6:
    boat_price = boat_price * 0.9
elif people <= 11:
    boat_price = boat_price * 0.85
else:
    boat_price = boat_price * 0.75

if people % 2 == 0 and not season == "Autumn":
    boat_price = 0.95 * boat_price

if boat_price <= budget:
    print(f'Yes! You have {budget-boat_price:.2f} leva left.')
else:
    print(f'Not enough money! You need {boat_price-budget:.2f} leva.')
