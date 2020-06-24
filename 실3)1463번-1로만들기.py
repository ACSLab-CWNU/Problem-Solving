X = int(input())
count = 0
minimum = [X]
def calc(a):
    result = []
    for i in a:
        result.append(i-1)
        if i % 3 == 0:
            result.append(i/3)
        if i % 2 == 0 :
            result.append(i/2)
    return result
while True:
    if X == 1:
        print(count)
        break
    tmp = minimum[:]
    minimum = []
    minimum = calc(tmp)
    count += 1
    if min(minimum) == 1:
        print(count)
        break