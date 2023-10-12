n = int(input())
results = []

for k in range(1, n + 1):
    total_ways = k * k * (k * k - 1) // 2
    attacking_ways = 4 * (k - 1) * (k - 2)
    count = total_ways - attacking_ways
    results.append(count)

for result in results:
    print(result)
