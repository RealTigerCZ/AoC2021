path = "input.txt"

file = open(path)
input = file.readlines()
file.close()

lenght = len(input[0][:-1])

zeros = [0 for i in range(lenght)]
ones = [0 for i in range(lenght)]

for line in input:
    for idx, item in enumerate(line):
        if item == "0":
            zeros[idx] += 1
        elif item == "1":
            ones[idx] += 1


gamma_rate = []
epsilon = []

for idx in range(lenght):
    if zeros[idx] > ones[idx]:
        gamma_rate.append("0")
        epsilon.append("1")
    else:
        gamma_rate.append("1")
        epsilon.append("0")

gamma_rate = "".join(gamma_rate)
epsilon = "".join(epsilon)

print(f"Gamma rate: ({gamma_rate} : {int(gamma_rate, 2)}), epsilon ({epsilon} : {int(epsilon, 2)})")
print(f"Result: {int(gamma_rate, 2)*int(epsilon, 2)}")
