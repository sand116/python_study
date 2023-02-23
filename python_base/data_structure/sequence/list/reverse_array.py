# python array [::] 용법 - list, tuple, str 
num = '3212'
num2 = list(num)
base = 5
answer = 0
print(num[::])

for idx, i in enumerate(num[::-1]): #num2 가능
    print(idx, i)
    answer += int(i) * ( base ** idx )
# int(x, base = 10) 함수는 진법 변환을 지원


# for 문 (0,0)(0,1) (0,2)..(0,n).. (1,0) (1,1) ,,(n,1) ..(n,n)
my_list = [[1,2,3,4,5],
           [6,7,8,9,10],
           [11,12,13,14,15]]

# i =0 j = 1,2 i=1 j =2 i=2 


 
#range index넘어가는 경우 그냥 null [] 반환 
for i in [] :
    print(f" {i} ")  #-> 그리고 이 상황에서 for문 안돌아감


#2차원 뒤집기

# 1.c스러움 
def solution(mylist):
    new_list = []
    for i in range(4) :
        new_list.append([row[i] for row in my_list])
    return new_list


# 2. python스러움
transpose_matrix = [[row[i] for row in my_list] for i in range(len(my_list[0]))]
print(transpose_matrix)

#3. 리스트 언패킹
mylist = [ [1,2,3], [4,5,6], [7,8,9] ]

#바깥 쪽 리스트 언패킹
print(*mylist)

new_list = list(map(list, zip(*mylist)))


# list comprehension 이해 
list_comp=[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]

# 동일 코드 - for 문과 if문의 논리 순서가 동일함
combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))



