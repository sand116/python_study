N, K = map(int, input().split())
queue = [i for i in range(1,N+1)] # 1 ~ N 개 
front = 0
permutation = []
while queue :
    for _ in range(K-1) :    
        queue.append(queue.pop(0))
    permutation.append(str(queue.pop(0)))

print('<'+', '.join(permutation)+'>')
    