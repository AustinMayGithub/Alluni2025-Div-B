from math import comb
from itertools import permutations

size = int(input())

cardNs={}

inLine = input().split(" ")

for card in inLine:
    if card in cardNs:
        cardNs[card] += 1
    else:
        cardNs[card] = 1
        
goodNs = list(filter(lambda a: a >= 2, [n for n in cardNs.values()]))
handGoods = 0
for p in permutations(goodNs, r=2):
    handGoods += comb(p[0], 2) * comb(p[1], 3) + comb(p[0], 3) * comb(p[1], 2)
print(handGoods / (2*comb(size, 5)))