N = int(input())
stair = [int(input()) for _ in range(N)]
dp = []
if N < 3 :
    if N == 1 :
        dp.append(stair[0])
    else:
        dp.append(max(stair[1]+stair[0], stair[1]))
else:
    dp.append(stair[0])
    dp.append(stair[1]+dp[0])
    dp.append(max(stair[2]+dp[0], stair[1] + stair[2]))
    for i in range(3, N):
        dp.append(max(stair[i] + stair[i-1]+ dp[i-3], stair[i]+ dp[i-2]))
    
print(dp[-1])