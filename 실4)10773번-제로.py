n = int(input())

x = []

for i in range(n):
    a = int(input())
    if a == 0:
        if x == []:
            continue
        else:
            x.pop()
    else:
        x.append(a)

result = 0        
for i in range(len(x)):
    result = result + x[i]
    
print(result)