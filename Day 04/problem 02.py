path = "input.txt"

file = open(path)
input = file.readlines()
file.close()

for i in range(len(input)):
    input[i] = input[i][:-1]
