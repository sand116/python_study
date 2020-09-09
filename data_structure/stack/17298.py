N = int(input())
num_list = []
for index, value in enumerate(input().split()) :
    num_list.append((index,int(value)))
output_list = [0]*(N)
stack = []
for i,j in num_list :
    while(stack != []) :
        if stack[-1][1] < j :
            #pop 한 것의 원래 인덱스 부분에 j 값을 넣어야 한다
            idx = stack.pop()[0]
            output_list[idx] = j
        else : break
    stack.append((i,j))
for i,j in enumerate(output_list) :
    if j == 0 :
        output_list[i] = -1

print(' '.join(map(str,output_list)))