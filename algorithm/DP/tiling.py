def tiling(width) :
    if width <= 1 :
        return 1
    ret = cache[width]
    if ret != -1 :
        return ret
    
    ret = (tiling(width - 1) + tiling( width - 2 ))%MOD
    cache[width] = ret
    return ret
def asymetric (width) :
    if width%2 == 1 :
        return (tiling(width) - tiling(width//2) + MOD)%MOD
    else :
        ret = (tiling(width)-tiling(width//2)+MOD)%MOD
        ret = (ret-tiling(width//2-1)+MOD)%MOD
        return ret
N = int(input())
MOD = 1000000007
cache= [-1]*(N+1) #width 가 0 부터 N개까지있을 수 있음
print(asymetric(N))