path = "input.txt"

file = open(path)
input = file.readlines()
file.close()


horizontal = 0
aim = 0
depth = 0

for item in input:
    dir, speed = item.split(" ")
    if dir == "forward":
        horizontal += int(speed)
        depth +=  int(speed) * aim
    elif dir == "down":
        aim += int(speed)
    elif dir == "up":
        aim -= int(speed)
    else:
        assert False, "Unreachable"

print(f"horizontal: {horizontal}, depth: {depth}, h * d = {horizontal*depth}")
