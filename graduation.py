name = input()
grades = 0
years = 0
poor_grade = 0
sum_avg_grade = 0

while years < 12:
    grade = float(input())
    if poor_grade > 1:
        break
    if grade < 4.00:
        poor_grade += 1
        continue
    years += 1
    sum_avg_grade += grade
if poor_grade < 1:
    avg_grade = sum_avg_grade / years
    print(f'{name} graduated. Average grade: {avg_grade:.2f}')
else:
    print(f'{name} has been excluded at {years} grade')
