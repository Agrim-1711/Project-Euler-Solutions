#Problem 34
#https://projecteuler.net/problem=34
#Find the sum of all numbers which are equal to the sum of the factorial of their digits

def factorial(f):
  if f == 0:
    return 1
  else:
    return f * factorial(f - 1)

total = 0

for n in range(3,100000):
  d = str(n)
  sum = 0
  for i in range(0,len(d)):
    sum += factorial(int(d[i]))
  if sum == n:
    print(n)
    total += n

print(total)