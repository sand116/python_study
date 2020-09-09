def poly(n,first) :
    ret = 0
    if n == first :
        return 1
    if  cache[n][first] != -1 :
        return cache[n][first]
    
    for second in range(1,n-first+1) :
        add = first+second-1
        add *= poly(n-first,second)
        add %= MOD
        ret += add
        ret %= MOD
    cache[n][first] = ret
    return ret        
    
N = int(input())
MOD = 10000000
cache =[[-1]*101 for i in range(101)]
ret = 0
for i in range(1,N+1) :
   ret += poly(N,i)
print(ret)