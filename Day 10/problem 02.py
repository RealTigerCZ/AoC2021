path = "input.txt"

file = open(path)
input = [line[:-1] for line in file.readlines()]
file.close()

illegal = [1, 2, 3, 4, 3, 57, 1197, 25137]
BRACKETS = ["(", "[", "{", "<", ")", "]", "}", ">"]


class Bracket:
    def __init__(self, bracket):
        self.ID = BRACKETS.index(bracket)
        self.starting = self.ID < 4
        self.name = bracket
        self.val = illegal[self.ID]

    def complete(self):
        return BRACKETS[self.ID + 4]


brackets = [[Bracket(bracket) for bracket in line] for line in input]


SCORES = []
for line in brackets:
    stack = []
    mistake = False
    for b in line:
        if b.starting:
            stack.append(b)
        else:
            mistake = mistake or (stack.pop().ID + 4 != b.ID)

    if not mistake:
        print("Complete by adding ", end = "")
        for item in stack[::-1]:
            print(item.complete(), end = "")
        print(".")

        toAdd = 0
        while len(stack):
            toAdd = toAdd * 5 + stack.pop().val
        SCORES.append(toAdd)


print("\nResult: ", list(sorted(SCORES))[len(SCORES)//2])
