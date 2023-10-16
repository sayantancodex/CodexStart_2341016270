'''
Name: Sayantan Patra
Reg No: 2341016270
PS LINK: https://cses.fi/problemset/task/1618/
'''


N = int(input())
ans = 0

while N > 0:
    N = N//5
    print(N)
    ans += N

print(ans)
