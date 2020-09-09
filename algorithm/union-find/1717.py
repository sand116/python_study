# find의 시간복잡도에 의해 결정
import sys

def union(node1, node2) : #해당 노드의 부모노드끼리 연결 
    root1 = find(node1)
    root2 = find(node2)
    
    if root1 == root2 :
        return
    parent[root2] = root1
    
def find(node) : # 부모노드를 찾는 것 
    if parent[node] == node : #최상위 노드인 경우에는 부모노드와 자신의 값이 같음
        return node
    parent[node] = find(parent[node])
    return parent[node]

def compare(node1, node2) :
    root1 = find(node1)
    root2 = find(node2)
    if root1 == root2 :
        return "YES\n"
    else :
        return "NO\n"

N, M = map(int, sys.stdin.readline().split())
parent = [ i for i in range(N+1)]
for _ in range(M) :
    select, node1, node2 = map (int, sys.stdin.readline().split())
    if select == 0 :
        union(node1, node2)
    elif select == 1 :
        sys.stdout.write(compare(node1, node2))
      

'''
import sys

def find(u:int)->int:
    if(parent[u] == u) :return u
    parent[u] = find(parent[u])
    return parent[u]

def merge(u:int, v:int):
    u = find(u)
    v = find(v)
    if(u == v): return
    parent[u] = v

N, M = map(int, sys.stdin.readline().split())

parent = [i for i in range(0, N+1)]


for i in range(0, M):
    a,b,c = map(int, sys.stdin.readline().split())
    if(a == 0): merge(b,c)
    else:
        A:int = find(b)
        B:int = find(c)
        if(A == B): sys.stdout.write("YES\n")
        else: sys.stdout.write("NO\n")

'''