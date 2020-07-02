# -*- coding: utf-8 -*-
"""
정답 제출시 언어를 pypy3으로 제출
"""
import sys
N = int(input())

result=0
num=0
i=1
test = []

while True:
    result += i
    if (num + result) > N:
        break
    else:
        num += result
        test.append(num)
        i += 1

C = []
for a in range(N+1):
    C.append(sys.maxsize)    
C[0] = 0

for j in range(1,N+1):
    for i in range(len(test)):
        if test[i] <= j and C[j-test[i]]+1<C[j]:
            #print('true')
            C[j] = C[j-test[i]]+1

print(test)            
print(C[-1])
