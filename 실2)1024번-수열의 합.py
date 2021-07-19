n, l = map(int, input().split())

t = 0
x = -1
result = 0

for i in range(l, 101):
    t = (i * i - i) / 2
    if (n - t) % i == 0 and (n - t) // i >= 0:
        x = (n - t) // i
        result = i
        break

if x == -1:
    print(-1)
else:
    for i in range(result):
        print(int(x + i))
