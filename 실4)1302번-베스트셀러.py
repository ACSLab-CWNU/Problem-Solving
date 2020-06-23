from collections import Counter
N = int(input())
book_list = []
for i in range(N):
    book_list.append(str(input()))
book_list.sort()
result = Counter(book_list)
word = sorted(result.items(), key=lambda x: x[1], reverse=True)
print(word[0][0])