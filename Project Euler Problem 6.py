#Problem 6
#https://projecteuler.net/problem=6
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum

total1 = 0
total2 = 0

for a in range(1,101):
  total1 = total1 + (a*a)
print(total1)

for b in range(1,101):
  total2 = total2 + b
print(total2*total2)

diff = total2*total2 - total1

print(f"{diff} is the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum!")