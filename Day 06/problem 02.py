path = "input.txt"

file = open(path)
input = file.readlines()
file.close()

all_fish = [[int(x) for x in line.split(",")] for line in input][0]

fish_count_by_index = [0 for _ in range(9)]

for fish in all_fish:
    fish_count_by_index[fish] += 1

for day in range(256):
    zeros = fish_count_by_index.pop(0)
    fish_count_by_index.append(zeros)
    fish_count_by_index[6] += zeros


print(sum(fish_count_by_index))
