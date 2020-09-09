import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
num_list = [ int(input()) for i in range(N)]

for i in sorted(num_list) :
    print(i)