path = "input.txt"

file = open(path)
input = file.readlines()
file.close()

class Basin:
    def __init__(self, point):
        self.size = 1
        self.point = point
        point.in_basin = True

    def add_point(self, point):
        point.in_basin = True
        self.size += 1

    def grow(self, heightmap):
        self.point.grow(self)

class Point:
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value
        self.in_basin = False
        self.neighbours = []
    def search_neighbours(self, heightmap):
        if self.x > 0:
            self.neighbours.append(heightmap[self.y][self.x-1])
        if self.x < X_MAX - 1:
            self.neighbours.append(heightmap[self.y][self.x+1])
        if self.y > 0:
            self.neighbours.append(heightmap[self.y-1][self.x])
        if self.y < Y_MAX - 1:
            self.neighbours.append(heightmap[self.y+1][self.x])

    def grow(self, basin):
        for neighbour in self.neighbours:
            if neighbour.value != 9 and not neighbour.in_basin:
                basin.add_point(neighbour)
                neighbour.grow(basin)

heightmap = [[Point(x, y, int(n)) for x, n in enumerate(line[:-1])] for y, line in enumerate(input)]

basins = []
X_MAX = len(heightmap[0])
Y_MAX = len(heightmap)

for line in heightmap:
    for point in line:
        point.search_neighbours(heightmap)


for y in range(Y_MAX):
    for x in range(X_MAX):
        point = heightmap[y][x]
        if not point.in_basin and point.value != 9:
            basin = Basin(point)
            basin.grow(heightmap)
            basins.append(basin)

basins = list(sorted([basin.size for basin in basins]))
print(basins[-1]*basins[-2]*basins[-3])
