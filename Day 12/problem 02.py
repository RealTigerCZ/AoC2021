path = "input.txt"

file = open(path)
input = [line[:-1] for line in file.readlines()]
file.close()
