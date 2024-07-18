# Introduction
numbers: list[int] = [1, 4, 5, 9]
# print(numbers[4]) # code error

# this may crash
try:
    grade: int = int(input('Enter grade:'))
    print('grade is ok')
except:
    print('something went wrong ...')

grade: int = None
#if grade -- False
while not grade:
    try:
        grade = int(input('Enter grade:'))
        print('grade is ok')
    except:
        print('something went wrong ... try again')

# this is how to print the error
grade: int = None
ex: Exception = ValueError
while not grade:
    try:
        grade = int(input('Enter grade:'))
        print('grade is ok')
    except Exception as e:
        print(f'something went wrong --{e}-- ... try again')

print('finish')
