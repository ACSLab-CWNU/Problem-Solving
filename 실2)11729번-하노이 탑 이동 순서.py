# -*- coding: utf-8 -*-

N = int(input())

def hanoi(n,start,last,mid):
    if(n == 1):
        print("{} {}".format(start,last))
        return
        
    hanoi(n-1,start,mid,last)
    print("{} {}".format(start,last))
    hanoi(n-1,mid,last,start)

print(2**N-1)
hanoi(N,1,3,2)