result = []
N, k = map(int,input().split())
human = list(range(1,N+1))
temp = int(k) - 1
for i in range (N):

    if len(human) > temp:
        result.append(human.pop(temp))
        temp += k - 1
    else:
        temp %= len(human)
        result.append(human.pop(temp))
        temp += k - 1

print('<', end ='')
print(", ".join(map(str, result)), end ='')
print('>', end ='')