n = int(input())

maps = []
for i in range(n):
    maps.append(list(map(int, input())))

def dfs(x, y):
    global count

    if x < 0 or x >= n or y < 0 or y >= n:
        return False 
    
    if maps[x][y] == 1:
        maps[x][y] = 0
        count += 1 
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1) 
        return True 
    
    return False 

res = 0
house = []
for i in range(n):
    for j in range(n):
        count = 0
        if dfs(i, j):
            res += 1
            house.append(count)

house.sort() 
print(res)
for i in house:
    print(i)
