from itertools import permutations

N, M = input().split()
n_list = list(range(1,int(N)+1))
n_result = []
for i in list(permutations(n_list,int(M))):
    n_result.append(i)

for i in n_result:
    print(' '.join(map(str, i)))