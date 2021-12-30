import os, sys

day_number = int(input("Day number: "))

day_path = "Day %02d" % day_number

PATH = os.path.join(sys.path[0], day_path)

os.mkdir(PATH)
print(f"Created '{day_path}' folder in {PATH}")


TEMPLATE = """path = "input.txt"

file = open(path)
input = [line[:-1] for line in file.readlines()]
file.close()
"""

URL = """[InternetShortcut]
URL=https://adventofcode.com/2021/day/%d
""" % day_number

url_file = open(os.path.join(PATH, "Day %d - Advent of Code 2021.url" % day_number), "w+")
url_file.write(URL)
url_file.close()
print(f"Created '{url_file.name}' file")

input = open(os.path.join(PATH, "input.txt"), "w+")
input.close()
print(f"Created '{input.name}' file")

sample = open(os.path.join(PATH, "sample.txt"), "w+")
sample.close()
print(f"Created '{sample.name}' file")

problem1 = open(os.path.join(PATH, "problem 01.py"), "w+")
problem1.write(TEMPLATE)
problem1.close()
print(f"Created '{problem1.name}' file")

problem2 = open(os.path.join(PATH, "problem 02.py"), "w+")
problem2.write(TEMPLATE)
problem2.close()
print(f"Created '{problem2.name}' file")
