def bfs(first_node) :
    queue, foot_prints = [first_node], [first_node]
    while queue :
        current_node = queue.pop(0)
        for search_node in range(len(matrix[current_node])) :
            if matrix[current_node][search_node] and search_node not in foot_prints : 
                queue.append(search_node)
                foot_prints.append(search_node) #큐에 넣고 방문처리를 해줌 
    return len(foot_prints[1:])
                 
            

N = int(input())
M = int(input())
matrix = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M) :
    a, b = map(int, input().split())
    matrix[a][b] = 1
    matrix[b][a] = 1
print(bfs(1))
    