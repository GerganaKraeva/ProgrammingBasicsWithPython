floors = int(input())
rooms = int(input())

for i in range(floors, 0, -1):
    for j in range(0, rooms, 1):
        if i == floors:
            print(f"L{i}{j}", end=" ")
        else:
            if i % 2 == 0:
                print(f"O{i}{j}", end=" ")
            else:
                print(f"A{i}{j}", end=" ")
    print()