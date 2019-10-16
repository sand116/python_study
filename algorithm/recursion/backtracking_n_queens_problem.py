# 백트래킹 - 모든 경우의 수를 다하지만, 다시 뒤로 돌아가 자신의 최근의 결정을 번복하는 것을 말함. 즉,
# 상태공간 트리를 깊이 우선 방식으로 탐색하여 해를 찾는 알고리즘을 말한다
'''
상태공간 트리 - 찾는 해를 포함하는 트리 : 
해가 존재한다면 그것은 반드시 이 트리의 어떤 한 노드에 해당함 
따라서 이 트리를 체계적으로 탐색하면 해를 구할 수 있음. 그러나 상태공간 트리의 모든 노드를 탐색해야 하는 것은 아님

백트래킹을 해결하는 방법은 일반적으로 두가지가 있음.
1. recursion
2. stack
'''


cols = [ 0 for _ in range(0,5)]
# list index = tree level / list 안의 값 = column
def check(level) :
    for i in range(level) :
        if cols[i] == cols[level] :
            return False 
        elif level-i == abs(cols[level]-cols[i]) :
            return False


def queens(level) :
    if check(level) == False :
        return False
        # 언프로미스한 경우
    elif level == 4 :
        print(cols[1:])
        return True
    for i in range(4) : # 자식 노드를 어디에 둘거냐 
        cols[level+1] = i+1
        queens(level+1)

# queens(0으로 호출)
queens(0)