path = "input.txt"

file = open(path)
input = file.readlines()
file.close()

numbers = [int(num) for num in input[0].split(",")]


input.pop(0)

boards = []

while len(input) >= 6:
    input.pop(0)
    board = []
    for i in range(5):
        board.append(input.pop(0).split(" "))
    boards.append(board)


boards = [[[int(p) for p in line if p!=''] for line in board] for board in boards]

saved_boards = boards[:]

def tick_number(n):
    global boards
    boards = [[[-1 if p == n else p for p in line] for line in board] for board in boards]

def check_boards():
    global boards
    for index, board in enumerate(boards):
        for line in board:
            complete = True
            for p in line:
                if p != -1:
                    complete = False
                    break
            if complete:
                return index

        for i in range(5):
            complete = True
            for j in range(5):
                if board[i][j] != -1:
                    complete = False
                    break

        if complete:
            return index


final_board_index = None
iterator = -1
while not final_board_index:
    iterator += 1
    tick_number(numbers[iterator])
    final_board_index = check_boards()

#from pprint import pprint as pp
#pp(saved_boards[final_board_index])

sum = 0
for line in boards[final_board_index]:
    for p in line:
        if p != -1:
            sum += p

sum *= numbers[iterator]
print(numbers[iterator])
print(f"Result: ", sum)
