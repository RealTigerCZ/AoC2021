path = "input.txt"

file = open(path)
input = file.readlines()
file.close()


#Logic solution
"""
? = intersection of sets
/ = without

A = !4 ? 7 = 7 / 1
B = !3 ? 4
---------
C = 1 ? 2 = !6
D = !0
E = !9
F = !2 ? 1
G =
--------- not needed

C, F = 7 / A
B, D = 4 / 1

problematic:
0, 6, 9
2, 3, 5

2 ? 1 != 1
3 ? 1 = 1
6 ? 1 != 1

9 ? 1 = 1
0 ? 1 = 1
6 ? 1 != 1

-------------------
Actual solving method / aglorithm
A -> 7 / 1
3 -> len = 5 and 3 ? 1 = 1
B -> !3 ? 4
5 ->  contain b and len = 5
2 -> len = 5 and is ont 5 or 3
D -> B, D = 4 / 1 (we know B)
0 -> !D
6 -> 6 ? 1 != 1 and len = 6
9 -> len = 6 and is not 6 or 0


MAPPING IS DONE MANUALLY TO NUMBERS WITH THAT ALGORITHM
ITS NOT NEEDED TO MAP ALL SEGMENTS (for this problem)s
"""

def sort(a): #sorts string
    return "".join(sorted(a))

def without(a, b):
    for item in b:
        if item in a:
            a = a.replace(item, "")
    return a

def intersect(a, b):
    toReturn = ""
    for item in a:
        if item in b:
            toReturn += item
    return toReturn

def not_code(a):
    return(without("abcdefg", a))

nums = []

for line in input:
    line = line.split("|")
    zero_six_nine = []
    two_three_five = []
    numbers = [0 for _ in range(10)]
    for element in line[0].strip().split(" "):
        element = sort(element)
        if len(element) == 2:
            numbers[1] = element
        elif len(element) == 3:
            numbers[7] = element
        elif len(element) == 4:
            numbers[4] = element
        elif len(element) == 5:
            two_three_five.append(element)
        elif len(element) == 6:
            zero_six_nine.append(element)
        elif len(element) == 7:
            numbers[8] = element
        else:
            assert False, "Unreachable!"

    A = without(numbers[7], numbers[1])
    for n in two_three_five: #finding 3
        if intersect(n, numbers[1]) == numbers[1]:
            two_three_five.remove(n)
            numbers[3] = n
            break
    B = intersect(not_code(numbers[3]), numbers[4])
    if B in two_three_five[0]: #finding 5 and 2
        numbers[5] = two_three_five[0]
        numbers[2] = two_three_five[1]
    else:
        numbers[5] = two_three_five[1]
        numbers[2] = two_three_five[0]
    D = without(without(numbers[4], numbers[1]), B)
    numbers[0] = not_code(D)
    zero_six_nine.remove(numbers[0])
    if intersect(zero_six_nine[0], numbers[1]) == numbers[1]:
        numbers[9] = zero_six_nine[0]
        numbers[6] = zero_six_nine[1]
    else:
        numbers[9] = zero_six_nine[1]
        numbers[6] = zero_six_nine[0]

    num_dict = {}
    for idx, num in enumerate(numbers):
        num_dict[num] = str(idx)

    ret_num = ""

    for element in line[1].strip().split(" "):
        element = sort(element)
        ret_num += num_dict[element]

    nums.append(int(ret_num))

print(sum(nums))
