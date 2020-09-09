from itertools import permutations

N, M = map(int , input().split())
permuation_list = permutations([ i for i in range(1,N+1)], M)

for i in permuation_list :
    for j in i :
        print(j, end=' ')
    print('')
    
    
                               
