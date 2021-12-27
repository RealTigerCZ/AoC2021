path = "input.txt"

file = open(path)
input = file.readlines()
file.close()

segments_to_number = {2:"1", 4:"4" , 3:"7" , 7:"8"}

print(sum([len([n for n in line.strip("\n").split("|")[1].split(" ") if len(n) in list(segments_to_number.keys())]) for line in input]))
