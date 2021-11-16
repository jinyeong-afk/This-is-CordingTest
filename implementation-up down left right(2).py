import time
start_time = time.time()
n = map(int, input().split())

move_root = list(map(str, input().split()))

x = 1
y = 1

for move in move_root:
    if move == 'R' and y != n:
        y += 1
    elif move == 'L' and y != 1:
        y -= 1
    elif move == 'U' and x != 1:
        x -= 1
    elif move == 'D' and x != n:
        x += 1
end_time = time.time()
print(x, ' ', y)
print(end_time - start_time)


#################################

start_time = time.time()
n = int(input())
x , y = 1, 1
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']
nx = 1
ny = 1
for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue
        x, y = nx, ny
end_time = time.time()
print(x, y)
print(end_time - start_time)
