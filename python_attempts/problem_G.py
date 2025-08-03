size = int(input())

accepted = [int(input())]
print('ACCEPTED')

for i in range(size-1):
    current_t = int(input())
    if i < 4:
        accepted.append(current_t)
        print('ACCEPTED')
        continue
    if current_t - accepted[i-5] > 10:
        accepted.append(current_t)
        print('ACCEPTED')
    else:
        print('DENIED')
        accepted.append(current_t)