p, m = map(int, input().split()) 

rooms = []
for i in range(p):
    l, n = input().split()
    
    if not rooms:
        rooms.append([[int(l), n]])
        continue 

    flag = False
    for room in rooms:
        if len(room) < m and room[0][0] - 10 <= int(l) <= room[0][0] + 10:
            room.append([int(l), n])
            flag = True
            break 

    if not flag:
        rooms.append([[int(l), n]])

for room in rooms:
    room.sort(key=lambda x: x[1])

for room in rooms:
    if len(room) == m:
        print('Started!')
    else:
        print('Waiting!')
    for level, name in room:
        print(level, name)
    



