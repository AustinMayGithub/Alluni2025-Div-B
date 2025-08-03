size = int(input())

givers = [0 for _ in range(size)]
takers = [0 for _ in range(size)]

for _ in range(size):
    names = input().split(" ")
    n1 = names[0]
    n2 = names[1]
    givers.append(n1)
    takers.append(n2)

giverSet = set(givers)
takerSet = set(takers)

diff = giverSet.difference(takerSet)
for _ in diff:
    print(_)