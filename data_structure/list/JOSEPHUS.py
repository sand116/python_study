    
def killing(N,killed_idx) :
    if N <= 2 :
        return people[0],people[1]
    del people[killed_idx]
    N -= 1
    next =  killed_idx + 2
    if next >= N :
        next = next-N
    ret = killing(N,next)
    return ret
N, K = map(int, input().split())
people = [ i+1 for i in range(N) ]
print(killing(N,0))

        [].a

    
    