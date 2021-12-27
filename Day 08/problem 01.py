path = "input.txt"

file = open(path)
input = file.readlines()
file.close()

coords = sorted([[int(n) for n in line.split(",")] for line in input][0])

# for i in range(min(coords), max(coords) + 1):
#     print(f"{i}:", sum([abs(n-i) for n in coords]))

i = coords[len(coords)//2]
print(f"{i}:", sum([abs(n-i) for n in coords]))
