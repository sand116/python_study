def path (y, x) :
    if y == N - 1 :
        return triangle[y][x]
    ret = cache[y][x]
    if ret != -1 :
        return ret
    else :
        cache[y][x] = max(path(y+1,x),path(y+1,x+1)) + triangle[y][x]
        return cache[y][x]    
N = int(input())
M = int(input())
triangle = []
cache = []
for i in range(N) :
    triangle.append(list(map(int, input().split())))
for i in range(N) :
    cache.append([-1]*M)
print(path(0,0))