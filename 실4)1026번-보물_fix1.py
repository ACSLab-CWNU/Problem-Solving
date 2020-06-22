N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort(reverse=True)
B.sort()
result = 0
sum = 0
for i in A:
    sum += i * B[result]
    result += 1
print(sum)