'''
Name: Sayantan Patra
Reg No: 2341016270
PS LINK: https://cses.fi/problemset/task/1754/
'''


T = int(input())
for t in range(T):
    a, b = map(int, input().split())
    if (a + b) % 3 == 0 and a <= 2 * b and b <= 2 * a:
        result = "YES"
    else:
        result = "NO"

    print(result)
