from collections import deque

T = int(input())

for tc in range(T):
    m, n, k = map(int, input().split())

    maps = [[0] * m for i in range(n)]
    visited = [[False] * m for i in range(n)]

    for _ in range(k):
        x, y = map(int,input().split())
        maps[y][x] = 1

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
                    if maps[nx][ny] == 1 and not visited[nx][ny]:
                        visited[nx][ny] = True
                        q.append((nx, ny))


    res = 0
    for i in range(n):
        for j in range(m):
            if  maps[i][j] == 1 and not visited[i][j]:
                visited[i][j] = True
                bfs(i, j)
                res += 1 

    print(res)

