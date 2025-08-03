from itertools import product

alphaDict = {
    'a' : 0,
    'b' : 1,
    'c' : 2,
    'd' : 3,
    'e' : 4,
    'f' : 5,
    'g' : 6,
    'h' : 7,
    'i' : 8,
    'j' : 9,
    'k' : 10,
    'l' : 11,
    'm' : 12,
    'n' : 13,
    'o' : 14,
    'p' : 15,
    'q' : 16,
    'r' : 17,
    's' : 18,
    't' : 19,
    'u' : 20,
    'v' : 21,
    'w' : 22,
    'x' : 23,
    'y' : 24,
    'z' : 25,  
}

vowels = ['a', 'e', 'i', 'o', 'u']
first5 = ['a', 'b', 'c', 'd', 'e']

size = int(input())

for _ in range(size):
    instr = input()
    inl = instr.split(" ")
    a = int(inl[0])
    b = int(inl[1])
    c = int(inl[2])
    score = 3380 * c + 10140 * a + 5858 * b
    print(f'{(score / (26 * 26 * 26)):.2f}')