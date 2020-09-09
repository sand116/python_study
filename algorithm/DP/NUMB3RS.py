def located(start, days) :
    ret = 0
    cnt = 0
    if days == D :
        if start == P :
            return 1
        else :
            return 0 
    if location[start][days] == -1 :
        return location[start][days]
    
    for next,value in enumerate(location[start]) :
        if value == 1 :
            cnt += 1
            ret += located(next, days + 1 )
    if cnt != 0 :
        ret /= cnt
    location[start][days] = ret    
    return ret

N, D, P = map(int, input().split())
location = []
cache = [[-1]*D for i in range(N)]
for i in range(N) :
    row = list( map(int, input().split()) )
    location.append(row)
    
T = int(input())
for i in range(T) :
    Q= int(input())
    print(located(P,0))