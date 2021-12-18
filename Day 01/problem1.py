path = "input.txt"

file = open(path)
input = file.readlines()
file.close()

for index, item in enumerate(input):
    input[index] = int(item)

last = input[0]
increase = 0

for item in input[1:]:
    if last < item:
        increase += 1
    last = item

print(increase)
