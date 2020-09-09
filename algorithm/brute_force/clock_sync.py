time = [int(input()) for _ in range(16)]
switch_by_time = [
    [0,1,2],[3,7,9,11],[4,10,14,15],[0,4,5,6,7],
    [6,7,8,10,12],[0,2,14,15],[3,14,15],
    [4,5,7,14,15],[1,2,3,4,5],[3,4,5,9,13]
    ]
here = 0
INF = 99999999
cnt = 123456789
clocksync(here, cnt, time)

def clocksync (here, time) :
    check = True
    if here == 10 : # 0~9 지난 경우 
        for i in range(time) :
            if i != 12 :
                check = False
                break
        if check == True :
            return 0
        else : 
            return INF
        
    ret = INF
    for cnt in range(4) :
        for i in switch_by_time[here] :
            if time[i]+3*cnt != 12 :
                time[i] = (time[i]+3*cnt) % 12
            else :
                time[i] = time[i]+3*cnt                    
        compare_num = cnt + clocksync(here + 1, time)
        for i in switch_by_time[here] :
            if time[i]-3*cnt == 0 :
                time[i] = 12
            else :
                time[i] = time[i] - 3*cnt
        ret = min([ret,compare_num])
    return ret