'''
Name: Sayantan Patra
Reg No: 2341016270
PS LINK: https://cses.fi/problemset/task/1070/
'''

N = int(input())

if N == 1:
    print("1")
elif N <= 3:
    print("NO SOLUTION")
else:
    even_numbers = list(range(2, N + 1, 2))

    odd_numbers = list(range(1, N + 1, 2))
    # print(odd_numbers)
    numbers = even_numbers + odd_numbers
    # print(numbers)
    print(" ".join(map(str, numbers)))
