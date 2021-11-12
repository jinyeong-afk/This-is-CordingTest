#n,m,k

n, m, k = map(int, input().split())
num = list(input().split())
sum = 0
count = 0

j = 0
num = list(map(int, num))
num.sort(reverse=True)

while True:
    for j in range(0,k):
        if count == m:
            break
        sum += num[0]
        count += 1
    if count == m:
        break
    sum += num[1]
    count += 1

print(sum)
