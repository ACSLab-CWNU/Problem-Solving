def bfs(start):
    queue = [start]
    foot_prints = [start]
    while queue:
        current_node = queue.pop(0)
        for search_node in range(len(matrix[current_node])):
            if matrix[current_node][search_node] and search_node not in foot_prints:
                foot_prints += [search_node]
                queue += [search_node]
    return foot_prints
                
com = int(input())
connect = int(input())
matrix = [[0 for col in range(com+1)] for row in range(com+1)]
start_node = 1
for i in range(connect):
    index = list(map(int,input().split()))
    matrix[index[0]][index[1]] = 1
    matrix[index[1]][index[0]] = 1
print(len(bfs(start_node))-1)