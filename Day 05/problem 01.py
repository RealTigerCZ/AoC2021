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

    def isHorizontalOrVertical(self):
        return self.x1 == self.x2 or self.y1 == self.y2

    def draw(self, diagram):
        if self.x1 == self.x2:
            y1 = min(self.y1, self.y2)
            y2 = max(self.y1, self.y2)
            for i in range(y1, y2 + 1):
                diagram[i][self.x1] += 1

        elif self.y1 == self.y2:
            x1 = min(self.x1, self.x2)
            x2 = max(self.x1, self.x2)
            for i in range(x1, x2 + 1):
                diagram[self.y1][i] += 1

        else:
            assert False, "Unreachable -> not Horizontal Or Vertical line"

lines = [line.replace("->", ",").strip().split(",") for line in input]
lines = [Line(int(x1), int(y1), int(x2), int(y2)) for x1, y1, x2, y2 in lines]

lines = [line for line in lines if line.isHorizontalOrVertical()]


diagram = [[0 for _ in range(1000)] for _ in range(1000)]


for line in lines:
    line.draw(diagram)

def count_overlaps(diagram):
    sum = 0
    for line in diagram:
        for item in line:
            sum += item >= 2
    return sum


print(count_overlaps(diagram))
