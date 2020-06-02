N = int(input())

numbers = []

for _ in range(N): 
    numbers.append(int(input()))

for i in range(len(numbers)-1):
    min = i
    for j in range(i+1,len(numbers)):
        if numbers[j] < numbers[min]:
            min = j
    
    tmp = numbers[i]
    numbers[i] = numbers[min]
    numbers[min] = tmp
            
for n in numbers: 
    print(n)