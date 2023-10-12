S = input()
N = len(S)
current = 1
best = 1

for i in range(1, N):
    if S[i] == S[i - 1]:
        current += 1
    else:
        current = 1
    best = max(best, current)

print(best)