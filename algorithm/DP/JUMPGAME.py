
def jump( right, down) : #right, down
    if right >= 7 or down >= 7 :
        return 0
    
    elif right == 6 and down == 6 :
        return 1
    
    elif foot_print[right][down] != -1 :
        return foot_print[right][down]
    
    jumpsize = board[right][down]
    foot_print[right][down] = int (jump(right+jumpsize,down) or jump(right, down+ jumpsize))
    return foot_print[right][down]



board = []
foot_print = []
#board
for i in range(7) :
    board.append(list(map(int, input().split())))
#초기화   
for i in range(7) :
    foot_print.append([-1]*7)

print(jump(0,0))
# 함수
