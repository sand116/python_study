# 시작노드 설정  -> 넓이(길이 N : 100000) (1~100000)
# 이전 노드에서 가능한 높이까지는 다음 노드가 가능하다하더라도 최상값이 아니기때문에 이전 노드보다 높은 높이인경우만 센다
# 직사각형 모양 유지할때까지(높이가 안 끊기는 시점)  && 인접 방문할 1x1 정사각형 노드가 있는경우
# 시작노드 변경해서 계속 1x1 정사각형 노드 방문( 해당 노드는 더이상 방문하지 않음)
def solution(start,height, node_list) :
    if node_list[start][1] < height :
        return  
    if start > len(node_list) -1 :
        return
    node_list[start][2] = True
    solution(start+1,node_list)
    
N = [int(i) for i in list(input().split())]
node_list = []
for i in range(1,N[0]+1) :
    node_list.append((i,N[i],False))
solution(0,1,node_list) 
# for i in node_list :
#     i[0]

    