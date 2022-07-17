#Problem 24
#https://projecteuler.net/problem=24
#What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9

from itertools import permutations

combinations = list(permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10))

#print(combinations)

ans = combinations[999999]

print(f"The millionth lexicographic permutation of the digits 0 to 9 is {ans}!")