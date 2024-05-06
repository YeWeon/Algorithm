from collections import deque 

m, n = map(int, input().split())

tomato = []
pos = []
for i in range(n):
    tomato.append(list(map(int, input().split())))
    for j in range(m):
        if tomato[i][j] == 1:
            pos.append((i, j))
            
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque(pos)
while q:
    x, y = q.popleft() 
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx < n and 0 <= ny < m:
            if tomato[nx][ny] == 0:
                tomato[nx][ny] = tomato[x][y] + 1 
                q.append((nx, ny))

res = -1e9
check = True
for i in range(n):
    for j in range(m):
        res = max(res, tomato[i][j])
        if (tomato[i][j] == 0):
            check = False
            
if(check):
    print(res - 1)
else:
    print(-1)