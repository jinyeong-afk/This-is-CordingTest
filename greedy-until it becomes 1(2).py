n , k = map(int, input().split())
count = 0
while n != 1:
    if n % k == 0:
        n = n / k
    else:
        n = n - 1
    count += 1

print(count)
    
