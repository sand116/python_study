def set(x,y,type, delta) :
    bool_ret = True
    for i in range(3) :
        next_y = y + select[type][i][0]
        next_x = x + select[type][i][1]
        # index 를 넘기는 접근은 무조건 미리 확인 
        if next_x < 0 or next_y < 0 or next_x >= len(board[0]) or next_y >= len(board):
            bool_ret = False
        elif (board[next_y][next_x] + delta) > 1 :
            bool_ret =  False
        board[next_y][next_x] += delta    
    return bool_ret
def cover(board) :
    y,x = -1, -1 # 항상 초기화는 상황에서 벗어난 상황으로 초기화하기
    ret = 0
    for row_idx, row in enumerate(board) :
        for col_idx, value in enumerate(row) :
            if value == 0 :
                y,x = row_idx, col_idx
                break
        if y != -1 : break
    if y == -1 :
        return 1 
    for i in range(4) :
        if set(x,y,i,1) :
            ret += cover(board)
        set(x,y,i,-1)
    return ret


C = int(input())
select =[
        [[0,0],[1,0],[0,1]],
        [[0,0],[0,1],[1,1]],
        [[0,0],[1,0],[1,1]],
        [[0,0],[1,0],[1,-1]],
         ]
        
for i in range(C) :
    h, w = map(int, input().split())
    board=[0]*h
    cnt = 0
    for i in range(h) :
        row = []
        for j in list(input()) : 
            if j == '#' :
                row.append(1)
            if j == '.' :
                row.append(0)
                cnt +=1
        board[i] = row
    print(board)
    if cnt %3 != 0 :
        print(-1)
    else :
        print(cover(board))
    
                
    