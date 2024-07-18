# Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
#                  0*0 1*1 2*2 3*3 4*4 5*5 6*6 7*7 8*8 9*9


n_list: list[int] = []
for i in range(0, 10):
    n_list.append(i ** 2);
print(n_list);

# comprehension
#             [what to append?]  [for-loop]
n_list: list[int] = [i ** 2 for i in range(0, 20)]
print(n_list);

''' tagril1: use comprehension to build a list with [0, 2, 4, 6, 8, .. 20] '''
targil1: list[int] = [i for i in range(0, 21, 2)]
print(targil1)

''' tagril2: use comprehension to build a list with 10 random numbers between 1-100 '''
import random

targil2: list[int] = [random.randint(1, 100) for _ in range(10)]
print(targil2)

''' tagril3: use comprehension to build a list with 10 random numbers between 1-100 
             use ONLY EVEN numbers, do not include odd numbers
             the list may not be in 10 length'''
# [79, 49, 89, 66, 54, 35, 68, 56, 91, 89]
# [66, 54, 68, 56]
rand_even: list[int] = []
for i in range(10):
    rnd: int = random.randint(1, 100)
    if rnd % 2 == 0:
        rand_even.append(rnd)
just_random: list[int] = [random.randint(1, 100) for _ in range(10)]
random_even: list[int] = [n for n in just_random if n % 2 == 0]
print(random_even)

# one line ! crazy!
# crazy: list[int] = [num for num in [random.randint(1, 100) for _ in range(10)] if num % 2 == 0]