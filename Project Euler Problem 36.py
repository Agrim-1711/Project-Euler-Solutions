#Problem 36
#https://projecteuler.net/problem=36
#Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2

from reverse import rev

total = 0

for x in range(1,1000000):
  b = bin(x)
  a = list(str(b))
  for i in range(1,3):
    a.remove(a[0])
  y = int("".join(a))
  if x == rev(x) and y == rev(y) and a[0] != 0:
    # print(x)
    total += x

print(total)