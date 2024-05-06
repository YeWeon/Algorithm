from collections import deque 

n = int(input())

maps = []
for i in range(n):
    maps.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[False] * len(maps) for i in range(n)]

def bfs(x, y):
    q = deque([(x, y)])
    count = 1
    while q:
        x, y = q.popleft() 
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < len(maps):
                if maps[nx][ny] == 1 and not visited[nx][ny]:
                    count += 1 
                    q.append((nx, ny))
                    visited[nx][ny] = True
    return count 

res = 0
count = []
for i in range(n):
    for j in range(len(maps)):
        if maps[i][j] == 1 and not visited[i][j]:
            visited[i][j] = True 
            count.append(bfs(i, j))
            res += 1

print(res)
count = sorted(count)
for i in range(res):
    print(count[i])
