type_film = input()
rows = int(input())
columns = int(input())

if type_film == "Premiere":
    print(f'{rows * columns * 12:.2f} leva')
elif type_film == "Normal":
    print(f'{rows * columns * 7.5:.2f} leva')
elif type_film == "Discount":
    print(f'{rows * columns * 5:.2f} leva')
