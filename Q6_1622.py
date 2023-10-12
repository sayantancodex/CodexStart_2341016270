from itertools import permutations

input_str = input()
n = len(input_str)

permutations_set = set()
for perm_tuple in permutations(input_str, n):
    permutations_set.add(''.join(perm_tuple))


sorted_permutations = sorted(list(permutations_set))

print(len(sorted_permutations))
for perm in sorted_permutations:
    print(perm)
