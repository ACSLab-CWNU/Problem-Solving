# 처음시도 = 시간초과
# =============================================================================
# N = int(input())
# counter = 0
# test = []
# for i in range(pow(10, N-1), pow(10, N)):
#     if str(i).count('1') + str(i).count('0') != len(str(i)) : 
#         continue
#     elif str(i).count('11') != 0 :
#         continue
#     else:
#         counter += 1
#         test.append(i)
# print(counter)
# =============================================================================

N = int(input())
dp = [0 for i in range(91)]
dp[1] = 1
dp[2] = 1
dp[3] = 2
for i in range(4, 91):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[N])