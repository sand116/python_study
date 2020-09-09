def fibonacci(n) :
    if n == 0:
        zero_dp[n] = 1
        one_dp[n] = 0
        return zero_dp[n], one_dp[n]
    
    elif n == 1 :
        zero_dp[n] = 0
        one_dp[n] = 1
        return zero_dp[n], one_dp[n]
    
    elif n == 2 :
        zero_dp = 1
        one_dp = 1
        return zero_dp[n], one_dp[n]
    
    elif zero_dp[n] != 0 and one_dp[n] !=0 :
        return zero_dp[n], one_dp[n]
    elif dp[n] == 0 :
        dp[n] = fibonacci(n-1) + fibonacci(n-2)
        return dp[n]

N = int(input())
zero_dp = [0]*(N+1)
one_dp = [0]*(N+1)
fibonacci(N)
print(dp[N])

# import sys
# def fibonacci(num) :
#     if num == 0 :
#         zero_count

# N = int(input())
# for _ in range(N) :
#     num = int(sys.stdin.readline().rstrip())
#     zero_count = [0]*num # 1 0 1 1 
#     one_count = [0]*num  #0 1 1 2
#     fibonacci(num)