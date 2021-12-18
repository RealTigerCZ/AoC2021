path = "input.txt"

file = open(path)
input = file.readlines()
file.close()

for index, item in enumerate(input):
    input[index] = int(item)

last = input[0] + input[1] + input[2]
increase = 0


for i in range(1, len(input)-2):
    now = input[i] + input[i + 1] + input[i + 2]
    if now > last:
        increase += 1
    last = now


print(increase)
