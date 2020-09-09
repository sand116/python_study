# 우물을 기어오르는 달팽이
def climb(move, date) :
    if date == 0 :
        return 0
    if sum(move) >= N :
        return 1/(2**M)
    ret = climb(move+[1],date-1) + climb(move+[2],date-1)
    return ret 
    
        
    ret +=  
N = int(input())
M = int(input())
cache = [-1]*M  #확률 합 더하기
climb([0],M)