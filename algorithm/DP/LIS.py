def partial(start) :
    ret = 1
    if start == len(num1)-1 :
        return ret
    if cache[start] != 0 :
        return cache[start]
    for i in range(start+1,len(num1)):
        if num1[i] > num1[start] :
            ret = max(ret, 1+partial(i))
            cache[start] = ret
    return ret
            

num1 = list(map(int,input().split())) # 수의 크기는 100으로 제한
#num2 = list(map(int,input().split())) # 수의 크기는 100으로 제한

cache = [0]*101

maxlen=0
for i in range(len(num1)) :
    maxlen = max(maxlen, partial(i))
print(maxlen)