path = "input.txt"

file = open(path)
input = file.readlines()
file.close()

heightmap = [[int(n) for n in line[:-1]] for line in input]

X_MAX = len(heightmap[0])
Y_MAX = len(heightmap)

def is_low(x, y, heightmap):
    val = heightmap[y][x]
    if y > 0:
        if val >= heightmap[y - 1][x]:
            return False
    if y < Y_MAX - 1:
        if val >= heightmap[y + 1][x]:
            return False
    if x > 0:
        if val >= heightmap[y][x - 1]:
            return False
    if x < X_MAX - 1:
        if val >= heightmap[y][x + 1]:
            return False
    return True

sum = 0
for y in range(Y_MAX):
    for x in range(X_MAX):
        if is_low(x, y, heightmap):
            #print("[%02d:%02d] -> %d" % (x, y, heightmap[y][x]))
            sum += heightmap[y][x] + 1

print(sum)
