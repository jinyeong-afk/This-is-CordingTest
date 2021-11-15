import time
start_time = time.time()
n, m = map(int, input().split())
result = 0
for i in range(n):
    num = list(map(int, input().split()))
    min_value = min(num)
    result = max(result, min_value)
end_time = time.time()
print(result)
print(end_time - start_time)
