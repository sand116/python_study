def fibonacci(n) :
    if n == 1 :
        dp[n] =1
        return dp[n]
    elif n == 2 :
        dp[n]= 1
        return dp[n]
    elif dp[n] != 0 :
        return dp[n]
    elif dp[n] == 0 :
        dp[n] = fibonacci(n-1) + fibonacci(n-2)
        return dp[n]

N = int(input())
dp =[0]*(N+1)
fibonacci(N)
print(dp[N])