import copy
def combination(num_list,selected_list,result,start,N) :
    if start == N :
        result.append([ _ for _ in selected_list])
        return
    for i,j in enumerate(num_list[:N+1]) :
        combination(num_list[i+1:], [j]+selected_list, result, start+1, N)
               
            
        
N = int(input()) 
num_list = [1,2,3,4,5,6]
selected_list = []
result = []
start = 0
combination(num_list,selected_list,result,start,N)
print(result)
