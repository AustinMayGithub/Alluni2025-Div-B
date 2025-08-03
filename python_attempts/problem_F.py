line = input()
lineSplit = line.split(" ")
numCats = int(lineSplit[0])
queries = int(lineSplit[1])

line = input()
split = line.split(" ")
costCats = list(map(lambda s: int(s), split))

line = input()
split = line.split(" ")
thresholds = list(map(lambda s: int(s), split))

for i in range(queries):
    total = 0
    for k in range(numCats):
        total += costCats[k]
        if total > thresholds[i]:
            total = k
            break
    print(total)