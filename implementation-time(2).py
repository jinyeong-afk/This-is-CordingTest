n = int(input())

count = 0

for hours in range(n+1):
    for minutes in range(60):
        for seconds in range(60):
            if '3' in str(hours) + str(minutes) + str(seconds):
                count += 1

print(count)
