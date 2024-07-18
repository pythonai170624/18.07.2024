
numbers: list[int] = [10, 2, -1, 4]
more_numbers: list[int] = [99, -999]

numbers.extend(more_numbers)  # add list 2 to list1
print(numbers)
print(more_numbers)
print('after concat', numbers)

# remove first occurrence of an item -999
x = numbers.remove(-999)
print('after remove 999', numbers)

pop: int = numbers.pop() # last index
print('pop last', pop)
print('after pop', numbers)

pop2: int = numbers.pop(1)  # pop at index 1
print('pop index [1] ==', pop2)
print('after pop [1]', numbers)

del numbers[1]  # remove at index 1
print('after remove item index 1', numbers)

# how to remove all occurrence of 99?
while 99 in numbers:
    numbers.remove(99)

# clear
numbers.clear()
print('after clear', numbers)

numbers.extend([10, 2, -1, 4])
print('after extend', numbers)
print('numbers.index(-1)', numbers.index(-1))

numbers.extend([4, 4, 4, 4, -9, 12, 4])
print('after extend', numbers)
print('numbers.count(4)', numbers.count(4))

# sort changes the list
clone = numbers.copy()
clone.sort()
print('after sort [clone]', clone)
clone.sort(reverse=True)
print('after sort reverse [clone]', clone)

# sorted does NOT change the list
print('after sorted', sorted(numbers))
print('after sorted reverse', sorted(numbers, reverse=True))
print('after list + reversed', list(reversed(numbers)))  # iterator

print(numbers)

bool1: list[bool] = [True, True, True]
bool2: list[bool] = [True, True, False]
bool3: list[int] = [20, 0, 300, 100, 100]
print('all bool1', bool1, all(bool1))  # True
print('all bool2', bool2, all(bool2))  # False
print('all bool3', bool3, all(bool3))  # False

bool1: list[bool] = [True, True, True]
bool2: list[bool] = [True, True, False]
bool3: list[int] = [20, 0, 300, 100, 100]
bool4: list[bool] = [False, False]
bool5: list[int] = [0, 0, 0, 0, 0]
print('any bool1', bool1, any(bool1))  # True
print('any bool2', bool2, any(bool2))  # True
print('any bool3', bool3, any(bool3))  # True
print('any bool4', bool4, any(bool4))  # False
print('any bool5', bool5, any(bool5))  # False

