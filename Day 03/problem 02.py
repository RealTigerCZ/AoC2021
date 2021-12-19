path = "input.txt"

file = open(path)
input = file.readlines()
file.close()

for i in range(len(input)):
    input[i] = input[i][:-1]


oxigen = input[:]

bit = 0
while len(oxigen) > 1:
    zeros, ones = 0, 0
    for item in oxigen:
        if item[bit] == "0":
            zeros += 1
        elif item[bit] == "1":
            ones += 1

    char = "1" if ones >= zeros else "0"
    i = 0
    while i < len(oxigen):
        if oxigen[i][bit] != char:
            oxigen.pop(i)
        else:
            i += 1
    bit += 1

CO2 = input[:]

bit = 0
while len(CO2) > 1:
    zeros, ones = 0, 0
    for item in CO2:
        if item[bit] == "0":
            zeros += 1
        elif item[bit] == "1":
            ones += 1

    char = "0" if zeros <= ones else "1"
    i = 0
    while i < len(CO2):
        if CO2[i][bit] != char:
            CO2.pop(i)
        else:
            i += 1

    bit += 1

print(oxigen, CO2)
print("Result: ", int(oxigen[0], 2) * int(CO2[0], 2))
