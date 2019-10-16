def slicing(num_array,start_row,end_row,start_col,end_col) :
    sliced_array=[]
    row=0
    for i in range(start_row,end_row) :
        sliced_array.append([])
        for j in range(start_col,end_col) :
            sliced_array[row].append(num_array[i][j])
        row+=1
    return sliced_array

def solution(array, N, compress_list) :
    sum_of_array = sum([sum(i) for i in array])
    if sum_of_array == 0 :
        compress_list.append('0')
        
        return
    elif sum_of_array == N**2 :
        compress_list.append('1')       
        return
    else :
        compress_list.append("(")
        solution(slicing(array,0,N//2,0,N//2),N//2,compress_list)
        solution(slicing(array,0,N//2,N//2,N),N//2,compress_list)
        solution(slicing(array,N//2,N,0,N//2),N//2,compress_list)
        solution(slicing(array,N//2,N,N//2,N),N//2,compress_list)
        compress_list.append(")")

N = int(input())
array = [ [int(i) for i in list(input())] for _ in range(N) ]
compress_list = []
solution(array, N, compress_list)
print(''.join(compress_list))