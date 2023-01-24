month = input()
number_nights = int(input())
studio_price = 0
apartment_price = 0

if month == "May" or month == "October":
    studio_price = 50
    apartment_price = 65
    if (number_nights > 7) and number_nights < 14:
        studio_price = studio_price * 0.95
    if number_nights > 14:
        studio_price = studio_price * 0.7
if month == "June" or month == "September":
    studio_price = 75.2
    apartment_price = 68.7
    if number_nights > 14:
        studio_price = 0.8 * studio_price
if month == "July" or month == "August":
    studio_price = 76
    apartment_price = 77

if number_nights > 14:
    apartment_price = 0.9 * apartment_price
print(f'Apartment: {apartment_price * number_nights:.2f} lv.')
print(f'Studio: {studio_price * number_nights:.2f} lv.')
