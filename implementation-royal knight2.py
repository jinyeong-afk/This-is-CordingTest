import time

start_time = time.time()
idx = input()

x = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
y = list(range(9))

inx = 0
count = 0
move_x = [1, -1, 2, 2, 1, -1, -2, -2]
move_y = [-2, -2, 1, -1, 2, 2, -1, 1]
min_val = 1
max_val = 8

for key, value in x.items():
    if idx[0:1] == key:
        inx = value

iny = int(idx[1:2])

for i in range(len(move_x)):
    if inx + move_x[i] >= min_val and inx + move_x[i] <= max_val \
    and iny + move_y[i] >= min_val and iny + move_y[i] <= max_val:
        count += 1
end_time = time.time()
print(end_time - start_time)
print(count)

#####
start_time2 = time.time()
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

result = 0

for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1
end_time2 = time.time()
print(result)
print(end_time2 - start_time2)

