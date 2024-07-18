
# index:               0  1   2  3  len=4
numbers: list[int] = [10, 2, -1, 4]
#                    200 201 202 203
#     numbers==#200
#       numbers[1]
print(numbers)
print(f"numbers[0] = {numbers[0]}") # 10
print(f"numbers[3] = {numbers[3]}") # 10
#print(numbers[4]) # Error
print(f"list length = {len(numbers)}")

# for. use it when we need the index
for i in range(0, len(numbers)):
    number = numbers[i]
    print(f"numbers[{i}] = {numbers[i]}", end=" | ")  # 10
print()

# [10, 2, -1, 4]
# for-each
for number in numbers:
    print(number, end=" ")
print()

for c in "Hello":
    print(c, end= " ")
print()

# index
#   0  1   2  3
# [10, 2, -1, 4]
print(f"numbers[0: 3] = {numbers[0: 3]}") # [10, 2, -1]
print(f"numbers[:3] = {numbers[:3]}")   # [10, 2, -1]
print(f"numbers[:] = {numbers[:]}")   # [10, 2, -1, 4]
print(f"numbers[2: 4] = {numbers[2: 4]}")   # [ -1, 4]
print(f"numbers[2:] = {numbers[2:]}")   # [ -1, 4]
print(f"numbers[0:4:2] = {numbers[0:4:2]}")   # [10, -1]
print(f"numbers[::-1] = {numbers[::-1]}")   # [4, -1, 2, 10]
print(f"numbers[len(numbers) - 1] = {numbers[len(numbers) - 1]}")   # [4]
print(f"numbers[-1] = {numbers[-1]}")   # [4]
print(f"numbers[-2] = {numbers[-2]}")   # [-1]

print()
print('original', numbers)
numbers[0] = 200
print('after numbers[0] = 200', numbers)
numbers.insert(2, 444)
print('after numbers.insert(2, 444)', numbers)
print()

# input grades from user until entered -999
# ignore < 0 or > 100
# store all of the grades
grades: list[int] = []
while True:
    grade: int = int(input("enter grade [-999 to exit]:"))
    if grade == -999:
        break
    if grade < 0 or grade > 100:
        continue
    grades.append(grade) # insert at the end

print(grades)
print(f"max(grades) = {max(grades)}")
print(f"min(grades) = {min(grades)}")
print(f"sum(grades) = {sum(grades)}")
print(f"len(grades) = {len(grades)}")
print(f"avg(grades) = {sum(grades) / len(grades) : .2f}")

import statistics
print(f"statistics.mean(grades) = {statistics.mean(grades) : .2f}")