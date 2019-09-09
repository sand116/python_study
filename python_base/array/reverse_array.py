# python array [::] 용법 - list, tuple, str 
num = '3212'
base = 5
answer = 0
for idx, i in enumerate(num[::-1]):
    answer += int(i) * ( base ** idx )
# int(x, base = 10) 함수는 진법 변환을 지원


# for 문 (0,0)(0,1) (0,2)..(0,n).. (1,0) (1,1) ,,(n,1) ..(n,n)
my_list = [[1,2,3,4],
           [5,6,7,8],
           [9,10,11,12],
           [13,14,15,16]]

# i =0 j = 1,2 i=1 j =2 i=2 

print([ i for i in my_list])
 
#range index넘어가는 경우 그냥 null [] 반환 
# for i in [] :
#     print(f" {i} ")  -> 그리고 이 상황에서 for문 안돌아감


#2차원 뒤집기
#c스러움 
def solution(mylist):
    new_list= [ [] for i in range(len(mylist))]
    for i in range(len(mylist)) :
        for j in range(len(mylist)) :
            print(i,j)
            # temp = mylist[j][i]
            # mylist[j][i] = mylist[i][j]
            # mylist[i][j] = temp
            new_list[i].append(mylist[j][i])
    return new_list

# python스러움

mylist = [ [1,2,3], [4,5,6], [7,8,9] ]
new_list = list(map(list, zip(*mylist)))

