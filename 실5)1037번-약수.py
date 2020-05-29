N = int(input())
measure = []
a = input().split()
measure.append(a)
measure = list(map(int, a))

if N == 1:
    print(max(measure)**2)
else :
    print(max(measure)*min(measure))
    
