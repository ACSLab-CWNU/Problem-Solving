def min_cost(package, single, N):
    mincost = []
    mincost.append(N*min(single))
    if N >= 6 :
        if N%6 == 0:
            mincost.append(int((N/6))*min(package))
        else:
            mincost.append((int((N/6))*min(package)) + ((N%6)*min(single)))
            mincost.append(((int((N/6))+1)*min(package)))
    else:
        mincost.append(min(package))
    return min(mincost)
        
N, M = map(int, input().split())
cost = []
package = []
single = []
for _ in range(M):
    brand = list(map(int, input().split()))
    cost.append(brand)
for brand in cost:
    package.append(brand[0])
    single.append(brand[1])
    
print(min_cost(package, single, int(N)))