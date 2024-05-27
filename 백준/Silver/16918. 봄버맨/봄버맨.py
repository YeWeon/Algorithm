from collections import deque 

r, c, n = map(int, input().split())

maps = []
for _ in range(r):
    maps.append(list(input()))

boom = []
def find_boom():
    for i in range(r):
        for j in range(c):
            if maps[i][j] == "O":
                boom.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs():
    q = deque(boom)

    while q:
        x, y = q.popleft()
        maps[x][y] = '.'
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and maps[nx][ny] == 'O':
                maps[nx][ny] = '.'

def all_boom():
    for i in range(r):
        for j in range(c):
            maps[i][j] = "O"

for i in range(1, n+1):
    if i == 1:
        find_boom();
    elif i % 2 == 0:
        all_boom();
    else:
        bfs(); 
        boom = []
        find_boom(); 

for i in range(r):
    for j in range(c):
        print(maps[i][j], end = "")
    print()
