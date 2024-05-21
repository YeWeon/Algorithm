from collections import deque

n, m = map(int, input().split())

maps = []
visited  = [[False] * m for i in range(n)]
for _ in range(n):
    maps.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x, y):
    q = deque([(x, y)])

    while q:
        x, y = q.popleft() 
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] == 0 and not visited[nx][ny]:
                    visited[nx][ny] = True 
                    q.append((nx, ny))
            elif nx >= n:
                return True 
            
res = "NO"
for i in range(m):
    if maps[0][i] == 0 and not visited[0][i]:
        if bfs(0, i):
            res = "YES"

print(res)