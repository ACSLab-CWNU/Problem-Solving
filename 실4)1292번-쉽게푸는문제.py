n_list = []
index = 1
result = 0

while len(n_list) < 1000:
    for i in range(index):
        n_list.append(index)
    index += 1
A, B= list(map(int, input().split()))
for i in range(A-1, B):
    result += n_list[i]
print(result)
