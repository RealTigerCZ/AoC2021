path = "input.txt"

file = open(path)
input = file.readlines()
file.close()

all_fish = [[int(x) for x in line.split(",")] for line in input][0]

for i in range(80):
    new = 0
    for idx in range(len(all_fish)):
        if all_fish[idx] == 0:
            all_fish[idx] = 6
            new += 1
        else:
            all_fish[idx] -= 1
    all_fish += [8 for _ in range(new)]

print(len(all_fish))
