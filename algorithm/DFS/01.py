from collections import deque
N ,M = map(int, input().split())
board = [list(map(int,input())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
q=deque()
q.append((0,0))
dir = [(-1,0),(1,0),(0,1), (0,-1)]
visited[0][0]=1
while q :
      now = q.popleft()
      for y,x in dir :
          nexty=now[0]+y
          nextx=now[1]+x
          if nexty<0 or nexty>=N or nextx<0 or nextx>=M :
              continue
          if board[nexty][nextx] == 1 and visited[nexty][nextx] == 0:
              q.append((nexty,nextx))
              visited[nexty][nextx]=visited[now[0]][now[1]]+1

      
print(visited[N-1][M-1])

