path = "input.txt"

file = open(path)
input = file.readlines()
file.close()

numbers = [int(num) for num in input[0].split(",")]


class BingoCard:
    def __init__(self, board):
        self.board = board

    def tick_number(self, n):
        self.board = [[-1 if p == n else p for p in line] for line in self.board]

    def check(self):
        #rows
        for line in self.board:
            if sum(line) == -5:
                return True

        #colombs
        for i in range(5):
            if sum([p[i] for p in self.board])== -5:
                return True
        return False


    def calc_score(self, last_number):
        sum = 0
        for line in self.board:
            for p in line:
                if p != -1:
                    sum += p
        return sum * last_number


input.pop(0)

boards = []

while len(input) >= 6:
    input.pop(0)
    board = []
    for i in range(5):
        board.append(input.pop(0).split(" "))
    boards.append(board)

boards = [[[int(p) for p in line if p!=''] for line in board] for board in boards]

boards = [BingoCard(board) for board in boards]

for number in numbers:
    [board.tick_number(number) for board in boards]
    boards = [board for board in boards if not board.check()]

    if len(boards) == 1:
        final_board = boards[0]

    elif len(boards) == 0:
        print(final_board.calc_score(number))
        break
