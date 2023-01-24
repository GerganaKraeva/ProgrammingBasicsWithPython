destination = input()
budget = 0
saved_money = 0

while destination != "End":
    if destination == "End":
        break
    budget = float(input())
    while saved_money < budget:
        saved_money += float(input())
    if saved_money >= budget:
        print(f"Going to {destination}!")
    saved_money = 0
    destination = input()
