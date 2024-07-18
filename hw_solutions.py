# ___*___
# __***__
# _*****_
# ********

# 7 / 2 = 3.5
# 7
# ___*___    3 spaces 1 star 3 spaces
# __***__    2 spaces 3 star 2 spaces
# _*****_    1 spaces 5 stars 1 space
# ********   0 spaces 7 stars 0 space

# 9
# ____*____   4 spaces 1 star  4 spaces
# ___***___   3 spaces 3 stars 3 space
# __*****__   2 spaces 5 stars 2 space
# _*******_   1 spaces 7 stars 1 space
# *********   0 spaces 9 stars 0 space

number: int = 15
space: int = number // 2
for i in range(1, number + 1, 2):
    print(space * " ", end= "")

    #print("*" * i)
    for j in range(1, i + 1):
        print("*", end="")
    print()
    space -= 1