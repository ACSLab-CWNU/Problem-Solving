def check_divisor(number, count):
    if count%number == 0 :
        return 1
    else:
        return 0
number = list(map(int,(input().split())))
result = 0
count = 0    
while count < 3 :
    count = 0
    result += 1
    for i in number:
        count += check_divisor(i, result)
        
print(result)