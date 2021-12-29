path = "input.txt"

file = open(path)
input = [line[:-1] for line in file.readlines()]
file.close()

illegal = [1, 2, 3, 4, 3, 57, 1197, 25137]
BRACKETS = ["(", "[", "{", "<", ")", "]", "}", ">"]
SUMA = 0

class Bracket:
    def __init__(self, bracket):
        self.ID = BRACKETS.index(bracket)
        self.starting = self.ID < 4
        self.name = bracket

    def connect(self, other):
        return self.ID + 4 == other.ID

    def match(self, other):
        if not self.connect(other):
            global SUMA
            SUMA += illegal[other.ID]
            print(f"Expected {BRACKETS[self.ID + 4]}, but found {other.name}: {illegal[other.ID]}")


brackets = [[Bracket(bracket) for bracket in line] for line in input]


for line in brackets:
    stack = []
    for b in line:
        if b.starting:
            stack.append(b)
        else:
            stack.pop().match(b)


print("\nResult: ", SUMA)
