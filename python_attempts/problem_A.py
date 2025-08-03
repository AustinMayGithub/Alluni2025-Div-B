size = int(input())

ourDict = {}

for _ in range(size):
    line = input()
    lineSplit = line.split(" ")
    game = lineSplit[0]
    num = int(lineSplit[1])
    if game in ourDict:
        if num > ourDict[game]:
                ourDict[game] = num
                print(f'Play {game}')
        else: 
            ourDict[game] = num
            print(f'Skip {game}')
    else:
        ourDict[game] = num
        print(f'Play {game}')
        