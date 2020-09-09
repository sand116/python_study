N, M, V = map(int, input().split())


matrix = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    link = list(map(int, input().split()))

    matrix[link[0]][link[1]] = 1
    matrix[link[1]][link[0]] = 1


def dfs(current_node, row, foot_prints):
    foot_prints += [current_node] # 방문 처리  
    for search_node in range(len(row[current_node])): # current_node와 인접 노드 
        if row[current_node][search_node] and search_node not in foot_prints: #방문하지 않았다면
            foot_prints = dfs(search_node, row, foot_prints) #재귀 호출함으로서 스택을 대신함
    return foot_prints


def bfs(start):
    queue = [start] # queue에 첫 노드 집어넣음
    foot_prints = [start] #방문처리를 해줌
    while queue: #큐가 비워질때까지
        current_node = queue.pop(0) #방문한 노드를 꺼냄 
        for search_node in range(len(matrix[current_node])):
            if matrix[current_node][search_node] and search_node not in foot_prints:
                foot_prints += [search_node]
                queue += [search_node]
    return foot_prints


print(*dfs(V, matrix, []))
print(*bfs(V))