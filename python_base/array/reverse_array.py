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
    new_list = []
    for i in range(4) :
        new_list.append([row[i] for row in my_list])
    return new_list

# python스러움
#
transpose_matrix = [[row[i] for row in my_list] for i in range(4)]

# ex1 리스트 언패킹
mylist = [ [1,2,3], [4,5,6], [7,8,9] ]

new_list = [map(list, zip(*mylist))]
# zip도 iterator 객체
print(new_list)




# ex1
list_comp=[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
# 동일 코드 - for 문과 if문의 논리 순서가 동일함
combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))



