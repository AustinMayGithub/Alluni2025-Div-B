inLine = input().split(" ")
size = int(inLine[0])
taken =int( inLine[1])

diffs = [0 for _ in range(size)]

for i in range(size):
    inl = input().split(" ")
    diff = int(inl[0]) - int(inl[1])
    diffs[i] = diff

print(sum(sorted(diffs, reverse=True)[:taken]))