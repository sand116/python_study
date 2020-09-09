import sys
input = lambda : sys.stdin.readline().rstrip()

def solution() :
    num_list = [int(input()) for _ in range(N)]
    num_pointer = 0
    i = 1 
    for i in range(1,N+1) :
        if i <= num_list[num_pointer] :
            stack_list.append(i)
            push_pop.append("+")
       
        while ( stack_list != [] and num_pointer <= N-1 ) :
            if stack_list[-1] == num_list[num_pointer] : 
                stack_list.pop()
                push_pop.append("-") 
                num_pointer += 1
            else : break
    return

N = int(input())

stack_list = []
push_pop = []
solution()
if stack_list == [] :
    for i in push_pop :
        sys.stdout.writelines(i+"\n")
else :
    sys.stdout.writelines("NO")




