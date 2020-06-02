n = int(input())

count = 0
while n > 0:
    if n % 5 == 0:
        n = n - 5
        count = count + 1
        
    elif n % 3 == 0:
        n = n - 3
        count = count + 1
    
    elif n > 5:
        n = n - 5
        count = count + 1
                   
    else:
        count = -1
        break
    
print(count)