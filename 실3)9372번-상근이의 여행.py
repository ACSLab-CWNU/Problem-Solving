# -*- coding: utf-8 -*-
"""
정답 제출시 언어를 pypy3으로 제출
"""

N = int(input())

for i in range(N):
    a,b = map(int,input().split())
    for j in range(b):
        c,d = map(int,input().split())
    print(a-1)

