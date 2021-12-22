path = "input.txt"

file = open(path)
input = file.readlines()
file.close()

class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

        self.diff = max(abs(x2 - x1), abs(y2 - y1))

        self.X_diff = -1 if x1 > x2 else 0 if x1 == x2 else 1
        self.Y_diff = -1 if y1 > y2 else 0 if y1 == y2 else 1

    def draw(self, diagram):
        for i in range(self.diff+1):
            x = self.x1 + i * self.X_diff
            y = self.y1 + i * self.Y_diff
            diagram[y][x] += 1



lines = [line.replace("->", ",").strip().split(",") for line in input]
lines = [Line(int(x1), int(y1), int(x2), int(y2)) for x1, y1, x2, y2 in lines]


diagram = [[0 for _ in range(1000)] for _ in range(1000)]


for line in lines:
    line.draw(diagram)

# for item in diagram:
#     print(item)


sum = 0
for line in diagram:
    for item in line:
        sum += item >= 2
print(sum)
