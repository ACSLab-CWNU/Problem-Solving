import math
def factorial(n):
    return math.factorial(n)
def Combination(n,r):
    return int(factorial(n)/(factorial(r)*factorial(n-r)))
n = int(input())
for i in range(n):
    bridge = input().split()
    print(Combination(int(bridge[1]),int(bridge[0])))
    
