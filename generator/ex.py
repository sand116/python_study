def sum_generator(max = 10) :
    sum = 0
    i = 0
    num_list =[1,2,3,4,5,6,7,8,9,20]
    while(True) :
        if sum > 10 :
            break
        yield num_list[i]
        i+=1
        sum+= num_list[i]
    
for i in sum_generator(10) :
    print(i)
# yeild의 개수대로 for문이 돌아감  