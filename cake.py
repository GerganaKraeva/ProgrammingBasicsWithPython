width_cake = int(input())
length_cake = int(input())
size = width_cake * length_cake
user_input = input()
pieces = 0

while user_input != "STOP":
    pieces = int(user_input)
    size -= pieces
    if size < 0:
        break
    user_input = input()
if size > 0:
    print(f"{size} pieces are left.")
else:
    print(f"No more cake left! You need {abs(size)} pieces more.")

