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

        self.horizontalX = self.x1 == self.x2
        self.horizontalY = self.y1 == self.y2
        self.diagonal = abs(self.x1 - self.x2) == abs(self.y1 - self.y2)

        self.x_reverse = -1 if x1 > x2 else 1
        self.y_reverse = -1 if y1 > y2 else 1

    def draw(self, diagram):
        if self.horizontalX:
            for i in range(self.y1, self.y2 + self.y_reverse, self.y_reverse):
                diagram[i][self.x1] += 1

        elif self.horizontalY:
            for i in range(self.x1, self.x2 + self.x_reverse, self.x_reverse):
                diagram[self.y1][i] += 1

        elif self.diagonal:
            x_coors = [i for i in range(self.x1, self.x2 + self.x_reverse, self.x_reverse)]
            y_coors = [i for i in range(self.y1, self.y2 + self.y_reverse, self.y_reverse)]

            for index in range(len(x_coors)):
                diagram[y_coors[index]][x_coors[index]] += 1



lines = [line.replace("->", ",").strip().split(",") for line in input]
lines = [Line(int(x1), int(y1), int(x2), int(y2)) for x1, y1, x2, y2 in lines]


diagram = [[0 for _ in range(1000)] for _ in range(1000)]


# Line(0, 8, 8, 0).draw(diagram)
# Line(0, 0, 8, 8).draw(diagram)

for line in lines:
    line.draw(diagram)

def count_overlaps(diagram):
    sum = 0
    for line in diagram:
        for item in line:
            sum += item >= 2
    return sum


# for item in diagram:
#     print(item)

print(count_overlaps(diagram))
