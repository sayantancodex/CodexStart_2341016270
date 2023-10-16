'''
Name: Sayantan Patra
Reg No: 2341016270
PS LINK: https://cses.fi/problemset/task/1083/
'''

N = int(input())
xum = 0

for i in range(1, N + 1):
    xum ^= i

numbers = list(map(int, input().split()))

for x in numbers:
    xum = xum^x

print(xum)
