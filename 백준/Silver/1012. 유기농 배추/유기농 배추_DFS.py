import sys
sys.setrecursionlimit(100000)
T = int(input())

for tc in range(T):
    m, n, k = map(int, input().split())

    maps = [[0] * m for i in range(n)]

    for _ in range(k):
        x, y = map(int,input().split())
        maps[y][x] = 1

    def dfs(x, y) :
        if x < 0 or x >= n or y < 0 or y >= m:
            return False 
        
        if maps[x][y] == 1 :
            maps[x][y] = 0 
            dfs(x-1, y)
            dfs(x+1, y)
            dfs(x, y-1)
            dfs(x, y+1)
            return True 
        
        return False 

    res = 0
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 1:
                if dfs(i,j):
                    res += 1 

    print(res)
