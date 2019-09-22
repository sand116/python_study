def bw_test(array) :
    change_count = 0
    for i in range(len(array)) :
        for j,entity in enumerate(array[i]) :
            if i%2 == 0 :
                if j%2 == 0:
                    if entity != "B" :
                        change_count += 1
                else : 
                    if entity != "W" :
                        change_count += 1
            else :
                if j%2 == 0:
                    if entity != "W" :
                        change_count += 1
                else : 
                    if entity != "B" :
                        change_count += 1
    return change_count
def wb_test(array) :
    change_count = 0
    for i in range(len(array)) :
        for j,entity in enumerate(array[i]) :
            if i%2 == 0 :
                if j%2 == 0:
                    if entity != "W" :
                        change_count += 1
                else : 
                    if entity != "B" :
                        change_count += 1
            else :
                if j%2 == 0:
                    if entity != "B" :
                        change_count += 1
                else : 
                    if entity != "W" :
                        change_count += 1
    return change_count

N,M = map(int,input().split()) #8,9
array = [ list(input()) for _ in range(N)]
num_count = []
sliced_list = []
for i in range(len(array) - 7) : #1
    for j in range(len(array[0]) - 7) : # 2
        sliced_array = []
        for c in range(i,i+8) : #0,8
            for l in range(j,j+8) : #0,8 / 1,9
                sliced_list.append(array[c][l])
            sliced_array.append(sliced_list) 
            sliced_list = [] #새로운 리스트 객체 할당
        # 2차원 array에 할당하려면 미리 2차원 리스트 만들어 놓아야함
        #print('\n'*3)
        num1 = bw_test(sliced_array)
        num2 = wb_test(sliced_array)
        if num1 > num2 :
            num_count.append(num2)
        else : num_count.append(num1)
print(min(num_count))