import sys 
sys.setrecursionlimit(1000000)
n, m = map(int, input().split())

maps = []
for _ in range(n):
    maps.append(list(map(int, input())))

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False 
    
    if maps[x][y] == 0:
        maps[x][y] = 2
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True 
    
    return False 

for i in range(m):
    if maps[0][i] == 0:
        dfs(0, i)

if 2 in maps[n-1]:
    print("YES")
else:
    print("NO")
