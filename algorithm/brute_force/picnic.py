import array
def make_relationship() :
    relationship_array = [0]*n
    for i in range(n) :
        relationship_array[i] = [0]*n
    i = 0
    for _ in range(m) :
        a, b = relationship[i], relationship[i+1] 
        relationship_array[a][b]=1
        relationship_array[b][a]=1
        i+=2
    return relationship_array

def solution(taken) :
    first = -1
    for i,j in enumerate(taken) :
        if j == 0 :
            first = i
            break
            
    if first == -1 :
        return 1
    ret = 0 
    for pair in range(first+1,n) :
        if taken[pair]  == 0 and relationship_array[first][pair] != 0 :
            taken[first] = 1
            taken[pair] = 1
            ret += solution(taken)
            taken[first], taken[pair] = 0, 0
    return ret
    
C = int(input())
for i in range(C) :
   n, m = map(int, input().split())
   relationship =  list(map(int,input().split()))
   relationship_array = make_relationship()
   taken = [0]*n
   print(solution(taken))
