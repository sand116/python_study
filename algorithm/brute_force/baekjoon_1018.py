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
N,M = map(int,input().split())
two_array = [ list(input()) for i in range(N)]
num_count = []
for i in range(len(two_array)-7) :
    for j in range(len(two_array[0])-7) :
        num1 = bw_test(two_array[i:i+8][j:j+8])
        num2 = wb_test(two_array[i:i+8][j:j+8])
        if num1 > num2 :
            num_count.append(num2)
        else : num_count.append(num1)

print(num_count)