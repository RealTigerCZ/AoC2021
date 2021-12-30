path = "input.txt"

file = open(path)
input = [line[:-1] for line in file.readlines()]
file.close()

class Octopus:
    def __init__(self, x, y, energy):
        self.x = x
        self.y = y
        self.energy = energy
        self.neighbours = []
        self.flashed = False

    def find_neighbours(self, octo):
        dirs = [(1,0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
        for dir in dirs:
            x = dir[0] + self.x
            y = dir[1] + self.y
            if x < X_MAX and x >= 0 and y < Y_MAX and y >= 0:
                self.neighbours.append(octo[y][x])

    def flash(self):
        self.energy += 1
        if self.energy > 9:
            self.energy = 0
            self.flashed = True
            for n in self.neighbours:
                if not n.flashed:
                    n.flash()


Octopuses = [[Octopus(x, y, int(n)) for x, n in enumerate(line)] for y, line in enumerate(input)]
X_MAX = len(Octopuses[0])
Y_MAX = len(Octopuses)

for line in Octopuses:
    for o in line:
        o.find_neighbours(Octopuses)


FLASHED = 0
for i in range(100):
    for line in Octopuses:
        for o in line:
            if not o.flashed:
                o.flash()
    for line in Octopuses:
        for o in line:
            if o.flashed:
                o.flashed = False
                FLASHED += 1

print(FLASHED)
