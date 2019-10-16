   
def solution(N,num_array,white_count,blue_count):
    sum_count = sum([ sum(num_list) for num_list in num_array])
    if sum_count == 0 :
        white_count.append(1)
        return
    elif sum_count == N**2 :
        blue_count.append(1)
        return
    else :
        solution(N//2,slicing(num_array,0,N//2,0,N//2),white_count,blue_count)
        solution(N//2,slicing(num_array,0,N//2,N//2,N),white_count,blue_count)
        solution(N//2,slicing(num_array,N//2,N,0,N//2),white_count,blue_count)
        solution(N//2,slicing(num_array,N//2,N,N//2,N),white_count,blue_count)
    
def slicing(num_array,start_row,end_row,start_col,end_col) :
    sliced_array=[]
    row=0
    for i in range(start_row,end_row) :
        sliced_array.append([])
        for j in range(start_col,end_col) :
            sliced_array[row].append(num_array[i][j])
        row+=1
    return sliced_array
        
        
            

N = int(input())
# num_array = [ int(i) for _ in range(N) for i in list(input()) ]
# [1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0,
# 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1]
num_array = [ [int(i) for i in list(input())] for _ in range(N) ]
white_count = []
blue_count = []
solution(N,num_array,white_count, blue_count)
print(sum(white_count))
print(sum(blue_count))