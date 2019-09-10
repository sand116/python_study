


def permutations(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r # 예외처리
    
    if r > n:
        return
    #error 
    
    indices = range(n) # 5개를 3개씩으로 순열한다 가정 - 0,1,2,3,4
    cycles = range(n, n-r, -1) # 5,4,3
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return
arr = [1,2,3]
print(permute(arr)) #함수에 ary 전달 시 단순 복사 
print (arr) #객체 바뀌어있음 