#Problem 43
#https://projecteuler.net/problem=43
#Find the sum of all 0 to 9 pandigital numbers with this property

import itertools
primes = [2,3,5,7,11,13,17]
digits = '0123456789'
pandigital = []

for p in itertools.permutations(digits):
  pandigital.append(''.join(p))

print(len(pandigital))

for num in pandigital:
  for a in range(1,8):
    sub_string = []
    for b in range(0,3):
      sub_string.append(num[a+b])
    string_num = int(str(''.join(sub_string)))
    if string_num % primes[a-1] != 0:
      pandigital.remove(num)
      break

print(len(pandigital))