N = int(input())
xum = 0

for i in range(1, N + 1):
    xum ^= i

numbers = list(map(int, input().split()))

for x in numbers:
    xum = xum^x

print(xum)
