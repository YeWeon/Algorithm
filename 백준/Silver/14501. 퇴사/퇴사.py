n = int(input())

t = []
p = []
for i in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)

dp = [0] * (n+1)
for i in range(n-1, -1, -1):
    if t[i] + i <= n:
        dp[i] = max(dp[i+1], p[i] + dp[t[i] + i]) 
    else:
        dp[i] = dp[i+1]
    

print(dp[0])

