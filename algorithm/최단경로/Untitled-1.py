

n, m, x = map(int, input().split())
INF = int(1e9)

# 방문했는지 확인
visited = [False]*(n+1)

# 현재 단계의 최단거리 테이블
distance = [INF]*(n+1)

# 지도 
board = [[] for i in range(n+1)]

for i in range(m) :
    y, x, t = map(int, input().split())
    board[y].append((x,t))
    
def get_small_node() :
    min_value = INF
    index = 0
    for i in range(1, n+1) :
        if distance[i] < min_value and not visited[i] :
            min = distance[i]
            index = i
    return index
        
def dijkstra(start) :
    # 방문지 체크 
    visited[start]=True
    
   # 시작 노드 제외하고 모든 노드에 대해 반복하기
    for i in range(n-1) : 
     # 방문지에서 연결된 노드 중 아직 방문하지 않은 노드 중 가장 짧은 노드를 꺼내서 방문 처리 
        now = get_small_node()
        visited[now]=True
        # 선택된 노드에 연결된 노드 확인
        for next in board[now] :
            cost = distance[now]+next[1]
            
            # 선택된 노드를 거쳐서 다른 노드로 이동하는 경우가, 기존 최단경로보다 더 짧은 경우 갱신 
            if cost < distance[next[0]] :
                distance[next[0]] = cost
    
    


# 도착 마을에서 시작 
dijkstra(x)