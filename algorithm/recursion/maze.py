def maze (start1,start2,end1,end2,maze,road) :
    if start1 == end1 and start2 == end2 :
        return road
    elif start1 == 0 : # 아래 왼쪽 오른쪽만 탐색
        
    elif start1 == end1 : # 위 왼쪽 오른쪽만 탐색
    elif start2 == 0 : # 위 아래와 오른쪽만 탐색
    elif start2 == end2 : # 위 아래 왼쪽만 탐색
    else : # 아래 위 왼쪽 오른쪽 전체 탐색

    if maze[i+1][j] == 1 and start1 != end1 :
        road.append(maze[i+1][j])
        maze(start1+1,start2,end1,end2,maze)
    else :
        
    elif maze[i+1]
        
    if maze[i][j+1] == 1 :
        maze(start1+1,start2,end1,end2,maze)
    