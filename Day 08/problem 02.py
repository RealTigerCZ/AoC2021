path = "input.txt"

file = open(path)
input = file.readlines()
file.close()

coords = sorted([[int(n) for n in line.split(",")] for line in input][0])

#super slow
#print(min([sum([sum([m + 1 for m in range(abs(n - i))]) for n in coords])] for i in range(coords[0], coords[-1]+1))[0])

add = [0]
for idx in range(2000):
    add.append(add[idx] + idx + 1)

print(min([sum([add[abs(n - i)] for n in coords])] for i in range(coords[0], coords[-1]+1))[0])
