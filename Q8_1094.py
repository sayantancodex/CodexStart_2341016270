n = int(input())
arr = list(map(int, input().split()))

moves = 0

for i in range(1, n):
    if arr[i] < arr[i - 1]:
        diff = arr[i - 1] - arr[i]
        arr[i] += diff
        moves += diff

print(moves)
