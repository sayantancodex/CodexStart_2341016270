N = int(input())

while N > 1:
    print(N, end=' ')
    if N % 2 == 1:
        N = 3 * N + 1
    else:
        N //= 2

print(1)
