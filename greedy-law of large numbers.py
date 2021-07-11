n, m ,k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()

result = 0

while m != 0:
    for j in range(k):
        result += data[-1]
        m -= 1
    result += data[-2]
    m -= 1

print(result)
