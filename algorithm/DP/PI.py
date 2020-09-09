
def classify(begin, end) :
    sub_num = num[begin:end+1]
    if sub_num.count(sub_num[0])==len(sub_num) :
        return 1
    
    progressive = True
    for i in range(len(sub_num)-1) :
        differ = sub_num[i]- sub_num[i+1]
        if (sub_num[0]- sub_num[1]) != differ :
         progressive = False
    alternating =  True 
    
    for i in range(len(sub_num)) :
        if sub_num[i] != sub_num[i%2] :
            alternating = False
            
    if progressive :
        if abs(differ) == 1 :
            return 2
        else :
            return 5
    if alternating :
        return 4
    
    return 10 
            
    
def memorize(begin) : # 부분수열의 시작 위치가 주어졌을 때 최소 난이도를 반환한다
    ret = 123456789
    if begin == len(num) : #수열의 마지막에 도달한 경우 
        return 0 
    
    if cache[begin] != -1 :
        return cache[begin]
    
    for L in range(3,6) :
        if begin + L <= len(num) :
            cache[begin] = min(ret,classify(begin,begin+L-1)+memorize(begin+L))
            ret = cache[begin]
            
    return ret

N = int(input())
for i in range(N) :
    num = list(map(int, list(input())))
    cache = [-1]*(len(num))
    print(memorize(0))
