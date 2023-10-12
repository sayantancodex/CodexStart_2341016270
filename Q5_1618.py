N = int(input())
ans = 0

while N > 0:
    N = N//5
    print(N)
    ans += N

print(ans)
