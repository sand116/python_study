import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
student_list = []
for i in range(N) :
    temp = input().split()
    student = [temp[0]]+list(map(int,temp[1:]))
    student_list.append(student)

student_list.sort(key = lambda x : (-x[1],x[2],-x[3],x[0]))
for i in range(len(student_list)) :
    print(student_list[i][0])