from collections import deque


test_case = int(input())

for _ in range(test_case) :
    N, M = map(int, input().split())
    importance = list(map(int, input().split()))
    max_importance = max(importance)
    q = deque()
    count = 0
    for i in range(N) :
        q.append(i)
    while q :
        pop_item = q.popleft()
        if pop_item == M and importance[pop_item] == max_importance :
            print(count+1)
            break
        elif importance[pop_item] == max_importance :
            importance[pop_item] = -1
            max_importance = max(importance)
            count +=1
            continue
        else :
            q.append(pop_item)
            continue
            
        
        
    
    